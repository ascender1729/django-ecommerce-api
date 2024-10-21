from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity', 'price']

    def validate_product_id(self, value):
        try:
            Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'items', 'created_at', 'updated_at']
        read_only_fields = ['user', 'total_price', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_price = 0

        for item_data in items_data:
            product = Product.objects.get(id=item_data['product_id'])
            if product.stock < item_data['quantity']:
                raise serializers.ValidationError(f"Not enough stock for {product.name}")
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data['quantity'],
                price=product.price
            )
            total_price += product.price * item_data['quantity']
            product.stock -= item_data['quantity']
            product.save()

        order.total_price = total_price
        order.save()
        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance