from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

@login_required()
def homepage(request):
    return render(request, 'accounts/homepage.html')

@login_required()
def register(request):
    return redirect('homepage')

@login_required()
def logout(request):
    return redirect('index')