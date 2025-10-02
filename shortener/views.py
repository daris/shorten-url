from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class ShortenURLView(APIView):
    def post(self, request: Request) -> Response:
        return Response()


class RedirectView(APIView):
    def get(self, request: Request, short_id: str) -> Response:
        return Response()
