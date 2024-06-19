from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class HelloView(ListAPIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get("name")
        message = request.GET.get("message")
        return Response(f'Hello {name}!, {message}!')
