from rest_framework import routers
from .api import PlayerViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('api/accounts', PlayerViewSet, 'players')
urlpatterns = router.urls + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
