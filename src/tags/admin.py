from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin

from .models import TaggedItem

class TaggedItemInLine(GenericTabularInline): #admin.TabularInLine
     model = TaggedItem
     extra = 0

class TaggedItemAdmin(admin.ModelAdmin):
    
    fields = ['tag', 'content_type', 'object_id', 'content_object']
    readonly_fields = ['content_object']
    class Meta:
         model = TaggedItem
         list_display = ['title']

admin.site.register(TaggedItem, TaggedItemAdmin)