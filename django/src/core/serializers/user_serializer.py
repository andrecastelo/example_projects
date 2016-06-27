from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=250)
    username = serializers.CharField(required=True, allow_blank=False, max_length=30)
    email = serializers.CharField(required=True, allow_blank=False, max_length=128)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    website = serializers.CharField(max_length=128)
    active = serializers.BooleanField(default=False)
    # country = CountryField(blank=True)

    def create(self, validated_data):
        """
        Create and return a new 'User' instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'User' instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get('description', instance.description)
        instance.website = validated_data.get('website', instance.website)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance
