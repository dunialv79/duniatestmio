from django.urls import path

from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('store', views.store, name="store"),
    path('about', views.about, name="about"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
