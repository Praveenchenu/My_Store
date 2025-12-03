from rest_framework.renderers import JSONRenderer

class CustomJsonRender(JSONRenderer):
    charset = 'utf-8'

    def render(self,data,accepted_media_type=None, renderer_content=None):
        response = {
            'status':'success',
            'data':data
        }
        return super().render(response,accepted_media_type,renderer_content)
    



