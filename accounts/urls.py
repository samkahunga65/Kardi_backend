from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, PlayerViewSet
from knox import views as knox_views
from . import views
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
    # to add friend at last slash {firend to add} {my id}
    path('addfrnd/<str:famid>', views.user, name='addfriend'),
    path('rmfrnd/<str:famid>', views.userRemove, name='removefriend'),
    path('addgld/<str:magld>', views.addGold, name='add gold'),
    path('rmgld/<str:magld>', views.rmGold, name='remove gold'),
    path('addchips/<str:magld>', views.addChips, name='add chips'),
    path('rmchips/<str:magld>', views.rmChips, name='remove chips'),
    path('uap/<int:id>', views.userAndPlayer, name='user and player'),
    path('findfriends/<str:ids>', views.findFriends, name='findFriends'),
]

urlpatterns = urlpattern + router.urls + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
