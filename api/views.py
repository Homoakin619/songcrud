from rest_framework import generics

from .serializers import SongSerializer,ArtisteSerializer,LyricSerializer
from musicapp.models import Song,Artiste,Lyric

class SongApiView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

class SongDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class ArtisteApiView(generics.ListCreateAPIView):
    serializer_class = ArtisteSerializer
    queryset = Artiste.objects.all()

class LyricsApiView(generics.ListCreateAPIView):
    serializer_class = LyricSerializer
    queryset = Lyric.objects.all()
