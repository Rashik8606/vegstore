from django.urls import path
from . import views


urlpatterns = [
    path('accounts/login/',views.loginview,name = 'login'),
    path('logout/',views.logoutview,name='logout'),
    path('accounts/register',views.sign_upview,name='register'),
]

