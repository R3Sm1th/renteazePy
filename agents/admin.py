from django.contrib import admin

# Register your models here.
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_mvp')
    list_editable = ('is_mvp',)
    search_fields = ('first_name', 'last_name')
    list_per_page = 25

admin.site.register(Agent, AgentAdmin)
