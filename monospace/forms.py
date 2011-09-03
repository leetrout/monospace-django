from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class MonospaceForm(forms.Form):

  def addError(self, message):
    self._errors[NON_FIELD_ERRORS] = self.error_class([message])

class SignInForm(MonospaceForm):
  
  email = forms.EmailField(
    required = True
  )
  
  password = forms.CharField(
    required = True, 
    widget = forms.PasswordInput(render_value = False)
  )
  
class CardForm(MonospaceForm):
  
  last_4_digits = forms.CharField(
    required = True,
    min_length = 4,
    max_length = 4,
    widget = forms.HiddenInput()
  )
  
  stripe_token = forms.CharField(
    required = True,
    widget = forms.HiddenInput()
  )
  
class UserForm(CardForm):
  
  name = forms.CharField(
    required = True
  )
  
  email = forms.EmailField(
    required = True
  )

  password1 = forms.CharField(
    required = True, 
    widget = forms.PasswordInput(render_value = False),
    label = 'Password'
  )

  password2 = forms.CharField(
    required = True, 
    widget = forms.PasswordInput(render_value = False),
    label = 'Password confirmation'
  )
  
  def clean(self):
    cleaned_data = self.cleaned_data
    password1 = cleaned_data.get('password1')
    password2 = cleaned_data.get('password2')
    if password1 != password2:
      raise forms.ValidationError('Passwords do not match')
    return cleaned_data
  
  
  