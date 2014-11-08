from datetime import date, datetime

from django import forms

from .models import Expense


class DateInput(forms.DateInput):

    def render(self, name, value, attrs=None):
        value = value.strftime('%Y-%m-%d') if isinstance(value, (date, datetime)) else value
        return super(DateInput, self).render(name, value, attrs=attrs)


class ExpenseModelForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('date', 'amount', 'description',)
        widgets = {
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }