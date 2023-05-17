from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, resolve_url
from my_music_app.profile_app.forms import ProfileForm
from my_music_app.profile_app.models import Profile
from my_music_app.ultilis.helper_funcs import check_user_exist


def home_page(request):
    form = ProfileForm(request.POST or None)
    context = {'form': form}

    if check_user_exist():
        user = Profile.objects.first()
        context['user_albums'] = user.album_set.all()
        context['user'] = user
        return render(request=request, template_name='home-with-profile.html', context=context)

    if form.is_valid():
        form.save()
        return redirect('home-page')

    return render(request=request, template_name='home-no-profile.html', context=context)
