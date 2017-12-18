from django import forms
from django.core.validators import RegexValidator

from ask.models import User, Question, Answer

textValidator = RegexValidator(r"[a-zA-Z]",
                               "Text should contain letters")
passwordValidator = RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                   "Password should contain minimum eight characters, at least one letter and one number")


class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(validators=[textValidator],
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(validators=[textValidator],
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))
    username = forms.CharField(validators=[textValidator],
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(validators=[passwordValidator],
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class UserSignInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserSettingsForm(forms.ModelForm):
    first_name = forms.CharField(required=False,
                                 validators=[textValidator],
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(required=False,
                                validators=[textValidator],
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))

    username = forms.CharField(validators=[textValidator],
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))

    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))

    upload = forms.ImageField(required=False,
                              widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email',)


class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(validators=[textValidator],
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'maxlength': 100,
                                                          'minlength': 10,
                                                          'placeholder': 'Write here your title'}))

    text = forms.CharField(validators=[textValidator],
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'minlength': 30,
                                                        'placeholder': 'And here tell about your question in more detail'}))

    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'List here tags by separating them with a '
                                                                        'space (the first 10 will be saved)'}))

    class Meta:
        model = Question
        fields = ('title', 'text', 'tags',)


class WriteAnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'minlength': 20,
                                                        'placeholder': 'Enter your reply text'}))

    class Meta:
        model = Answer
        fields = ('text',)
