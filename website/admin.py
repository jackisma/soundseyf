from django.contrib import admin
from .models import * 


# Registering and Showing the Post view in ORM admin panel  
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_on"
    empty_value_display = "-empty-"
    list_display = ("name","email","subject","created_on")
    list_filter = ("subject",)
    search_fields = ["name","subject" ,"email"]
    summernote_fields = ('message',)
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
