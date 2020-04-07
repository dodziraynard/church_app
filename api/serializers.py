from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from dashboard.models import (
            Leader,
            Church,
            DailyDevotion,
            Notification,
            Audio,
            Video,
            Material,
            Photo,
            Testimony,
            PrayerRequest,
            Feedback
        )
from account.models import Profile

class LeaderSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    image = serializers.URLField(source="get_image_url", read_only=True)
    
    class Meta:
        model = Leader
        fields = "__all__"
    
class ChurchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Church
        fields = "__all__"

class DailyDevotionSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="get_image_url", read_only=True)
    class Meta:
        model = DailyDevotion
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source="get_readable_date", read_only=True)
    
    class Meta:
        model = Notification
        fields = "__all__"
    
class VideoSerializer(serializers.ModelSerializer):
    file = serializers.URLField(source="get_file_url", read_only=True)
    image = serializers.URLField(source="get_image_url", read_only=True)
    date = serializers.CharField(source="get_readable_date", read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    file = serializers.URLField(source="get_file_url", read_only=True)
    image = serializers.URLField(source="get_image_url", read_only=True)
    date = serializers.CharField(source="get_readable_date", read_only=True)

    class Meta:
        model = Material
        fields = "__all__"
    
class AudioSerializer(serializers.ModelSerializer):
    file = serializers.URLField(source="get_file_url", read_only=True)
    image = serializers.URLField(source="get_image_url", read_only=True)
    date = serializers.CharField(source="get_readable_date", read_only=True)
    
    class Meta:
        model = Audio
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = "__all__"

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ["testimony"]

class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = ["request"]

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["feedback"]
