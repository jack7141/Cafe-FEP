from django.urls import path
from .views import KAKAOCafeViewSet

urlpatterns = [
    path('cafes/', KAKAOCafeViewSet.as_view({'post': 'cafe_list'}))
]
