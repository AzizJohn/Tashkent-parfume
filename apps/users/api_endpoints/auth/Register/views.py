# from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.users.models import User

from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            return Response({"message": "User registered successfully."}, status=201)
        else:
            return response


__all__ = ["RegisterView"]
