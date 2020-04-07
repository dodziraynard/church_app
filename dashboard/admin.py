from django.contrib import admin
from . models import (
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
    Feedback,
)

admin.site.register(Leader)
admin.site.register(Church)
admin.site.register(DailyDevotion)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Material)
admin.site.register(Photo)
admin.site.register(Notification)
admin.site.register(Testimony)
admin.site.register(PrayerRequest)
admin.site.register(Feedback)
