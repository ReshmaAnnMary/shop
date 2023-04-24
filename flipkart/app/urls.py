from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.all_product, name='all_category'),
    path('<slug:c_slug>/', views.all_product, name='product_by_category'),
    path('<slug:c_slug>/<slug:pro_slug>/', views.pro_details, name='pro_details'),
]
