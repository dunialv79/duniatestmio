from django.urls import path

from frontend import views
urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('store', views.store, name="store"),
    path('about', views.about, name="about"),
]
