
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_music_app.core.urls')),
    path('profile/', include('my_music_app.profile_app.urls'))
]
