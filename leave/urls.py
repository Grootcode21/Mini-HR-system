from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply/', views.apply_leave, name='apply_leave'),
    path('all/', views.leave_list, name='leave_list'),
    path('approve/<int:pk>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:pk>/', views.reject_leave, name='reject_leave'),
    path('register/', views.register, name='register'),

]
