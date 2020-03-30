from django.contrib import admin
from . models import (
    Leader,
    Church,
    DailyDevotion,
    Notification,
    Preaching,
    Video,
    Material,
    Photo
)

admin.site.register(Leader)
admin.site.register(Church)
admin.site.register(DailyDevotion)
admin.site.register(Preaching)
admin.site.register(Video)
admin.site.register(Material)
admin.site.register(Photo)
admin.site.register(Notification)
