from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

##
from .forms import registForm, loginForm

##

# Create your views here.
def index(request):
    title = "Login"

    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # messages.success(request, 'You have successfully logged in.')
                # logger.info(f"User {username} logged in successfully.")
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
                messages.error(request, 'Invalid username or password.')
                # logger.warning(f"Failed login attempt for username: {username}")
        else:
            messages.error(request, 'Invalid form submission.')
            # logger.warning("Invalid form submission.")
    else:
        form = loginForm()
        # logger.debug("Login form requested.")

    return render(request, 'accounts/index.html', {'form': form, 'title': title})

def register(request):
    title = "Sign Up"

    if request.method == 'POST':
        form = registForm(request.POST)
        messages = error.WARNING("")
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = registForm()
        return redirect('index')

@login_required(login_url='index')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')

@login_required(login_url='index')
def homepage(request):
    title = "Home"
    return render(request, 'accounts/homepage.html')

