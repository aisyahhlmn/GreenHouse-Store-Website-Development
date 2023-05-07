from django.contrib import admin
from .models import SignIn, SignUp, Checkout, Product, Cart
# Register your models here.

admin.site.register(SignIn)
admin.site.register(SignUp)
admin.site.register(Checkout)
admin.site.register(Product)
admin.site.register(Cart)