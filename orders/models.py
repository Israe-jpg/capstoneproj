from django.db import models
from products.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Check if stock is sufficient
        if self.product.stock_quantity >= self.quantity:
            # Reduce the stock quantity when an order is placed
            self.product.stock_quantity -= self.quantity
            self.product.save()
        else:
            raise ValueError("Not enough stock to fulfill the order.")
        super(Order, self).save(*args, **kwargs)
