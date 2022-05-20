from django.http import JsonResponse
import json


def api_home(request):
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)
    finally:
        pass
    print(data)

    return JsonResponse(data)
