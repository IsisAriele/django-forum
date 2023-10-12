from django.views import View
from django.shortcuts import render
from forum.forms.user_form import UserRegistrationForm
from django.contrib.auth.models import User


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

            return render(request, "forum/login.html", {"message": "Registration completed successfully"})

        # Deu problema
        return render(request, "forum/register.html", {"form": form})
