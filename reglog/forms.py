
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def email_validate(value):
      if User.objects.filter(email=value).exists():
        raise forms.ValidationError(
            'Такая почта уже зарегистрирована!',
            params={'value': value},
        )  

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Почта', validators=[email_validate])
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Еще раз', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username' : 'Логин',
            'email' : 'Почта',
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    email = forms.EmailField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        labels = {
            'email' : 'Почта',
        }