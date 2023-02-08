from django import forms
from .models import Image
from django.utils.text import slugify
from PIL import Image as Image_PIL, ImageOps, ImageFilter


class ImageCreateForm(forms.ModelForm):
    # x = forms.FloatField(widget=forms.HiddenInput())
    # y = forms.FloatField(widget=forms.HiddenInput())
    # width = forms.FloatField(widget=forms.HiddenInput())
    # height = forms.FloatField(widget=forms.HiddenInput())
    # filter = forms.ChoiceField(choices=[
    #     ('BLUR', 'Blur'),
    #     ('CONTOUR', 'Contour'),
    #     ('DETAIL', 'Detail'),
    #     ('EDGE_ENHANCE', 'Edge Enhance'),
    #     ('EDGE_ENHANCE_MORE', 'Edge Enhance More'),
    #     ('EMBOSS', 'Emboss'),
    #     ('FIND_EDGES', 'Find Edges'),
    #     ('SHARPEN', 'Sharpen'),
    #     ('SMOOTH', 'Smooth'),
    #     ('SMOOTH_MORE', 'Smooth More'),
    # ])
    # rotation_angle = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Image
        fields = ['image', 'title', 'description']
        # fields = ['image', 'title', 'description', 'x', 'y', 'width', 'height', 'filter', 'rotation_angle']

    # def save(self, commit=True, user=None):
    #     new_image = super().save(commit=False)
    #     image = Image_PIL.open(new_image)
    #
    #     #filter image
    #
    #     filter = self.cleaned_data['filter']
    #     if filter == 'BLUR':
    #         image = image.filter(ImageFilter.BLUR)
    #     elif filter == 'CONTOUR':
    #         image = image.filter(ImageFilter.CONTOUR)
    #     elif filter == 'DETAIL':
    #         image = image.filter(ImageFilter.DETAIL)
    #     elif filter == 'EDGE_ENHANCE':
    #         image = image.filter(ImageFilter.EDGE_ENHANCE)
    #     elif filter == 'EDGE_ENHANCE_MORE':
    #         image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    #     elif filter == 'EMBOSS':
    #         image = image.filter(ImageFilter.EMBOSS)
    #     elif filter == 'FIND_EDGES':
    #         image = image.filter(ImageFilter.FIND_EDGES)
    #     elif filter == 'SHARPEN':
    #         image = image.filter(ImageFilter.SHARPEN)
    #     elif filter == 'SMOOTH':
    #         image = image.filter(ImageFilter.SMOOTH)
    #     elif filter == 'SMOOTH_MORE':
    #         image = image.filter(ImageFilter.SMOOTH_MORE)
    #
    #     #cropping image
    #
    #     x = self.cleaned_data['x']
    #     y = self.cleaned_data['y']
    #     width = self.cleaned_data['width']
    #     height = self.cleaned_data['height']
    #     image = image.crop(x, y, width, height)
    #
    #     #rotate image
    #
    #     rotation_angle = self.cleaned_data['rotation_angle']
    #     image = image.rotate(rotation_angle)
    #     if commit:
    #         image.save()
    #     return image
