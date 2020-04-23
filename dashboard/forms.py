from django import forms
from . models import DailyDevotion
from . models import Video, Audio, Material, Leader, Church

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

class MaterialForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                        required=False, label="Description")
    image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), 
                        required=False,
                        label="File Thumbnail")
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), 
                        required=False, label="FILE (.pdf only)")

    class Meta:
        model = Material
        fields = [      "title",
                        "file",
                        "desc",
                        "image"]

class AudioForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                        required=False, label="Description")
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), 
                        required=False, label="Audio file (.mp3 only)")

    class Meta:
        model = Audio
        fields = [      "title",
                        "file",
                        "desc"]

class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        fields = [  "position",
                    "user",
                    "contacts"]

class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = [ 
            "name",
            "about",
            "address",
            "head_pastor",
            "help_text",
            "momo",
            "contact",
            "church_id",
        ]