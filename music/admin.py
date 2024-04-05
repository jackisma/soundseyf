from django.contrib import admin
from .models import * 



class MasterPiecesAdmin(admin.ModelAdmin):
    list_display = ('song_id','name','Composer')
    list_filter = ('Composer',)
    empty_value_display = "-empty-"
    search_fields = ('name','Composer')
    save_as = True 
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'


admin.site.register(MasterPieces,MasterPiecesAdmin)