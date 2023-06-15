from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.product.api_endpoints.Review.ReviewList.serializers import ReviewListSerializer
from apps.product.models import Review


class ReviewListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewListSerializer
    # queryset = Review.objects.all().order_by('-created_at')

    def get_queryset(self):
        my_review = Review.objects.filter(user=self.request.user)
        other_reviews = Review.objects.exclude(user=self.request.user).order_by('-created_at')
        return list(my_review) + list(other_reviews)

__all__ = ["ReviewListAPIView"]
