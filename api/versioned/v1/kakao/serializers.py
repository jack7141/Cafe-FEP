from api.versioned.v1.kakao.adapter import kakao_openapi_adapter


class AdapterMixin(object):
    adapter = kakao_openapi_adapter
    response_serializer_class = None
    base_url = None
    endpoint = ''
    kwargs = {}

    def to_representation(self, instance):
        if self.adapter:
            response = self.get_adapter_response(endpoint=self.endpoint, body=instance)
            serializer = self.response_serializer_class(response)
        return serializer.data

    def get_adapter_response(self, endpoint, body):
        response = self.adapter.request(additional_url=endpoint,
                                        body=body,
                                        **self.kwargs)
        return response