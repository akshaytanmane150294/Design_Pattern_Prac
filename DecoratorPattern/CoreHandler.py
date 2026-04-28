
from Handlerfile import Handler


class RequestHandler(Handler):
    def handle(self, request: dict):
        print(f'Processing: {request['path']}')
        return {'status': 200, 'body': "Success"}
