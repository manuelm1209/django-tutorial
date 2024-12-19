from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
    return render(request, "users/user.html")

# def user(request):
#     return render(request, "users/user.html")

def register_view(request):
    # If the method is POST, it means the form was submitted.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # If the form is valid, we need to save the user.
        if form.is_valid():
            # form.save()
            # form.save() also returs the user valua as form.get() from the login form.
            login(request, form.save())
            # After saving we want to redirect.
            return redirect("posts:list")
    # If the method is not POST is because the form is not submitted. Show the empty form.
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # We are getting the user with form.get_user
            login(request, form.get_user())
            # If we are getting "Next" from the conditional in the login.html page, we return the value of "next", otherwise we redirect the user to "posts:list"
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")