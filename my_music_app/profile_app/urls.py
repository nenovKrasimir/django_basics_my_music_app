from django.urls import path, include

from my_music_app.profile_app import views


urlpatterns = [
    path('details/', views.profile_details, name='profile-details'),
    path('delete/', views.delete_profile, name='delete-profile')
]
