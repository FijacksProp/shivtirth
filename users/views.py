from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from django.views import View

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)

class CustomLogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('login')

# def login(request):
#     return render(request, 'users/login.html')