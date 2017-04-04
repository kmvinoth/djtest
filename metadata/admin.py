from django.contrib import admin
from .models import MetadataAttributes, Value, DepositValue, DataObjectValue


class MetadataAttributesAdmin(admin.ModelAdmin):
    list_display = ['label', 'key', 'type', 'meta_data_type', 'meta_data_level']


class ValueAdmin(admin.ModelAdmin):
    list_display = ['project', 'md_attributes', 'val']


class DepositValueAdmin(admin.ModelAdmin):
    list_display = ['deposit', 'md_attributes', 'val']


class DataObjectValueAdmin(admin.ModelAdmin):
    list_display = ['dataobject', 'md_attributes', 'val']


admin.site.register(MetadataAttributes, MetadataAttributesAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(DepositValue, DepositValueAdmin)
admin.site.register(DataObjectValue, DataObjectValueAdmin)


