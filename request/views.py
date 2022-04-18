from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


@login_required(login_url='login')
def home_view(request):
    return render(request, 'request/home.html')


class SignupView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse('login'))

        return render(request, 'request/signup.html')


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


class RequestsView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        return render(request, 'request/requests.html')


