from django.urls import path, include   
from rest_framework import routers                  
from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register("testimonies", views.TestimonyAPI, 'testimonies')
router.register("prayer-requests", views.PrayerRequestAPI, 'prayer_request')
router.register("feedback", views.FeedbackAPI, 'feedback')

urlpatterns = [
    path('', include(router.urls)),
    path("leaders", views.LeadersAPI.as_view()),
    path("videos", views.VideosAPI.as_view()),
    path("church", views.ChurchAPI.as_view()),
    path("devotion", views.DevotionsAPI.as_view(),  name="devotions"),
    path("notifications", views.NotificationsAPI.as_view()),
    path("materials", views.MaterialsAPI.as_view()),
    path("audios", views.AudiosAPI.as_view(), name="audios"),
    path("photos", views.PhotosAPI.as_view()),
    path("profile", views.UserProfileAPI.as_view()),

    # users
    path('auth/register', views.RegisterAPI.as_view()),
    path('auth/login', views.LoginAPI.as_view()),
    path('auth/user', views.UserAPI.as_view()),
]