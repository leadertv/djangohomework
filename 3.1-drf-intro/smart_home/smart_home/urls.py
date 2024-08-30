from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include('measurement.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты
]
