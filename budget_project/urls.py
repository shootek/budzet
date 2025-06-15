from django.contrib import admin
from django.urls import path
from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),


]
