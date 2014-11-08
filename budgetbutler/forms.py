from django import forms

from .models import Expense


class DateInput(forms.DateInput):

    def render(self, name, value, attrs=None):
        return super(DateInput, self).render(name, value.strftime('%Y-%m-%d'), attrs=attrs)


class ExpenseModelForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('date', 'amount', 'description',)
        widgets = {
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }