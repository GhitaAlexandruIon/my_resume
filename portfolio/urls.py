from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('home/<int:pk>/', views.projects_detail, name='projects_detail'),

]
