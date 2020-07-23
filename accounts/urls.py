from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, PlayerViewSet
from knox import views as knox_views

from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('api/player', PlayerViewSet, 'players')
urlpattern = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]

urlpatterns = urlpattern + router.urls + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
