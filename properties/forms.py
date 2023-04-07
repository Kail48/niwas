from django.forms import ModelForm
from django import forms
from .models import *

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields=['category','title','description','price','city','address','parking','water']
        widgets={
            'parking':forms.RadioSelect(),
            'water':forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': ''})
        self.fields['title'].widget.attrs.update({'class': 'input is-primary'})
        self.fields['description'].widget.attrs.update({'class': 'textarea'})
        self.fields['price'].widget.attrs.update({'class': 'input is-rounded'})
        self.fields['city'].widget.attrs.update({'class': ''})
        self.fields['address'].widget.attrs.update({'class': 'input is-link'})
        self.fields['parking'].widget.attrs.update({'class': 'radio-choice'})
        self.fields['water'].widget.attrs.update({'class': 'radio-choice'})

class KitchenForm(ModelForm):
    class Meta:
        model = Kitchen
        fields=['type','image']
        widgets={
            'type':forms.RadioSelect(),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget.attrs.update({'class': 'radio-choice'})
        self.fields['image'].widget.attrs.update({'class': 'file-input'})

class BathroomForm(ModelForm):
    class Meta:
        model = Bathroom
        fields=['type','image']
        widgets={
            'type':forms.RadioSelect(),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget.attrs.update({'class': 'radio-choice'})
        self.fields['image'].widget.attrs.update({'class': 'file-input'})

class BedroomForm(ModelForm):
    class Meta:
        model = Bedroom
        fields=['numbers']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BedroomImageForm(ModelForm):
    class Meta:
        model = BedroomImage
        fields=['image']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'file-input'})

class VideoForm(ModelForm):
    class Meta:
        model = VideoTour
        fields=['videofile']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['videofile'].widget.attrs.update({'class': 'file-input'})