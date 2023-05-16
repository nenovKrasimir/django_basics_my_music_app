from my_music_app.profile_app.models import Profile


def check_user_exist():
    return Profile.objects.exists()