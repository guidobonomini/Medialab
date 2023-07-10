import json
import jwt

from unittest.mock import Mock
from django.test import TestCase

from polls.middleware import DecodeUserMiddleware


class MiddlewareTestCase(TestCase):
    def test_middleware_decodes_jwt(self):
        user_data = {'id': 1, 'username': 'user@gmail.com'}
        token = jwt.encode(user_data, 'secret', algorithm='HS256')
        request = Mock()
        request.headers = {'Authorization': f'Bearer {token}'}

        middleware = DecodeUserMiddleware(Mock())
        middleware(request)

        self.assertEqual(request.user_data, user_data)

    def test_middleware_without_token(self):
        request = Mock()
        request.headers = {}

        middleware = DecodeUserMiddleware(Mock())
        middleware(request)

        self.assertEqual(request.user_data, None)


