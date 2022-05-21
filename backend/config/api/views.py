from django.http import JsonResponse
import json
from product.models import Product
from django.forms.models import model_to_dict


def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])

    return JsonResponse(data)
