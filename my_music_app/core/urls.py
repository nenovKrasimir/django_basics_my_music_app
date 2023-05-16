from django.urls import path, include

from my_music_app.core import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
]
