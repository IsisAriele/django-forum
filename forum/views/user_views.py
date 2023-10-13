from django.views import View
from django.shortcuts import render, redirect
from forum.forms.user_form import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class UserRegisterView(View):
    def get(self, request):
        context = {"form": UserRegistrationForm()}
        return render(request, "forum/register.html", context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.data["username"],
                email=form.data["email"],
                password=form.data["password"],
                first_name=form.data["first_name"],
                last_name=form.data["last_name"],
            )

            user.save()

            return redirect("login")

        # Deu problema
        return render(request, "forum/register.html", {"form": form})

class UserLoginView(View):
    def get(self, request):
        context = {"form": UserLoginForm()}
        return render(request, "forum/login.html", context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            user = authenticate(username=form.data["username"], password=form.data["password"])
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "forum/login.html", {"form": form, "message": "Username or password is invalid"})

        return render(request, "forum/login.html", {"form": form})
