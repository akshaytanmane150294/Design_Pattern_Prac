
from Handlerfile import Handler


class Middleware(Handler):
    def __init__(self, handler: Handler):
        self._handler = handler

    def handle(self, request: dict):
        return self._handler.handle(request)
