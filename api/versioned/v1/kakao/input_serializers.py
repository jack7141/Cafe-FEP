from rest_framework import serializers

from api.versioned.v1.kakao import output_serializers
from api.versioned.v1.kakao.serializers import AdapterMixin


class CafeListReqSerializer(AdapterMixin, serializers.Serializer):
    endpoint = "/v2/local/search/category.json"

    response_serializer_class = output_serializers.CafeListRespSerializer

    page = serializers.HiddenField(default=1,help_text='페이지')
    size = serializers.HiddenField(default=15, help_text='사이즈')
    sort = serializers.HiddenField(default='accuracy', help_text='분류')
    latitude = serializers.DecimalField(default=37.690235357826, max_digits=20, decimal_places=16, source="y", help_text='위도')
    longitude = serializers.DecimalField(default=126.71946531058, max_digits=20, decimal_places=16, source="x", help_text='경도')
    category_group_code = serializers.HiddenField(default="CE7", help_text='코드')