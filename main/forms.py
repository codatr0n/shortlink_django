from django import forms

from .models import Link, Tag


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'tags']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Give your link a name..'}
            ),
            'url': forms.URLInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Paste your link here..'}
            ),
            'tags': forms.SelectMultiple(
                attrs={'class': 'form-control form-control-sm'}
            )
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'description', 'code', 'tag_type']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Give your tag a name..'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Tag description..'}
            ),
            'code': forms.Textarea(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Paste the script here..'}
            ),
            'tag_type': forms.Select(
                attrs={'class': 'form-control form-control-sm'}
            ),
        }