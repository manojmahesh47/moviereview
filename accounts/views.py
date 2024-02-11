from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth import logout


def register(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect("main:home")
        else:
            form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect("main:home")
            else:
                return render(request, 'accounts/login.html',
                              {"error": "Your account has been disabled or Invalid Username or Password"})

        return render(request, 'accounts/login.html')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        print("Logged Out successfully")
    return redirect("accounts:login")

from .forms import EditProfileForm

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect to the home page or a profile view
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'main/edit_profile.html', {'form': form})

def view_profile(request):
    return render(request, 'main/view_profile.html')