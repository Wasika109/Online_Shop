from django.db import models


# Create your models here.

class user_upload(models.Model):
    user_id = models.IntegerField()
    user_image = models.ImageField()


class log_in(models.Model):
    user_name = models.CharField(max_length=25)
    user_password = models.CharField(max_length=25)
    user_email = models.CharField(max_length=25)


class customer_product(models.Model):
    c_product_title = models.CharField(max_length=25)
    c_product_image = models.ImageField()
    c_product_cost = models.FloatField()
    user_id = models.IntegerField()


class cart(models.Model):
    order_id = models.IntegerField()
    product_title = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    quantity = models.IntegerField()
    total_bill = models.FloatField()


class product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=25)
    product_image = models.ImageField()
    product_price = models.FloatField()
    cat_name = models.CharField(max_length=25)


class category(models.Model):
    cat_name = models.CharField(max_length=25)
    cat_description = models.CharField(max_length=25)


class order(models.Model):
    order_id = models.IntegerField()
    user_name = models.CharField(max_length=25)
    user_id = models.IntegerField()
    user_contact = models.IntegerField()
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
