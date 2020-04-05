from .models import Testimony, PrayerRequest

class CustomMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.testimony_count = Testimony.objects.filter(viewed=False).count()
        request.request_count = PrayerRequest.objects.filter(viewed=False).count()
        return self.get_response(request)