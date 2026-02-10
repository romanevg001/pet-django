from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

# Create your views here.
# def login_view(request: HttpRequest) -> HttpResponse:
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return  redirect('/shop/')
#         return render(request, 'myauth/login.html')
#
#     username = request.POST['username']
#     password = request.POST['password']
#
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/shop/')
#
#     return render(request, 'myauth/login.html', {'error': 'Invalid username and/or password.'})


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fuzz","buzz", max_age=3600)
    return response

def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fuzz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")

def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set")

def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")

# def logout_view(request: HttpRequest) -> HttpResponse:
#     logout(request)
#     return redirect(reverse("myauth:login"))

class MyLogout(LogoutView):
    next_page = reverse_lazy("myauth:login")
