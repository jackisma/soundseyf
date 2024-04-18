from django.contrib import admin
from .models import * 


# Showing Pieces Table in ORM admin panel 
class MasterPiecesAdmin(admin.ModelAdmin):
    list_display = ('song_id','name','composer')
    list_filter = ('composer', 'tags')
    empty_value_display = "-empty-"
    search_fields = ('name','composer')
    save_as = True 
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'



# Showing Pieces Table in ORM admin panel 
class ComposersAdmin(admin.ModelAdmin):
    list_display = ('name','nationality')
    list_filter = ('name','genre')
    empty_value_display = "-empty-"
    search_fields = ('name',)
    save_as = True 
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'


class FavoriteComposerAdmin(admin.ModelAdmin):
    list_display = ('user','composer')
    list_filter = ('user',)
    empty_value_display = "-empty-"
    search_fields = ('user',)
    save_as = True 
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'



admin.site.register(MasterPiece,MasterPiecesAdmin)
admin.site.register(Composer,ComposersAdmin)
admin.site.register(FavoriteComposer,FavoriteComposerAdmin)