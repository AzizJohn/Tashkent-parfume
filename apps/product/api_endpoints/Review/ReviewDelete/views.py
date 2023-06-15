from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.generics import DestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from apps.product.models import Review
from apps.product.permissions import ReviewUserOrReadOnly


class ReviewDeleteAPIView(DestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    parser_classes = [FormParser, MultiPartParser]

    def destroy(self, request, *args, **kwargs):
        try:
            product = Review.objects.get(user=self.request.user, product=self.kwargs['product_id'])
            product.delete()
            return Response({"status": 204, "message": "Review deleted from product."})
        except ObjectDoesNotExist:
            raise Http404("Product not found")


__all__ = ["ReviewDeleteAPIView"]
