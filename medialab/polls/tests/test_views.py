import json

from unittest.mock import patch, Mock

from django.test import TestCase, RequestFactory

from medialab.users.tests.factories import UserFactory
from medialab.polls.views import service_view


class FakeResponse:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data

class ItemsServiceViewTestCase(TestCase):
    def test_get_service_view_asks_to_service(self):
        user = UserFactory()
        MockService = Mock()
        mock_service = MockService.return_value
        mock_service.request.return_value = FakeResponse({'foo': 'bar'}, 200)
        status_view = service_view('/polls')

        request = RequestFactory().get('/polls')
        request.user = user
        with patch('polls.views.PollsService', MockService):
            response = status_view(request)

        mock_service.request.assert_called_once_with(
            'GET',
            '/polls',
            {},
            user.get_jwt(),
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertEqual(data, {'foo': 'bar'})