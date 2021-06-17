from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
        )
    # name=models.CharField(null=True)

    name = models.CharField(max_length=30,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=30,null=True, choices=CATEGORY)
    description=models.CharField(max_length=300,null=True,blank=True)
    date_created=date_created=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
   
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    #one to maney relation  and on delete becouse whenever customer is deleted Order is not deleted

    
    customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)

    #status deliver is ok or pending
    status=models.CharField(max_length=30,null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
    




