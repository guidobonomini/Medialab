from django.http import JsonResponse

from medialab.polls.services import PollsService

def service_view(path):
    def view(request, **kwargs):
        clean_path = path.format(username=request.user.username, **kwargs)

        polls_service = PollsService()
        response = polls_service.request(request.method, clean_path, request.GET, request.user.get_jwt())
        return JsonResponse(response.json())

    return view