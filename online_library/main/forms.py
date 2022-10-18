from django import forms

from online_library.main.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            )
        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            )
        }