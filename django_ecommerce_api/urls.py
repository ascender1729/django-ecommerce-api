from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import api_root

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]