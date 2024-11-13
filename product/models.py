
from django.db import models
from django.conf import settings

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_weight = models.CharField(max_length=50)
    storage_method = models.TextField()
    discount_percentage = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True,blank=True)

    def __str__(self):
        return self.name

    def get_discount_amount(self):
        if self.discount_price:
            return self.price - self.discount_price
        return 0

    def get_discount_percentage(self):
        if self.discount_price:
            discount_percentage = ((self.price - self.discount_price) / self.price) * 100
            return round(discount_percentage, 2)
        return 0
    


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    @property
    def subtotal(self):
        return self.product.price*self.quantity
        
    def __str__(self) -> str:
            return f"{'self.quantity'} x {'self.product.name'}"
