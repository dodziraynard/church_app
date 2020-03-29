from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView      

from dashboard.models import (
        Leader,
        ChurchInfo,
        DailyDevotion,
        Notification,
        Preaching,
        Video,
        Material,
        Photo,
    )

from . serializers import (
        LeaderSerializer,
        ChurchInfoSerializer,
        DailyDevotionSerializer,
        NotificationSerializer,
        ProfileSerializer,
        VideoSerializer,
        MaterialSerializer,
        PreachingSerializer,
        PhotoSerializer,
    )

class LeadersAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = LeaderSerializer

    def get_queryset(self):
        return Leader.objects.filter(inactive=None)
    
class VideosAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = VideoSerializer

    def get_queryset(self):
        return Video.objects.all().order_by("-id")

class ChurchInfoAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = ChurchInfoSerializer

    def get_queryset(self):
        return ChurchInfo.objects.first()

class DailyDevotionsAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = DailyDevotionSerializer

    def get_queryset(self):
        return DailyDevotion.objects.all().order_by("-id")

class NotificationsAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.all().order_by("-id")

# class ProfileAPI(generics.RetriveAPIView):
#     serializer_class    = ProfileSerializer

#     def get_queryset(self):
#         return self.request.user.profile

class MaterialsAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = MaterialSerializer

    def get_queryset(self):
        return Material.objects.all().order_by("-id")

class PreachingsAPI(APIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = PreachingSerializer

    def get(self, request):
        preachings = Preaching.objects.all().order_by("-id")
        data = self.serializer_class(preachings, many=True).data
        return Response({"preachings": data})

class DevotionsAPI(APIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = DailyDevotionSerializer

    def post(self, request, *args, **kwargs):
        previous_id = request.POST.get("previous_id")
        if previous_id:
            d = DailyDevotion.objects.filter(id__gt=previous_id).order_by("-id").first()
            if d:
                devotions = DailyDevotion.objects.filter(id=d.id)
            else:
                d = DailyDevotion.objects.all().order_by("-id").first()
        else:
            d = DailyDevotion.objects.all().order_by("-id").first()
        
        devotions = DailyDevotion.objects.filter(id=d.id)
        data = self.serializer_class(devotions, many=True).data
        return Response({"devotions": data})


class PhotosAPI(generics.ListAPIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.all().order_by("-id")