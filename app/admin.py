from django.contrib import admin
from .models import Hood,Business,User

# Register your models here.
class HoodAdmin(admin.ModelAdmin):
    list_display = ('name','location','count')
    list_display_links = ('name',)
    list_editable = ('count',)
    list_per_page = 10
    search_fields = ('name','location','count')
    list_filter = ('name','location')




admin.site.register(Hood,HoodAdmin)
admin.site.register(Business)
admin.site.register(User)