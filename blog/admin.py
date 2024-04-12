from django.contrib import admin
from .models import Post 
from django_summernote.admin import SummernoteModelAdmin

# Creating the actions use by Action Decorator Function Queryset method And Model Admin  
@admin.action(description="Mark selected Posts as Published")
def make_published(modeladmin , request, queryset):
    queryset.update(status="p")


# Registering and Showing the Post view in ORM admin panel  
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_on"
    empty_value_display = "-empty-"
    list_display = ("title","author","slug","status","created_on","counted_views","login_required")
    list_filter = ("status","author" ,"login_required")
    search_fields = ["author","title" , "content"]
    summernote_fields = ('content',)
    actions = [make_published]
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
