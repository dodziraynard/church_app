from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse 
from .models import (   Preaching,
                        Video,
                        Material,
                        DailyDevotion,
                        Testimony,
                        Notification,
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

def notifications(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")
        Notification.objects.create(title=title, message=message, church=request.user.profile.church)
        request.session["message_type"] = "success"
        request.session["message"] = "Notification sent to users"
        return redirect("dashboard:notifications")

    context = {
        "notifications":Notification.objects.all().order_by("-id")
    }
    template = "dashboard/notifications.html"
    return render(request, template, context)

def prayer_request(request):
    new_requests = PrayerRequest.objects.filter(viewed=False)
    old_requests = PrayerRequest.objects.filter(viewed=True)

    context = {
        "new_requests":new_requests,
        "old_requests":old_requests,
    }
    template = "dashboard/prayer_request.html"
    return render(request, template, context)

def view_request(request, pk):
    PrayerRequest.objects.filter(pk=pk).update(viewed=True)
    return JsonResponse({"success":True})