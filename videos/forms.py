from django import forms
from .models import Video

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'file']

class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'level',
            'duration',
            'file',
        ]