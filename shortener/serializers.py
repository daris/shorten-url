from rest_framework import serializers
from .models import URL


class URLInputSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = ['short_url']

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/{obj.short_id}")