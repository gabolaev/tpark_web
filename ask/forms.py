from django import forms

from ask.models import User


class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'maxlength': 150,
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class UserSignInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'maxlength': 150,
                                                             'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserSettingsForm(forms.ModelForm):
    username = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'maxlength': 150,
                                                             'placeholder': 'Username'}))

    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))

    avatar = forms.ImageField(required=False,widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('username', 'email',)
