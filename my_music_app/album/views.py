from django.shortcuts import render, redirect

from my_music_app.album.forms import AlbumForm
from my_music_app.album.models import Album
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


def album_details(request, pk):
    album = Album.objects.get(id=pk)

    context = {'album': album}
    return render(request=request, template_name='album-details.html', context=context)


def album_edit(request, pk):
    album = Album.objects.get(id=pk)
    form = AlbumForm(request.POST or None, instance=album)

    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {'album': album, 'form': form}
    return render(request=request, template_name='edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.get(id=pk)
    form = AlbumForm(request.POST or None, instance=album)

    if request.method == "GET":
        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

        context = {'album': album, 'form': form}
        return render(request=request, template_name='delete-album.html', context=context)

    album.delete()
    return redirect('home-page')
