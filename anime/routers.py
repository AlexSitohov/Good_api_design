from rest_framework.routers import *

from anime.api import *

router = DefaultRouter()
router.register('anime', CreateAnimeAPIViewSet)
router.register('studio', StudioAPIViewSet)

urlpatterns = router.urls
