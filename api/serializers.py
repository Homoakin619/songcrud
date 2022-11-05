from dataclasses import field
from rest_framework import serializers
from rest_framework.reverse import reverse

from musicapp.models import Song,Artiste,Lyric


class SongSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'date_released',
            'likes',
            'artiste_id',
            'detail_url'
        ]

    def get_detail_url(self,obj):
        request = self.context.get('request')
        return reverse('song-detail',request=request,kwargs={'pk':obj.pk})

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = [
            'first_name',
            'last_name',
            'age',
        ]

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = [
            'song_id',
            'content',
        ]