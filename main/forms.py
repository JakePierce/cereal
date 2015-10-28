from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div 
from crispy_forms.bootstrap import FormActions
from main.models import Cereal, Manufacturer


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    #arg are variables, key-word arguments are variables and a value.
    #val, val2="something"
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
            Div('name', 'email', 'phone', css_class='col-md-6'),
            Div('message', css_class='col-md-6')
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary"))

        )


class ManufacturerEditForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ManufacturerEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )


class CerealEditForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CerealEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save changes', "Save Changes", css_class="btn-primary")
                )
            )