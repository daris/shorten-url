from rest_framework import serializers
from django.urls import reverse

from shortener.models import URL


class URLInputSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = ['short_url']

    def get_short_url(self, obj: URL) -> str:
        request = self.context.get('request')
        relative_url = reverse('redirect', kwargs={'short_id': obj.short_id})
        return request.build_absolute_uri(relative_url)
