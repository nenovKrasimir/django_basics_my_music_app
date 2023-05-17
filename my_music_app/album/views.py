from django.shortcuts import render, redirect

from my_music_app.album.forms import AlbumForm
from my_music_app.profile_app.models import Profile


# Create your views here.
def add_album(request):
    form = AlbumForm(request.POST or None)
    context = {'form': form}

    user = Profile.objects.first()

    if form.is_valid():
        album = form.save()
        album.user = user
        album.save()
        return redirect('home-page')

    return render(request=request, template_name='add-album.html', context=context)
