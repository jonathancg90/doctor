from django import forms
from apps.doc.models.Country import Country
from crispy_forms.helper import FormHelper


class CountryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'nombre'

    class Meta:
        model = Country
        exclude = ['status']


class CountryFiltersForm(forms.Form):
    name__icontains = forms.CharField(max_length=100,
                                      required=False,
                                      label=(u'Name')
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(CountryFiltersForm, self).__init__(*args, **kwargs)
