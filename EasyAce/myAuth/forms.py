from django.forms import ModelForm
from .models import MyUser

class SignupForm(ModelForm):
  class Meta:
    model = MyUser
    fields = ['username','role','password']
class LoginForm(ModelForm):
  class Meta:
    model = MyUser
    fields = ['username','password']