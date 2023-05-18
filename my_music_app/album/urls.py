from django.urls import path, include

from my_music_app.album import views


urlpatterns = [
    path('add/', views.add_album, name='add-album'),
    path('details/<int:pk>', views.album_details, name='album-details'),
    path('edit/<int:pk>', views.album_edit, name='album-edit'),
    path('delete/<int:pk>', views.album_delete, name='album-delete')
]
