from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('email', 'name', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
