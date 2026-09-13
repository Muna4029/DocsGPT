from application.api.answer.routes import answer_blueprint as answer

from application.api import api
from application.api.answer.routes.answer import AnswerResource
from application.api.answer.routes.base import answer_ns
from application.api.answer.routes.stream import StreamResource


api.add_namespace(answer_ns)


def init_answer_routes():
    api.add_resource(StreamResource, "/stream")
    api.add_resource(AnswerResource, "/api/answer")


init_answer_routes()

__all__ = ["answer"]
