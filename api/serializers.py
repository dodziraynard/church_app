from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
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
from account.models import Profile

class LeaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leader
        fields = "__all__"
    
class ChurchInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChurchInfo
        fields = "__all__"

class DailyDevotionSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="get_image_url", read_only=True)
    class Meta:
        model = DailyDevotion
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"
    
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="get_image_url", read_only=True)
    class Meta:
        model = Material
        fields = "__all__"
    
class PreachingSerializer(serializers.ModelSerializer):
    file = serializers.URLField(source="get_file_url", read_only=True)
    image = serializers.URLField(source="get_image_url", read_only=True)

    class Meta:
        model = Preaching
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = "__all__"