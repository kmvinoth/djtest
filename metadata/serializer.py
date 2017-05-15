from rest_framework import serializers
from .models import MetadataAttributes, Value, Project, Deposit, DepositValue, DataObject, DataObjectValue


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('project_name',)


class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit
        fields = ('deposit_name',)


class DataObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataObject
        fields = ('data_object_name',)


class MetaDataAttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetadataAttributes
        fields = ('label', 'key', 'type', 'meta_data_type', 'meta_data_level')


class ValueSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()
    md_attributes = MetaDataAttributesSerializer()

    class Meta:
        model = Value
        fields = ('project', 'md_attributes', 'val')


class DepositValueSerializer(serializers.ModelSerializer):

    deposit = DepositSerializer()
    md_attributes = MetaDataAttributesSerializer()

    class Meta:
        model = DepositValue
        fields = ('deposit', 'md_attributes', 'val')


class DataObjectValueSerializer(serializers.ModelSerializer):

    dataobject = DataObjectSerializer()
    md_attributes = MetaDataAttributesSerializer()

    class Meta:
        model = DataObjectValue
        fields = ('dataobject', 'md_attributes', 'val')

