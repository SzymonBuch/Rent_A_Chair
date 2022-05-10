from django.urls import path

from . import views


urlpatterns = [
    path('new_product', views.new_product, name="new_product"),
    path('product_csv', views.product_csv, name="product_csv"),
    path('new_worker',views.new_worker, name="new_worker"),
    path('new_storage',views.new_storage, name="new_storage"),

]