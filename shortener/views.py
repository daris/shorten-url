from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect

from .utils import generate_short_id
from .models import URL
from .serializers import URLSerializer


class ShortenURLView(APIView):
    def post(self, request):
        original_url = request.data.get('url')
        if not original_url:
            return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Return existing if already stored
        existing = URL.objects.filter(original_url=original_url).first()
        if existing:
            serializer = URLSerializer(existing, context={'request': request})
            return Response(serializer.data)

        url = URL.objects.create(original_url=original_url, short_id=generate_short_id())
        serializer = URLSerializer(url, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RedirectView(APIView):
    def get(self, request, short_id):
        url = get_object_or_404(URL, short_id=short_id)
        return redirect(url.original_url)