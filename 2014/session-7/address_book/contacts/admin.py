from django.contrib import admin
from .models import Contact, Address

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'mobile')
	list_filter = ['name']

class AddressAdmin(admin.ModelAdmin):
	list_display = ('street_address', 'pincode')
	list_filter = ['pincode']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
