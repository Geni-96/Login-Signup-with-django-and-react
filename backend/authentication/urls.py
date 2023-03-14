from django.urls import path
from . import views

urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('logout/', views.LogoutView.as_view(), name ='logout'),
     path('register/', views.register),
     path('token/', views.token),
     path('token/refresh/', views.refresh_token),
     path('token/revoke/', views.revoke_token),
]