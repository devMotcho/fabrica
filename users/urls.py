from django.urls import path

from .views import (
    loginView,
    logoutUser,
)
app_name = 'users'

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutUser, name='logout'),
]
