
from BaseDecorator import *
from CoreHandler import *


class LoggingMiddleware(Middleware):
    def __init__(self, handle):
        super().__init__(handle)

    def handle(self, request: dict):
        print(f"[LOG] {request['method']} {request['path']}")

        response = super().handle(request)
        print(f'[LOG] Response:{response['status']}')
        return response


class AuthMiddleWare(Middleware):
    def __init__(self, handle):
        super().__init__(handle)

    def handle(self, request):
        if not request.get('token'):
            return {"status": 401, 'body': "Unauthorized"}

        print("[AUTH] Token valid")
        return super().handle(request)


class RateLimitingMiddleware(Middleware):
    def __init__(self, handler, limit=100):
        super().__init__(handler)
        self._count = 0
        self._limit = limit

    def handle(self, request: dict):
        self._count += 1
        if self._count > self._limit:
            return {'status': 429, 'body': 'Too many Request'}

        return super().handle(request)


pipeline = RequestHandler()
pipeline = LoggingMiddleware(pipeline)
pipeline = AuthMiddleWare(pipeline)
pipeline = RateLimitingMiddleware(pipeline, limit=100)

res = pipeline.handle({
    "method": "GET",
    "path": "/api/users",
    "token": "Bearer xyz"
})

print(res)
