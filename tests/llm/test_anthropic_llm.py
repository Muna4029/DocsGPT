import sys
import types
import pytest


class _FakeCompletion:
    def __init__(self, text):
        self.completion = text


class _FakeCompletions:
    def __init__(self):
        self.last_kwargs = None
        self._stream = [_FakeCompletion("s1"), _FakeCompletion("s2")]

    def create(self, **kwargs):
        self.last_kwargs = kwargs
        if kwargs.get("stream"):
            return self._stream
        return _FakeCompletion("final")


class _FakeAnthropic:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.completions = _FakeCompletions()


@pytest.fixture(autouse=True)
def patch_anthropic(monkeypatch):
    fake = types.ModuleType("anthropic")
    fake.Anthropic = _FakeAnthropic
    fake.HUMAN_PROMPT = "<HUMAN>"
    fake.AI_PROMPT = "<AI>"
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    # If application.llm.anthropic was already imported (e.g. by another test
    # that imported application.llm.llm_creator), its module-level names are
    # already bound to the real anthropic classes.  Override them to use the
    # fake so that real API calls are never made.
    if "application.llm.anthropic" in sys.modules:
        import application.llm.anthropic as mod

        monkeypatch.setattr(mod, "Anthropic", _FakeAnthropic)
        monkeypatch.setattr(mod, "HUMAN_PROMPT", "<HUMAN>")
        monkeypatch.setattr(mod, "AI_PROMPT", "<AI>")


def test_anthropic_raw_gen_builds_prompt_and_returns_completion():
    from application.llm.anthropic import AnthropicLLM

    llm = AnthropicLLM(api_key="k")
    msgs = [
        {"content": "ctx"},
        {"content": "q"},
    ]
    out = llm._raw_gen(
        llm, model="claude-2", messages=msgs, stream=False, max_tokens=55
    )
    assert out == "final"
    last = llm.anthropic.completions.last_kwargs
    assert last["model"] == "claude-2"
    assert last["max_tokens_to_sample"] == 55
    assert last["prompt"].startswith("<HUMAN>") and last["prompt"].endswith("<AI>")
    assert "### Context" in last["prompt"] and "### Question" in last["prompt"]


def test_anthropic_raw_gen_stream_yields_chunks():
    from application.llm.anthropic import AnthropicLLM

    llm = AnthropicLLM(api_key="k")
    msgs = [
        {"content": "ctx"},
        {"content": "q"},
    ]
    gen = llm._raw_gen_stream(
        llm, model="claude", messages=msgs, stream=True, max_tokens=10
    )
    chunks = list(gen)
    assert chunks == ["s1", "s2"]
