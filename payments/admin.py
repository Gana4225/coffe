from django.contrib import admin
from .models import *


class gana(admin.ModelAdmin):
    list_display = ("pid","name")
admin.site.register(coff,gana)

class data(admin.ModelAdmin):
    list_display = ("name", "price")
admin.site.register(cofffdata, data)