from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('users.urls')),
    path('', include('dashboard.urls')),
    path('products/', include('products.urls')),
]
