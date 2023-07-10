import jwt


class DecodeUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if token:
            user_data = jwt.decode(token, 'secret', algorithms=['HS256'])
            request.user_data = user_data
        else:
            request.user_data = None

        response = self.get_response(request)

        return response