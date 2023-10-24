from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(null=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    image = models.TextField()

    def __str__(self):
        return '{name: %s, price: %s}' % (self.name, self.price)

    def to_dict(self):
        return {"name": self.name, "description": self.description,
                "price": self.price, "image": self.image}


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{order: %s,  product: %s, quantity: %s' % (
            self.order, self.product, self.quantity)


class Order(models.Model):
    username = models.CharField(max_length=200)
    items = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return '{username: %s, items: %s}' % (self.username, self.items)



