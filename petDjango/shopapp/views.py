from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def shop_index(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("Hello, world. You're at the shop index.")
