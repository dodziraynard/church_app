from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView      
from account.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from knox.models import AuthToken
from rest_framework.viewsets import ModelViewSet     
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from dashboard.models import (
        Leader,
        Church,
        DailyDevotion,
        Notification,
        Audio,
        Video,
        Material,
        Photo,
        Feedback,
    )

from . serializers import (
        LeaderSerializer,
        ChurchSerializer,
        DailyDevotionSerializer,
        NotificationSerializer,
        VideoSerializer,
        MaterialSerializer,
        AudioSerializer,
        PhotoSerializer,
        TestimonySerializer,
        PrayerRequestSerializer,
        FeedbackSerializer
    )

from account.models import (
    Profile
)
from account.serializers import (
        UserSerializer,
        RegisterSerializer,
        LoginSerializer,
        ProfileSerializer,
)

class LeadersAPI(APIView):
    serializer_class    = LeaderSerializer

    def get(self, request, *args, **kwargs):
        leaders = Leader.objects.filter(church=request.user.profile.church, inactive=None).order_by("-id")
        data = self.serializer_class(leaders, many=True).data
        return Response({"leaders": data})
    
class VideosAPI(APIView):
    serializer_class    = VideoSerializer

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query")
        videos = Video.objects.filter(church=request.user.profile.church).order_by("-id")
        if query:
            videos = videos.filter(
                Q(title__icontains=query) |
                Q(desc__icontains=query)
            )
        data = self.serializer_class(videos, many=True).data
        return Response({"videos": data})


class ChurchAPI(APIView):
    serializer_class    = ChurchSerializer

    def get_queryset(self):
        return Church.objects.first()


class NotificationsAPI(APIView):
    serializer_class    = NotificationSerializer

    def get(self, request, *args, **kwargs):
        date_five_days_ago = datetime.now() - timedelta(days=5)
        notifications = Notification.objects.filter(church=request.user.profile.church,
                                        date__gte=date_five_days_ago
                                        ).order_by("-id")
        data = self.serializer_class(notifications, many=True).data
        return Response({"notifications": data})

class MaterialsAPI(APIView):
    serializer_class    = MaterialSerializer

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query")
        materials = Material.objects.filter(church=request.user.profile.church).order_by("-id")
        if query:
            materials = materials.filter(
                Q(title__icontains=query) |
                Q(desc__icontains=query)
            )
        data = self.serializer_class(materials, many=True).data
        return Response({"materials": data})

class AudiosAPI(APIView):
    serializer_class    = AudioSerializer

    def get(self, request):
        query = request.GET.get("query")
        audios = Audio.objects.filter(church=request.user.profile.church).order_by("-id")
        if query:
            audios = audios.filter(
                Q(title__icontains=query) |
                Q(desc__icontains=query)
            )
        data = self.serializer_class(audios, many=True).data
        return Response({"audios": data})

class DevotionsAPI(APIView):
    serializer_class    = DailyDevotionSerializer

    def get(self, request, *args, **kwargs):
        d = DailyDevotion.objects.filter(church=request.user.profile.church).order_by("-id").first()
        devotions = DailyDevotion.objects.filter(id=d.id)
        data = self.serializer_class(devotions, many=True).data
        return Response({"devotions": data})

class PhotosAPI(APIView):
    serializer_class    = PhotoSerializer

    def get(self, request):
        photos = Photo.objects.filter(church=request.user.profile.church).order_by("-id")
        data = self.serializer_class(photos, many=True).data
        return Response({"photos": data})

class TestimonyAPI(ModelViewSet):
    serializer_class = TestimonySerializer

    def get_queryset(self):
        return self.request.user.testimonies
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PrayerRequestAPI(ModelViewSet):
    serializer_class = PrayerRequestSerializer

    def get_queryset(self):
        return self.request.user.prayer_requests
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedbackAPI(ModelViewSet):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.all()
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)

# USERS
# Register API
class RegisterAPI(generics.GenericAPIView):
    """
    User registration endpoint
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        church_id = request.POST.get("church_id")
        full_name = request.POST.get("full_name")
        mobile = request.POST.get("mobile")

        profile = user.profile
        profile.church_id = church_id
        profile.full_name = full_name
        profile.mobile = mobile
        profile.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(generics.GenericAPIView):
    """
    User login endpoint
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Get User API
class UserAPI(APIView):
    """
    User endpoint to retrieve and update an authenticated user.
    """
    def get(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response({"user": data})

    def patch(self, request, *args, **kwargs):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        username = request.data.get("username")
        email = request.data.get("email")

        if email:
            user.email = email
        if username:
            user.username = username
        user.save()  

        if new_password and old_password:
            if user.check_password(old_password):
                user.set_password(new_password)
            
            else:
                errors = {"detail": "Invalid Old Password"}
                return Response(errors, status=status.HTTP_403_FORBIDDEN)

        data = UserSerializer(user).data
        return Response({"user": data})

# UserProfile API
class UserProfileAPI(APIView):
    """
    API endpoint by which an authenticated user can view his/her profile
    """
    serializer_class = ProfileSerializer         

    def get(self, request):
        data = self.serializer_class(request.user.profile).data
        return Response({"profile": [data]})
    
    def post(self, request, *args, **kwargs):
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")

        # update user's info
        profile  = request.user.profile
        profile.full_name = full_name
        profile.mobile = mobile
        profile.save()

        # Update user's email
        request.user.email = email
        request.user.save()

        data = self.serializer_class(request.user.profile).data
        return Response({"profile": [data]})