from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse 
from .models import (   Audio,
                        Video,
                        Material,
                        DailyDevotion,
                        Testimony,
                        Leader,
                        Material,
                        Notification,
                        PrayerRequest)

from . forms import DevotionForm, VideoForm, MaterialForm, AudioForm, LeaderForm, ChurchForm
from account.models import Profile

def index(request):
    users = Profile.objects.filter(user__is_active=True, church=request.user.profile.church)
    preachings  = Audio.objects.filter(church=request.user.profile.church)
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
    church = request.GET.get("church")
    if pk:
        devotion = get_object_or_404(DailyDevotion, pk=pk)
    elif church:
        devotion = DailyDevotion.objects.filter(church_id=church).last()
    else:
        devotion = DailyDevotion.objects.last()

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

def library(request):
    form_class = MaterialForm
    template = "dashboard/library.html"
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.church = request.user.profile.church
            material.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Material Added"
            return redirect("dashboard:library")
    context = {
        "form":form, 
        "materials":Material.objects.filter(church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)

def edit_material(request, pk):
    form_class = MaterialForm
    material = get_object_or_404(Material, pk=pk)
    if request.method == "GET":
        form = form_class(instance = material)

    elif request.method == "POST":
        form = form_class(request.POST, request.FILES, instance = material)
        if form.is_valid():            
            form.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Book Updated"
            return redirect("dashboard:library")
    
    context = {
        "form":form,
        "material":material,
    }
    template = "dashboard/edit_library.html"
    return render(request, template, context)

def audio(request):
    form_class = AudioForm
    template = "dashboard/audio.html"
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.church = request.user.profile.church
            audio.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Material Added"
            return redirect("dashboard:audio")

    context = {
        "form":form, 
        "audios":Audio.objects.filter(church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)

def edit_audio(request, pk):
    form_class = AudioForm
    audio = get_object_or_404(Audio, pk=pk)
    if request.method == "GET":
        form = form_class(instance = audio)

    elif request.method == "POST":
        form = form_class(request.POST, request.FILES, instance = audio)
        if form.is_valid():            
            form.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Audio Updated"
            return redirect("dashboard:audio")
    
    context = {
        "form":form,
        "audio":audio,
    }
    template = "dashboard/edit_audio.html"
    return render(request, template, context)

def leader(request):
    form_class = LeaderForm
    template = "dashboard/leader.html"
    form = form_class()
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            leader = form.save(commit=False)
            leader.church = request.user.profile.church
            leader.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Leader Added"
            return redirect("dashboard:leader")

    context = {
        "form":form, 
        "leaders":Leader.objects.filter(church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)

def edit_leader(request, pk):
    form_class = LeaderForm
    leader = get_object_or_404(Leader, pk=pk)
    if request.method == "GET":
        form = form_class(instance = leader)

    elif request.method == "POST":
        form = form_class(request.POST, instance = leader)
        if form.is_valid():            
            form.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Leader Updated"
            return redirect("dashboard:leader")
    
    context = {
        "form":form,
        "leader":leader,
    }
    template = "dashboard/edit_leader.html"
    return render(request, template, context)

def church_info(request):
    form_class = ChurchForm
    church = request.user.profile.church
    if request.method == "GET":
        form = form_class(instance = church)

    elif request.method == "POST":
        form = form_class(request.POST, instance = church)
        if form.is_valid():            
            form.save()
            request.session["message_type"] = "success"
            request.session["message"] = "Church Info Updated"
            return redirect("dashboard:church_info")
    
    context = {
        "form":form,
        "church":church,
    }
    template = "dashboard/church_info.html"
    return render(request, template, context)

def sms(request):
    template = "dashboard/sms.html"
    return render(request, template)

def testimony_list(request):
    template = "dashboard/testimony_list.html"

    context = {
        "testimonies":Testimony.objects.filter(user__profile__church=request.user.profile.church).order_by("-id")
    }
    return render(request, template, context)