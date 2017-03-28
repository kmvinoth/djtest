from django.contrib import admin
from .models import MetadataAttributes, Value


class MetadataAttributesAdmin(admin.ModelAdmin):
    list_display = ['label', 'key', 'type']


class ValueAdmin(admin.ModelAdmin):
    list_display = ['project', 'md_attributes', 'val']


admin.site.register(MetadataAttributes, MetadataAttributesAdmin)
admin.site.register(Value, ValueAdmin)


