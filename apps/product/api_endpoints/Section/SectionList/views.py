from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Section.SectionList.serializers import SectionListSerializer
from apps.product.models import Section


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()


__all__ = ['SectionListAPIView']
