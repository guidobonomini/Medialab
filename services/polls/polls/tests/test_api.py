import pytest
from rest_framework.test import APIRequestFactory

from polls.views import PollAPIView
from polls.tests.factories import PollFactory


class TestPollAPIView:
    @pytest.fixture
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_get_list_polls(self, user: User, api_rf: APIRequestFactory):
        view = PollAPIView()
        PollFactory(category='Cinema', vote=10)
        request = api_rf.get("/polls")
        request.user = user

        view.request = request

        response = view.request(request)

        assert response.data == [{
            "vote": 10,
            "category": "Cinema"
        }]