from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    # If the method is POST, it means the form was submitted.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # If the form is valid, we need to save the user.
        if form.is_valid():
            form.save()
            # After saving we want to redirect.
            return redirect("posts:list")
    # If the method is not POST is because the form is not submitted. Show the empty form.
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
