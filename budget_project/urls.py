from django.contrib import admin
from django.urls import path, include
from budget import views
from reporting import views as reporting_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('report/chart/', reporting_views.expenses_chart_view, name='chart'),
    path('report/chart/data/', reporting_views.expenses_chart_data, name='chart_data'),
    path('captcha/', include('captcha.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
