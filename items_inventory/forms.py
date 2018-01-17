from django import forms
from django.contrib.admin import widgets 
from django.core.exceptions import ValidationError
from items_inventory.models import Record

class RecordForm(forms.ModelForm):
    in_date = forms.DateField(help_text='Data w formacie DD.MM.YYYY',
                              label='Data przychodu i względnie rozchodu',
                              widget=forms.DateInput(attrs={'id':'datetimepicker'}),
                              required=False)
    
    class Meta:
        model = Record
        fields = '__all__'

    def clean(self):
        number_of_incoming = int(1 if None else self.cleaned_data['number_of_incoming'])
        number_of_outgoing = int(self.cleaned_data['number_of_outgoing']) or 0
        number_result = int(self.cleaned_data['number_result']) or 0

        incoming_value = int(self.cleaned_data['incoming_value']) or 0
        outgoing_value = int(self.cleaned_data['outgoing_value']) or 0
        value_result = int(self.cleaned_data['value_result']) or 0
        result = number_of_incoming - number_of_outgoing
        result2 = incoming_value - outgoing_value
        if number_result != result:
            raise ValidationError('Nie zgadza się stan ilości {}'.format(number_result))
        if value_result != result2:
            raise ValidationError('Nie zgadza się stan wartości {}'.format(value_result))
        return self.cleaned_data
        