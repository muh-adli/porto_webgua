from django.shortcuts import render
from django.contrib.auth.decorators import login_required

##
from .forms import registForm, loginForm

##

# Create your views here.
def index(request):
    title = "Home"

    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = loginForm()

    return render(request, 'accounts/index.html', {'form': form})

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
    return redirect('index')

@login_required(login_url='index')
def homepage(request):
    title = "Home"
    return render(request, 'accounts/homepage.html')

