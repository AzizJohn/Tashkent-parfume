from rest_framework.generics import CreateAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.product.api_endpoints.Review.ReviewCreate.serializers import ReviewCreateSerializer
from apps.product.models import Review


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    parser_classes = [FormParser, MultiPartParser]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


__all__ = ["ReviewCreateAPIView"]