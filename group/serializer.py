from rest_framework import serializers
from group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name',
                  'created_at', 'created_by', 'updated_at', 'updated_by']
