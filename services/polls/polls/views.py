from rest_framework import generics
from polls.serializers import PollSerializer
from polls.models import Poll


class PollAPIView(generics.ListAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
