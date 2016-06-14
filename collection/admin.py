from django.contrib import admin

# Register your models here.

# import your model
from collection.models import todo

# and register it
admin.site.register(todo)