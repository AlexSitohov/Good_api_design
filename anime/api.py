from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.viewsets import *
from rest_framework.permissions import *

from anime.models import *
from .pagination import AnimeAPIListPagination
from .serializeres import *
from rest_framework.generics import *


# class GETAnimeAPIViewSet(ListAPIView):
#     queryset = Anime.objects.all().order_by('-id')
#     serializer_class = GETAnimeSerializer


class GETAnimeAPIViewSet(APIView):
    def get(self, request):
        anime = Anime.objects.all().order_by('-id')
        serializer = GETAnimeSerializer(anime, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        serializer = GETAnimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)


class ONEGETAnimeAPIViewSet(APIView):
    def get(self, request, pk, *args, **kwargs):
        anime = Anime.objects.get(pk=pk)
        serializer = GETAnimeSerializer(anime)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        anime = Anime.objects.get(pk=pk)
        data = self.request.data
        serializer = GETAnimeSerializer(data=data)
        if serializer.is_valid():
            data_serializer = serializer.data
            anime.title = data_serializer.get('title')
            anime.save()
            anime_serializer = GETAnimeSerializer(anime)

            return Response(anime_serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        anime = Anime.objects.get(pk=pk)
        anime.delete()
        return Response({'!!!': 'Анимешка удалена'})


class CreateAnimeAPIViewSet(ModelViewSet):
    queryset = Anime.objects.all().order_by('-id')
    serializer_class = CreateAnimeSerializer
    pagination_class = AnimeAPIListPagination
    permission_classes = [IsAdminUser]


class StudioAPIViewSet(ModelViewSet):
    queryset = Studio.objects.all().order_by('-id')
    serializer_class = StudioSerializer


class LikeAPI(APIView):
    def get(self, request):
        anime = Anime.objects.all().order_by('-id')
        serializer = GETAnimeSerializer(anime, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = self.request.data
        pk = data.get('who_like_pk')
        count = data.get('count')
        anime = Anime.objects.get(pk=pk)
        anime.rating += count
        anime.save()
        anime_serializer = GETAnimeSerializer(anime)

        return Response(anime_serializer.data)
