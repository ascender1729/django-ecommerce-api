from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('product-list', request=request, format=format),
        'cart': reverse('cart-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
    })