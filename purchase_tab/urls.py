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
    path('register/', views.RegisterView.as_view(), name='register'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
