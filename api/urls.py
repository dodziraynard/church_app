from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("leaders", views.LeadersAPI.as_view()),
    path("videos", views.VideosAPI.as_view()),
    path("church-info", views.ChurchInfoAPI.as_view()),
    path("daily-devotion", views.DevotionsAPI.as_view(),  name="devotions"),
    path("notifications", views.NotificationsAPI.as_view()),
    path("materials", views.MaterialsAPI.as_view()),
    path("preachings", views.PreachingsAPI.as_view(), name="preachings"),
    path("photos", views.PhotosAPI.as_view()),
    # path("profile", views.ProfileAPI.as_view()),
]









