from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import *

from anime.api import GETAnimeAPIViewSet, ONEInstanceAnimeAPIViewSet, LikeAPI, IDK
from config import settings
from anime.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('anime.routers')),
    path('api/anime_list_w_info/', GETAnimeAPIViewSet.as_view()),
    path('api/anime_list_w_info/<int:pk>/', ONEInstanceAnimeAPIViewSet.as_view()),
    path('api/like_anime/', LikeAPI.as_view()),
    path('api/idk/', IDK),

    path('api/auth/', include('djoser.urls')),  # new
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += doc_urls
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
