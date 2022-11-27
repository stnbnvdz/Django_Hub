from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_resources, name='view_resources'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
]