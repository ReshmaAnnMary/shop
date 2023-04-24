from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.cart_minus, name='cart_minus'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
]
