from .models import Product, Order, OrderItem
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

    def create(self, validated_data):
        print('validated_data')
        print(validated_data)
        product_id = validated_data.pop('product')
        quantity = validated_data.get('quantity')
        product = Product.objects.get(id=product_id)
        order_item = OrderItem.objects.create(product=product, quantity=quantity, **validated_data)
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=False)
    class Meta:
        model = Order
        fields = ['id', 'username', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_id = item_data.pop('product')
            product = Product.objects.get(id=product_id)
            order_item = OrderItem.objects.create(order=order, product=product, **item_data)
        return order

