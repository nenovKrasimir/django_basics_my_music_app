from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLField(attrs={'type': 'url'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'genre': 'Genre',
            'artist': 'Artist',
            'image': 'Image',
            'price': 'Price',
        }