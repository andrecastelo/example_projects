from rest_framework import serializers
from core.models import Tweet

class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'content', 'mentions', 'created_at', 'updated_at')