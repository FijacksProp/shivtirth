from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import CustomLogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
