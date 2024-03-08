from django.conf import settings
from django.core.exceptions import PermissionDenied

class BlockIPSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(settings, 'BLOCKED_IPS') and settings.BLOCKED_IPS is not None:
            if request.META['REMOTE_ADDR'] in settings.BLOCKED_IPS:
                print("Middleware Called \t IPS is Blocked")
                raise PermissionDenied()

        response = self.get_response(request)
        return response