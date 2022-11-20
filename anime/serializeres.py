from rest_framework.serializers import *

from .models import *


class StudioSerializer(ModelSerializer):
    # animes = PrimaryKeyRelatedField(many=True, queryset=Anime.objects.all())

    class Meta:
        depth = 1
        model = Studio
        fields = ['name', 'base_city', 'animes']


class GETAnimeSerializer(ModelSerializer):
    # studio_data = SerializerMethodField(read_only=True)

    class Meta:
        depth = 1
        model = Anime
        fields = ['id', 'title', 'description', 'image', 'rating', 'studio', ]

    # def get_studio_data(self, obj):
    #     return {
    #         'id': obj.studio.pk,
    #         'name': obj.studio.name,
    #         'base_city': obj.studio.base_city
    #     }


class CreateAnimeSerializer(ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'image', 'rating', 'studio', ]


