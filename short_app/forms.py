from django import forms
from short_app.models import Bookmark


class BookmarkCreateForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'description']
