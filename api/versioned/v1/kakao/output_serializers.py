from django.conf import settings
from rest_framework import serializers

class CafeListRespSerializer(serializers.Serializer):
    class CafeListDataSerializer(serializers.Serializer):
        address_name = serializers.CharField(default='', help_text="주소")
        category_group_code = serializers.HiddenField(default='', help_text="카테고리 분류")
        category_group_name = serializers.HiddenField(default='', help_text="카테고리 이름")
        category_group_tree = serializers.HiddenField(default='', source="category_name", help_text="카테고리 이름")
        id = serializers.HiddenField(default='', help_text="id")
        distance = serializers.CharField(default='', help_text="거리")
        phone_number = serializers.CharField(default='', source="phone", help_text="전화 번호")
        cafe_name = serializers.CharField(default='', source="place_name", help_text="카페 이름")
        cafe_url = serializers.CharField(default='', source="place_url", help_text="카페 url")
        road_address_name = serializers.CharField(default='', help_text="길 주소")
        latitude = serializers.CharField(default='', source='y', help_text='위도')
        longitude = serializers.CharField(default='', source='x', help_text='경도')
    documents = CafeListDataSerializer(many=True)