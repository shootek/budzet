from django.contrib import admin
from django.urls import path
from budget import views
from reporting import views as reporting_views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('report/chart/', reporting_views.expenses_chart_view, name='chart'),
    path('captcha/', include('captcha.urls')),

]
