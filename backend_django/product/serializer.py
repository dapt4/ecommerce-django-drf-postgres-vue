from .models import Product, Order, OrderItem, InvoiceItem, Invoice
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=False)
    class Meta:
        model = Order
        fields = ['id', 'username', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            order_item = OrderItem.objects.create(order=order, **item_data)
            order.items.add(order_item)
        return order

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['name', 'price', 'quantity']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=False)
    class Meta:
        model = Invoice
        fields = ['id','username', 'items', 'amount']

    def create(self, validated_data):
        invoice_items = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        amount = 0.0
        for item in invoice_items:
            product = Product.objects.get(id=item.product)
            invoice_item = InvoiceItem(name=product.name, price=product.price,
                                        quantity=item.quantity)
            amount += product.price * item.quantity
            invoice.items.add(invoice_item)
        invoice.amount = amount
        return invoice

