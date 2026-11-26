from application.llm.groq import GroqLLM
from application.llm.openai import OpenAILLM, AzureOpenAILLM
from application.llm.sagemaker import SagemakerAPILLM
from application.llm.huggingface import HuggingFaceLLM
from application.llm.llama_cpp import LlamaCpp
from application.llm.anthropic import AnthropicLLM
from application.llm.docsgpt_provider import DocsGPTAPILLM
from application.llm.premai import PremAILLM
from application.llm.google_ai import GoogleLLM
from application.llm.novita import NovitaLLM


class LLMCreator:
    llms = {
        "openai": OpenAILLM,
        "azure_openai": AzureOpenAILLM,
        "sagemaker": SagemakerAPILLM,
        "huggingface": HuggingFaceLLM,
        "llama.cpp": LlamaCpp,
        "anthropic": AnthropicLLM,
        "docsgpt": DocsGPTAPILLM,
        "premai": PremAILLM,
        "groq": GroqLLM,
        "google": GoogleLLM,
        "novita": NovitaLLM,
    }

    @classmethod
    def create_llm(cls, llm_type, api_key, user_api_key, decoded_token=None, *args, **kwargs):
        llm_type_key = str(llm_type).lower() if llm_type is not None else ""
        llm_class = cls.llms.get(llm_type_key)
        if not llm_class:
            raise ValueError(f"No LLM class found for type {llm_type}")
        return llm_class(
            api_key, user_api_key, decoded_token=decoded_token, *args, **kwargs
        )
