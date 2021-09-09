from django.contrib import admin
# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import Listagen
class ListagensAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','publicado','preco','hectares','Corretor')
    list_display_links = ('id', 'titulo')
    list_editable = ('publicado',)
    search_fields = ('titulo','descricao','publicado','preco','hectares')
    list_per_page = 25

admin.site.register(Listagen, ListagensAdmin)

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


