from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View

from .models import Category, Expense


class JsonView(View):

    def dispatch(self, request, *args, **kwargs):
        data = super(JsonView, self).dispatch(request, *args, **kwargs)

        if isinstance(data, HttpResponse):
            return data
        return JsonResponse(data)


class IndexView(TemplateView):
    template_name = 'index.html'


class ExpenseView(JsonView):

    def get(self, request, *args, **kwargs):
        expenses = [Expense(description='Expense %i' % i, amount=i) for i in range(5)]
        return {'expenses': [model_to_dict(expense) for expense in expenses]}