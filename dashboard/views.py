from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse 
from .models import (   Preaching,
                        Video,
                        Material,
                        DailyDevotion,
                        Testimony,
                        Notification,
                        PrayerRequest,)

from . forms import DevotionForm, VideoForm

def index(request):
    users = Profil.objects.filter(is_active=True, church=request.user.profile.church)
    preachings  = Preaching.objects.filter(church=request.user.profile.church)
    videos      = Video.objects.filter(church=request.user.profile.church)
    materials      = Material.objects.filter(church=request.user.profile.church)
    testimonies = Testimony.objects.filter(user__profile__church=request.user.profile.church).order_by("-id")[:5]
    prayer_requests = PrayerRequest.objects.filter(user__profile__church=request.user.profile.church).order_by("-id")[:5]
    devotion = DailyDevotion.objects.filter(church=request.user.profile.church).last()

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
    new_requests = PrayerRequest.objects.filter(viewed=False, user__profile__church=request.user.profile.church)
    old_requests = PrayerRequest.objects.filter(viewed=True, user__profile__church=request.user.profile.church)

    context = {
        "new_requests":new_requests,
        "old_requests":old_requests,
    }
    template = "dashboard/prayer_request.html"
    return render(request, template, context)

def view_request(request, pk):
    PrayerRequest.objects.filter(pk=pk).update(viewed=True)
    return JsonResponse({"success":True})

def testimonies(request):
    new_testimonies = Testimony.objects.filter(viewed=False, user__profile__church=request.user.profile.church)
    old_testimonies = Testimony.objects.filter(viewed=True, user__profile__church=request.user.profile.church)

    context = {
        "new_testimonies":new_testimonies,
        "old_testimonies":old_testimonies,
    }
    template = "dashboard/testimonies.html"
    return render(request, template, context)

def view_testimony(request, pk):
    Testimony.objects.filter(pk=pk).update(viewed=True)
    return JsonResponse({"success":True})

def devotion(request):
    form_class = DevotionForm
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            devotion = form.save(commit=False)
            devotion.church = request.user.profile.church
            devotion.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Devotion Submitted"
            return redirect("dashboard:devotion")

    template = "dashboard/devotion.html"
    context = {
        "form":form, 
        "devotions":DailyDevotion.objects.filter(church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)

def edit_devotion(request, pk):
    form_class = DevotionForm
    devotion = get_object_or_404(DailyDevotion, pk=pk)
    if request.method == "GET":
        form = form_class(instance = devotion)

    elif request.method == "POST":
        form = form_class(request.POST, request.FILES, instance = devotion)
        if form.is_valid():
            devotion.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Devotion Updated"
            return redirect("dashboard:devotion")
    
    context = {
        "form":form,
        "devotion":devotion,
    }
    template = "dashboard/edit_devotion.html"
    return render(request, template, context)

def daily_devotion(request):
    pk = request.GET.get("pk")
    if pk:
        devotion = get_object_or_404(DailyDevotion, pk=pk)
    else:
        devotion = DailyDevotion.objects.filter(church=request.user.profile.church).last()

    template = "dashboard/devotion_preview.html"
    context = {
        "devotion": devotion
    }   
    return render(request, template, context)

def video(request):
    form_class = VideoForm
    template = "dashboard/video.html"
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.church = request.user.profile.church
            video.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Video Added"
            return redirect("dashboard:video")

    context = {
        "form":form, 
        "videos":Video.objects.filter(church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)

def edit_video(request, pk):
    form_class = VideoForm
    video = get_object_or_404(Video, pk=pk)
    if request.method == "GET":
        form = form_class(instance = video)

    elif request.method == "POST":
        form = form_class(request.POST, request.FILES, instance = video)
        if form.is_valid():            
            video.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Video Updated"
            return redirect("dashboard:video")
    
    context = {
        "form":form,
        "video":video,
    }
    template = "dashboard/edit_video.html"
    return render(request, template, context)