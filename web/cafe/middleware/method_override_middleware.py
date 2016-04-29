ALLOWED_HTTP_METHODS = ['GET', 'HEAD', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'PATCH']

PARAM_KEY = '_method'

HTTP_HEADER = 'HTTP_X_HTTP_METHOD_OVERRIDE'

class MethodOverrideMiddleware(object):
    def process_view(self, request, callback=None, callback_args=None, callback_kwargs=None):
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