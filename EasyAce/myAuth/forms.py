from django.forms import ModelForm
from .models import MyUser

class SignupForm(ModelForm):
  class Meta:
    model = MyUser
    fields = ['username','email','role','gender','phone','password']
class LoginForm(ModelForm):
  class Meta:
    model = MyUser
    fields = ['username','password']