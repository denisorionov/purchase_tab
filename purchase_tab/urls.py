from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from request import views
from request.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('my_requests/', views.MyRequestsView.as_view(), name='my_requests'),
    path('new_requests/', views.NewRequestsView.as_view(), name='new_requests'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
