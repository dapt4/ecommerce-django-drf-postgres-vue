from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(null=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    image = models.TextField()

    def __str__(self):
        return '{name: %s, price: %s}' % (self.name, self.price)


class OrderItem(models.Model):
    product = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{ product: %s, quantity: %s }' % (self.product, self.quantity)


class Order(models.Model):
    username = models.CharField(max_length=200)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return '{username: %s, items: %s}' % (self.username, self.items)



