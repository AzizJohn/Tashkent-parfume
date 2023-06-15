from hashlib import sha256

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class DeleteProfile(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ["delete"]

    def delete(self, request):
        user = request.user
        user.prepare_to_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["DeleteProfile"]
