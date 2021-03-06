import datetime

from django.http import HttpResponse, JsonResponse
from django.views.generic import View, DayArchiveView, CreateView, TemplateView

from .forms import ExpenseModelForm
from .models import Expense
from .utils import get_months, get_days


class JsonView(View):
    safe = True

    def dispatch(self, request, *args, **kwargs):
        data = super(JsonView, self).dispatch(request, *args, **kwargs)

        if isinstance(data, HttpResponse):
            return data
        return JsonResponse(data, safe=self.safe)
    

class MonthListView(TemplateView):
    template_name = 'views/month-list-view.html'

    def get_context_data(self, **kwargs):
        years_with_months = [
            (year, get_months(year))
            for year in (2014, 2015)
        ]
        return super(MonthListView, self).get_context_data(years_with_months=years_with_months, **kwargs)
    
    
class MonthDetailView(TemplateView):
    template_name = 'views/month-detail-view.html'
    
    def get_context_data(self, **kwargs):
        date = datetime.date(int(self.kwargs.get('year')), int(self.kwargs.get('month')), 1)
        weeks_with_days = [
            (week, [(day, Expense.objects.get_budget(day)) for day in days])
            for week, days in get_days(date.year, date.month)
        ]
        return super(MonthDetailView, self).get_context_data(date=date, weeks_with_days=weeks_with_days)


class IndexView(MonthListView):
    template_name = 'index.html'


class ExpenseMixIn(object):
    model = Expense


class ExpenseListView(ExpenseMixIn, DayArchiveView):
    template_name = 'views/day-detail-view.html'
    allow_empty = True
    allow_future = True
    date_field = 'date'
    month_format = '%m'

    def render_to_response(self, context, **response_kwargs):
        objects, date = (lambda object_list, day, **extra: (object_list, day))(**context)
        context.update(total=objects.get_sum_amount(), budget=Expense.objects.get_budget(date))
        return super(ExpenseListView, self).render_to_response(context, **response_kwargs)


class ExpenseAddView(ExpenseMixIn, CreateView):
    form_class = ExpenseModelForm
    template_name = 'forms/add-expense-form.html'

    def form_valid(self, form):
        self.object = form.save()
        url = self.get_success_url()
        return JsonResponse({'pk': self.object.pk, 'url': url}, status=201)