from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from shortener.serializers import URLInputSerializer


class ShortenURLView(APIView):
    def post(self, request: Request) -> Response:
        input_serializer = URLInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class RedirectView(APIView):
    def get(self, request: Request, short_id: str) -> Response:
        return Response()
