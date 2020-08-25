virtual_hosts = {
    "127.0.0.1:8000": "app.web.urls",
    "localhost:8000": "app.cucm.urls",
}


class VirtualHostMiddlewareClass(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # let's configure the root urlconf
        host = request.get_host()
        request.urlconf = virtual_hosts.get(host)
        # order matters!
        response = self.get_response(request)
        return response