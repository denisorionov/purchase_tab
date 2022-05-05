from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from request.models import Request


@login_required(login_url='login')
def home_view(request):
    managers = User.objects.filter(groups__name__in=['managers']).annotate(
        qt=Count('requests', filter=Q(
            requests__status__in=['review', 'rework', 'reparation_documentation', 'agreement_documentation',
                                  'rework_documentation', 'approval', 'negotiation', 'signing_contract'])))
    requests = list(Request.objects.all())

    saving = {}

    for r in requests:
        try:
            saving[r.id] = round((100 - (r.contract_price * 100 / r.amount)), 2)
        except:
            saving[r.id] = 0
    print(saving)
    return render(request, 'request/home.html', context={'requests': requests, 'managers': managers, 'saving': saving})


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


class MyRequestsView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user = auth.get_user(request)
        requests = Request.objects.filter(employee_dkz_id=user.id)
        return render(request, 'request/my_requests.html', context={'requests': requests})


class NewRequestsView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user = auth.get_user(request)
        requests = Request.objects.filter(employee_dkz_id=user.id)
        return render(request, 'request/new_requests.html', context={'requests': requests})
