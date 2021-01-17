from django.forms import ModelForm      
from cloudinary.forms import CloudinaryFileField
from .models import Closet

class ClosetUploadForm(ModelForm):

    class Meta:
        model = Closet
        fields = ['image']
        