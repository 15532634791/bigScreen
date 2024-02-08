from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    """
    跨域中间件
    """
    def process_response(self, request, response):

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Methods"] = "GET, DELETE, PUT, POST"
        return response
