from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from shortener.models import URL
from shortener.serializers import URLInputSerializer, URLSerializer
from shortener.utils import generate_unique_short_id


class ShortenURLView(APIView):
    def post(self, request: Request) -> Response:
        input_serializer = URLInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        original_url = input_serializer.validated_data['url']

        short_id = generate_unique_short_id()

        url = URL.objects.create(original_url=original_url, short_id=short_id)
        serializer = URLSerializer(url, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RedirectView(APIView):
    def get(self, request: Request, short_id: str) -> Response:
        return Response()
