from django.urls import path
from . import views

urlpatterns = [
    
    path('api/problems/', views.problem_list),
]