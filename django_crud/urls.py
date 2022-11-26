from django.contrib import admin
from django.urls import path
from dashboard import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.data_form, name='data_create'),
    path('data/', views.data_form, name='data_read'),
    path('<int:id>', views.data_form, name='data_update'),
    path('data_delete/<str:candidate_id>', views.data_form, name='data_delete'),
]