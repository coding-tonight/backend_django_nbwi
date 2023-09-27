from rest_framework import serializers
from factory.models import Factory, FactoryOwner


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['id', 'factory_name', 'factory_address', 'phone_number',
                  'created_at', 'created_by', 'updated_at', 'updated_by']


class FactoryOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryOwner
        fields = ['id', 'owner_name', 'address', 'phone_number', 'factory_id',
                  'created_at', 'created_by', 'updated_at', 'updated_by']
