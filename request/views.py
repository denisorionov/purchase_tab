from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View


@login_required(login_url='login')
def home_view(request):
    return render(request, 'request/home.html')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        return render(request, 'request/register.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        return render(request, 'request/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'request/login.html', context={'invalid': True})
