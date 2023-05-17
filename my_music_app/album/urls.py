from django.urls import path, include

from my_music_app.album import views


urlpatterns = [
    path('add/', views.add_album, name='add-album'),
]
