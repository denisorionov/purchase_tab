from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from purchase_order import views
from purchase_order.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('my_purchase_orders/', views.MyPurchaseOrdersView.as_view(), name='my_purchase_orders'),
    path('new_purchase_order/', views.NewPurchaseOrderView.as_view(), name='new_purchase_order'),
    path('order/<int:id>/', views.EditPurchaseOrderView.as_view(), name='edit_order'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
