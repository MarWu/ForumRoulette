from django import forms


class UserCreationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.PasswordInput()
    email = forms.EmailField()


class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(label='Profile Picture')
