from django.contrib import admin
from .models import Corretor
# Register your models here.
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Corretor,CorretorAdmin)
