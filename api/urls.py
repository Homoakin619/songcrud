from django.urls import path

from . import views

urlpatterns = [
    path('',views.SongApiView.as_view()),
    path('song/<int:pk>/',views.SongDetailApiView.as_view(),name='song-detail'),
    path('artiste/',views.ArtisteApiView.as_view()),
    path('lyrics/',views.LyricsApiView.as_view()),
]