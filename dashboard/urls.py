from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("notifications", views.notifications, name="notifications"),
    path("prayer_request", views.prayer_request, name="prayer_request"),
    path("view_request/<int:pk>", views.view_request, name="view_request"),
]
