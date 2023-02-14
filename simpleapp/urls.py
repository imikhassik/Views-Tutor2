from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate, ProductUpdate
)


urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update')
]
