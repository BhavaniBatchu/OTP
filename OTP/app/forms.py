from django import forms
from . models import Aadhar
from django_recaptcha.fields import ReCaptchaField

class AadharForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Aadhar
        fields = "__all__"