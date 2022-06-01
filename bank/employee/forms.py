from django import forms
from .models import money
class moneyform(forms.ModelForm):
    class Meta:
          model=money
          fields='__all__'

