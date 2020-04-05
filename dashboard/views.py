from django.shortcuts import render
from django.contrib.auth.models import User
from .models import (   Preaching,
                        Video,
                        Material,
                        DailyDevotion,
                        Testimony,
                        PrayerRequest,)
def index(request):
    users = User.objects.filter(is_active=True)
    preachings  = Preaching.objects.filter()
    videos      = Video.objects.filter()
    materials      = Material.objects.filter()
    testimonies = Testimony.objects.all().order_by("-id")[:5]
    prayer_requests = PrayerRequest.objects.all().order_by("-id")[:5]
    devotion = DailyDevotion.objects.last()

    users_count = users.count()
    preachings_count = preachings.count()
    videos_count = videos.count()
    materials_count = materials.count()

    template = "dashboard/index.html"
    context = {
        "users_count":users_count,
        "preachings_count":preachings_count,
        "videos_count":videos_count,
        "materials_count":materials_count,
        "testimonies":testimonies,
        "prayer_requests":prayer_requests,
        "devotion":devotion,
    }
    return render(request, template, context)