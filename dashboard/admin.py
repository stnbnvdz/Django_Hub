from django.contrib import admin

from .models import DjangoHub, NameOfTutorial

class DjangoHubAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'tags', 'format', 'difficulty', 'time']
    search_fields = ['name', 'tags', 'difficulty', 'format']
    list_per_page = 10

admin.site.register(DjangoHub, DjangoHubAdmin)
admin.site.register(NameOfTutorial)