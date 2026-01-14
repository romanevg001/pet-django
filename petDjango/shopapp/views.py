from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def shop_index(request: HttpRequest) -> HttpResponse:
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Mouse', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products
    }
    return render(request, "shopapp/shop-index.html", context = context)
    #print(request)
    #return HttpResponse("Hello, world. You're at the shop index.")


def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
       "groups": Group.objects.all(),
    }
    return render(request, "shopapp/groups-list.html", context = context)
