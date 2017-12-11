from django import forms

from ask.models import User

class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md',
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md',
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md',
                                                             'maxlength': 150,
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control input-md',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-md',
                                                                 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-md',
                                                                              'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
