from rest_framework import serializers
from .models import User, ConnectionRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'avatar', 'connections', 'connections_count', 'people_you_may_know', 'job_list_count', 'is_active', 'is_superuser', 'is_staff', 'date_joined', 'last_login']
        read_only_fields = ['date_joined', 'last_login']

class ConnectionRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = ConnectionRequest
        fields = ['id', 'sender', 'receiver', 'status', 'created_at']
        read_only_fields = ['created_at']
