from rest_framework import serializers

from .models import Host


class HostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Host
        exclude = ('users',)


class HostAdminSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Host
        fields = '__all__'
        extra_kwargs = {
            'users': {'required': False}
        }




