ALLOWED_HTTP_METHODS = ['GET', 'HEAD', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'PATCH']

PARAM_KEY = '_method'

HTTP_HEADER = 'HTTP_X_HTTP_METHOD_OVERRIDE'

INPUT_TEMPLATE = '<input type="hidden" name="{name}" value="{value}">'

class MethodOverrideMiddleware(object):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.method != 'POST':
            return
        method = self._get_method_override(request)
        if method in ALLOWED_HTTP_METHODS:
            setattr(request, method, request.POST.copy())
            request.method = method

    def _get_method_override(self, request):
        method = (request.POST.get(PARAM_KEY) or
                  request.META.get(HTTP_HEADER))
        return method and method.upper()