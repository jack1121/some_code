from django import forms

class NameForm(forms.Form):
	"""docstring for NameForm"""
	your_name = forms.CharField(label = 'your_name', max_length = 100)
