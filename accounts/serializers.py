from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        profile = Profile.objects.create_user(password=password, **validated_data)
        return profile