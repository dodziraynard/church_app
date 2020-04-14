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

    path("library", views.library, name="library"),
    path("edit_material/<int:pk>", views.edit_material, name="edit_material"),

    path("audio", views.audio, name="audio"),
    path("edit_audio/<int:pk>", views.edit_audio, name="edit_audio"),
    
    path("leader", views.leader, name="leader"),
    path("edit_leader/<int:pk>", views.edit_leader, name="edit_leader"),

    path("church_info", views.church_info, name="church_info"),
    path("sms", views.sms, name="sms"),
    path("testimony_list", views.testimony_list, name="testimony_list"),
    
    path("delete_video/<int:pk>", views.delete_video, name="delete_video"),
    path("delete_audio/<int:pk>", views.delete_audio, name="delete_audio"),
    path("delete_material/<int:pk>", views.delete_material, name="delete_material"),
    path("delete_leader/<int:pk>", views.delete_leader, name="delete_leader"),

    path("transaction", views.transaction, name="transaction"),
    path("donation", views.donation, name="donation"),
]
