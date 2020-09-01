from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForm(forms.Form):
    name = forms.CharField(label='Imię')
    surname = forms.CharField(label='Nazwisko')
    phone_number = forms.IntegerField(label='Numer telefonu')
    extra_info = forms.CharField(widget=forms.Textarea, label="Dodatkowe informacje", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(

            'name',
            'surname',
            'phone_number',
            'extra_info',
            Submit('submit', 'Prześlij', css_class='btn-success')
        )




class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ['name', 'surname', 'phone_number', 'extra_info']