from django.contrib import admin
from django.urls import path
from budget import views
from reporting import views as reporting_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),

    # 📊 Wykres wydatków
    path('report/chart/', reporting_views.expenses_chart_view, name='chart'),

    # 📧 Wysyłanie raportu e-mailem
    path('report/email/', reporting_views.send_report_email, name='send_email'),
]
