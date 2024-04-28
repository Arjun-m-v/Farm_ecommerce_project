from django.contrib import admin
from django.urls import path,include
from .views import LoginView,RegisterView,LogoutView

urlpatterns = [
        path('login',LoginView.as_view(),name="log"),
        path('reg',RegisterView.as_view(),name="reg"),
        path('logout',LogoutView.as_view(),name="logout"),

]
