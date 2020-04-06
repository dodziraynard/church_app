from django import forms
from . models import DailyDevotion
from . models import Video, Preaching, Material, Leader

class DevotionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    background = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), required=False)
    class Meta:
        model = DailyDevotion
        fields = ["title",
                "background",
                "content"]

class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                        required=False, label="Description")
    image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), 
                        required=False,
                        label="Video Thumbnail")
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), 
                        required=False, label="Video (.mp4 only)")

    class Meta:
        model = Video
        fields = [      "title",
                        "file",
                        "desc",
                        "image"]