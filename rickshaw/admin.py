from django.contrib import admin
from .models import Rickshaw, Cargo


class RickshawAdmin(admin.ModelAdmin):
    list_display = ['driver', 'session', 'paid', 'saved']


class CargoAdmin(admin.ModelAdmin):
    list_display = ['rickshaw', 'product', 'quantity', 'price']


admin.site.register(Rickshaw, RickshawAdmin)
admin.site.register(Cargo, CargoAdmin)
