from django.urls import path
from .views import ProductsList, ProductDetail


urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
]
