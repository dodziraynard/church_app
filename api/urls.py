from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("leaders", views.LeadersAPI.as_view()),
    path("videos", views.VideosAPI.as_view()),
    path("church", views.ChurchAPI.as_view()),
    path("devotion", views.DevotionsAPI.as_view(),  name="devotions"),
    path("notifications", views.NotificationsAPI.as_view()),
    path("materials", views.MaterialsAPI.as_view()),
    path("preachings", views.PreachingsAPI.as_view(), name="preachings"),
    path("photos", views.PhotosAPI.as_view()),
    path("profile", views.UserProfileAPI.as_view()),

    # users
    path('auth/register', views.RegisterAPI.as_view()),
    path('auth/login', views.LoginAPI.as_view()),
    path('auth/user', views.UserAPI.as_view()),
]









