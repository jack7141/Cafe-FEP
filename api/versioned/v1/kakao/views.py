from rest_framework import viewsets, permissions, response
from rest_framework.settings import api_settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.versioned.v1.kakao import input_serializers
from api.versioned.v1.kakao.serializers import AdapterMixin
from common.viewsets import RetrieveModelMixin, MappingViewSetMixin


class CafeBaseViewSet(MappingViewSetMixin,
                      viewsets.GenericViewSet,
                      ):
    permission_classes = [permissions.AllowAny]
    # filter_backends = (filters.DjangoFilterBackend,)
    filter_class = None
    serializer_class = None

    def get_queryset(self):
        return None

class KAKAOCafeViewSet(RetrieveModelMixin, CafeBaseViewSet):
    """
    account_base: 입출금 원금 조회

    해외 거래내역을 조회하여 시작날짜부터 현재까지의 입출금 원금을 계산합니다.
    """

    filter_class = None
    serializer_class = input_serializers.CafeListReqSerializer

    def cafe_list(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

