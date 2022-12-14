from django.contrib import admin

from .models import user, customer, customer_product, cart, product, category, order

admin.site.register(user)
admin.site.register(customer)
admin.site.register(customer_product)
admin.site.register(cart)
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)



# Register your models here.
