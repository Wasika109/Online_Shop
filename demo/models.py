from django.db import models



# Create your models here.

class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=25)
    user_image=models.ImageField()
    user_contact=models.IntegerField()


class customer(models.Model):
     customer_id = models.IntegerField(primary_key=True)
     customer_name = models.CharField(max_length=200, null=True)
     customer_image = models.ImageField()
     customer_phone = models.IntegerField()
     customer_address = models.CharField(max_length=50, null=True)

class customer_product(models.Model):
   # product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer_product_title = models.CharField(max_length=25)
    customer_product_image = models.ImageField()
    customer_product_cost = models.FloatField()
    customer_product_discount = models.FloatField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)


class cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    cart_status = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    total_price = models.FloatField()


class product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=25)
    product_image = models.ImageField()
    product_price = models.FloatField()
    cat_name = models.CharField(max_length=25)


class category(models.Model):
    cat_name = models.CharField(max_length=25)
    cat_description = models.CharField(max_length=25)


class order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    total_cost = models.FloatField()
    customer_name = models.CharField(max_length=25)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    customer_phone = models.IntegerField()
    customer_address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)


