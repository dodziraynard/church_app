from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("notifications", views.notifications, name="notifications"),
    path("prayer_request", views.prayer_request, name="prayer_request"),
    path("view_request/<int:pk>", views.view_request, name="view_request"),
    
    path("testimonies", views.testimonies, name="testimonies"),
    path("view_testimony/<int:pk>", views.view_testimony, name="view_testimony"),

    path("devotion", views.devotion, name="devotion"),
    path("daily_devotion", views.daily_devotion, name="daily_devotion"),
    path("edit_devotion/<int:pk>", views.edit_devotion, name="edit_devotion"),

    path("video", views.video, name="video"),
    path("edit_video/<int:pk>", views.edit_video, name="edit_video"),
]