import django_filters.rest_framework
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.viewsets import *
from rest_framework.permissions import *
from rest_framework.generics import *

from .models import *
from .pagination import *
from .serializeres import *


# class GETAnimeAPIViewSet(ListAPIView):
#     queryset = Anime.objects.all().order_by('-id')
#     serializer_class = GETAnimeSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


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


class ONEInstanceAnimeAPIViewSet(APIView):
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
            anime.description = data_serializer.get('description')
            anime.image = data_serializer.get('image')
            anime.rating = data_serializer.get('rating')
            anime.save()
            anime_serializer = GETAnimeSerializer(anime)

            return Response(anime_serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        anime = Anime.objects.get(pk=pk)
        anime.delete()
        return Response({'msg': 'Анимешка удалена'})


class CreateAnimeAPIViewSet(ModelViewSet):
    queryset = Anime.objects.all().order_by('-id')
    serializer_class = CreateAnimeSerializer
    pagination_class = AnimeAPIListPagination
    permission_classes = [IsAdminUser]


class StudioAPIViewSet(ModelViewSet):
    queryset = Studio.objects.all().order_by('-id')
    serializer_class = StudioSerializer


class LikeAPI(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):
        anime = Anime.objects.all().order_by('-id')
        serializer = GETAnimeSerializer(anime, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = RatingSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        # pk = data['who_like_pk']
        # count = data.get('count')
        # anime = Anime.objects.get(pk=pk)
        # anime.rating += count
        # anime.save()
        # anime_serializer = GETAnimeSerializer(anime)

        # return Response(anime_serializer.data)

    def post(self, request, format=None):
        return Response({'received data': request.data})


@api_view(['GET', 'POST'])
def IDK(request):
    parser_classes = [JSONParser]

    if request.method == 'GET':
        anime = Anime.objects.all().order_by('-id')
        serializer = GETAnimeSerializer(anime, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        count = data.get('count')
        return Response({'count': count ** 5})


print('HW')