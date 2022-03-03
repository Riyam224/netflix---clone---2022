from django.contrib import admin

# Register your models here.

from .models import Customer , Profile , Movie , Video


admin.site.register(Customer)

admin.site.register(Profile)

admin.site.register(Movie)

admin.site.register(Video)