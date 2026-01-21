from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product,Order


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
       #"groups": Group.objects.all(),
       "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, "shopapp/groups-list.html", context = context)


def products_list(request: HttpRequest) -> HttpResponse:
    context = {
       "products": Product.objects.all(),
    }
    return render(request, "shopapp/products-list.html", context = context)

def orders_list(request: HttpRequest) -> HttpResponse:
    class Employee:

        def __init__(self, name):
            print('Employee'+name)
            self.__name = name

        @property
        def name(self):
            return self.__name

        def work(self):
            print(f"{self.name} works")

    class Student:

        def __init__(self, name):
            print('Student'+name)

            self.__name = name

        @property
        def name(self):
            return self.__name

        def study(self):
            print(f"{self.name} studies")

    class WorkingStudent(Employee, Student):
        pass

    tom = WorkingStudent("Tom")
    tom.work()
    tom.study()

    class Person:
        name = "Undefined"

        def __init__(self, name, age):
            self.name = name
            self.__age = age

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            if 0 < age < 110:
                self.__age = age
            else:
                print("Недопустимый возраст")

        def print_name(self):
            print('name: ',self.name)
            print('age: ',self.age)

    print('-----------')

    tom = Person('tom',23)
    bob = Person('bob',35)
    print('-----------')

    tom.print_name()  # Undefined
    bob.print_name()  # Undefined
    print('-----------')

    Person.name = "Nikolskaya"
    bob.name = "Bob"

    bob.print_name()  # Bob
    tom.print_name()  # Undefined

    context = {
       "orders": Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, "shopapp/orders-list.html", context = context)

