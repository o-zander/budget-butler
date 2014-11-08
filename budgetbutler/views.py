from django.http import HttpResponse, JsonResponse
from django.views.generic import View, DayArchiveView, RedirectView, CreateView
from budgetbutler.utils import get_date_url

from .forms import ExpenseModelForm
from .models import Expense


class JsonView(View):
    safe = True

    def dispatch(self, request, *args, **kwargs):
        data = super(JsonView, self).dispatch(request, *args, **kwargs)

        if isinstance(data, HttpResponse):
            return data
        return JsonResponse(data, safe=self.safe)


class RedirectToToday(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return get_date_url()


class ExpenseMixIn(object):
    model = Expense


class ExpenseListView(ExpenseMixIn, DayArchiveView):
    template_name = 'budgetbutler/expense-list-view.html'
    allow_empty = True
    allow_future = True
    date_field = 'date'
    month_format = '%m'

    def get_context_data(self, object_list, **kwargs):
        kwargs.update(sum_amount=object_list.get_sum_amount(), object_list=object_list)
        return super(ExpenseListView, self).get_context_data(**kwargs)


class ExpenseAddView(ExpenseMixIn, CreateView):
    form_class = ExpenseModelForm
    template_name = 'budgetbutler/expense-add-view.html'