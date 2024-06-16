from custom_auth.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sessions.models import Session


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(
                request,
                "custom_auth/login.html",
                {"error": "Invalid username or password"},
            )
        login(request, user)
        request.session["role"] = user.role
        request.session.save()
        return redirect("articles:home")
    else:
        return render(request, "custom_auth/login.html")


def logout_view(request):
    logout(request)
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect("home")


def success_view(request):
    return render(request, "custom_auth/success.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "custom_auth/register.html", {"form": form})
