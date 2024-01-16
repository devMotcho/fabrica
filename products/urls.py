from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    ProductListView,
    deleteProduct,
    updateProduct,

    viewInventary,

    viewProduction,
    editProduction,
)

app_name = 'products'

urlpatterns = [
    path('', login_required(ProductListView.as_view()), name='products'),
    path('delete/<str:pk>/', deleteProduct, name='delete'),
    path('update/<str:pk>/', updateProduct, name='update'),
    path('inv/', viewInventary, name='inv'),
    path('productions/', viewProduction, name='productions'),
    path('edit-production/<str:pk>/', editProduction, name='edit-production'),

]