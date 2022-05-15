from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from purchase_order.forms import PurchaseOrderForm
from purchase_order.models import PurchaseOrder


@login_required(login_url='login')
def home_view(request):
    managers = User.objects.filter(groups__name__in=['managers']).annotate(
        qt=Count('purchase_orders', filter=Q(
            purchase_orders__status__in=['review', 'rework', 'reparation_documentation', 'agreement_documentation',
                                         'rework_documentation', 'approval', 'negotiation', 'signing_contract'])))
    purchase_orders = list(PurchaseOrder.objects.all())

    saving = {}

    for purchase_order in purchase_orders:
        try:
            saving[purchase_order.id] = round((100 - (purchase_order.contract_price * 100 / purchase_order.amount)), 2)
        except:
            saving[purchase_order.id] = 0

    return render(request, 'purchase_order/home.html',
                  context={'purchase_orders': purchase_orders, 'managers': managers, 'saving': saving})


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

        return render(request, 'purchase_order/signup.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        return render(request, 'purchase_order/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'purchase_order/login.html', context={'invalid': True})


class MyPurchaseOrdersView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user = auth.get_user(request)
        purchase_orders = PurchaseOrder.objects.filter(employee_dkz_id=user.id)
        return render(request, 'purchase_order/my_purchase_orders.html', context={'purchase_orders': purchase_orders})


class NewPurchaseOrderView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        purchase_order_form = PurchaseOrderForm()

        return render(request, 'purchase_order/purchase_order.html', context={'form': purchase_order_form})

    def post(self, request):
        purchase_order_form = PurchaseOrderForm(request.POST)

        if purchase_order_form.is_valid():
            purchase_order_form.save(commit=False)
            purchase_order_form.instance.employee_dkz = request.user
            purchase_order_form.save()

            return redirect('my_purchase_orders')

        return render(request, 'purchase_order/purchase_order.html', context={'form': purchase_order_form})


class EditPurchaseOrderView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        manager = auth.get_user(request)

        if PurchaseOrder.objects.filter(employee_dkz__id=manager.id).filter(id=id):
            purchase_order_form = PurchaseOrderForm(instance=PurchaseOrder.objects.filter(id=id).first())
            return render(request, 'purchase_order/purchase_order.html', context={'form': purchase_order_form})

        raise Http404

    def post(self, request, id):
        purchase_order_form = PurchaseOrderForm(request.POST, instance=PurchaseOrder.objects.filter(id=id).first())

        if purchase_order_form.is_valid():
            purchase_order_form.save(commit=False)
            purchase_order_form.instance.employee_dkz = request.user
            purchase_order_form.save()

            return redirect('my_purchase_orders')

        return render(request, 'purchase_order/purchase_order.html', context={'form': purchase_order_form})
