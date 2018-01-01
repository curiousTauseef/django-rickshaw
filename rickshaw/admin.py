from django.contrib import admin
from .models import Rickshaw, Cargo


class RickshawAdmin(admin.ModelAdmin):
    list_display = ['driver', 'paid', 'saved']


admin.site.register(Rickshaw, RickshawAdmin)
admin.site.register(Cargo)
