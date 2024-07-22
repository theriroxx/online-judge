from django.urls import path
from . import views

urlpatterns = [
    path('', views.problem_list, name='problem_list'),
    path('create/', views.create_problem, name='create_problem'),
    path('edit/<int:problem_id>/', views.edit_problem, name='edit_problem'),
    path('<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('<int:problem_id>/submit/', views.submit_code, name='submit_code'),
]
