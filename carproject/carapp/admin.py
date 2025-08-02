from django.contrib import admin
from carapp.models import *
# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
@admin.register(apponment)
class apponmentAdmin(admin.ModelAdmin):
    list_display = ('vehicle_year','vehicle_make','vehicle_mileage','date','time','service','Name2', 'email2', 'number2', 'message2')    