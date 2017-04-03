from django.contrib import admin
from .models import MetadataAttributes, Value, DepositValue


class MetadataAttributesAdmin(admin.ModelAdmin):
    list_display = ['label', 'key', 'type']


class ValueAdmin(admin.ModelAdmin):
    list_display = ['project', 'md_attributes', 'val']


class DepositValueAdmin(admin.ModelAdmin):
    list_display = ['deposit', 'md_attributes', 'val']


admin.site.register(MetadataAttributes, MetadataAttributesAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(DepositValue, DepositValueAdmin)


