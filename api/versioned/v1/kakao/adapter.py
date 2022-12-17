from urllib.parse import urljoin

from api.bases.kakao.base import APIRequest
from api_backend import settings
from common.designpatterns import dotdict, SingletonClass

__all__ = ["kakao_openapi_adapter", "kakao_settings"]
kakao_settings = dotdict(settings.KAKAO_CLIENT)

class KakaoAdapterClass(SingletonClass):
    __base = kakao_settings.KAKAO_BASE_URL
    __token = kakao_settings.KAKAO_API_TOKEN

    def request(self, additional_url=None, body=None, headers=None, method='GET', timeout=None):
        requester = APIRequest(url=urljoin(self.__base, additional_url), headers=headers, body=body)
        requester.update_headers({"Authorization": f"KakaoAK {self.__token}"})
        response = requester.send(method=method)
        return response


kakao_openapi_adapter = KakaoAdapterClass.instance()