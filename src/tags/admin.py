from django.contrib import admin

from .models import TaggedItem

class TaggedItemAdmin(admin.ModelAdmin):
    
    fields = ['tag', 'content_type', 'object_id', 'content_object']
    readonly_fields = ['content_object']
    class Meta:
         model = TaggedItem
         list_display = ['title']

admin.site.register(TaggedItem, TaggedItemAdmin)