from django.shortcuts import render
from django.http import JsonResponse
from budget.models import Entry
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def expenses_chart_view(request):
    return render(request, 'reporting/expenses_chart.html')

def expenses_chart_data(request):
    base_queryset = Entry.objects.annotate(month=TruncMonth('date')).values('month', 'type')
    data = (
        base_queryset
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    labels = sorted(list(set(d['month'].strftime('%B') for d in data)))
    income_map = {d['month'].strftime('%B'): float(d['total']) for d in data if d['type'] == 'income'}
    expense_map = {d['month'].strftime('%B'): float(d['total']) for d in data if d['type'] == 'expense'}

    incomes = [income_map.get(label, 0) for label in labels]
    expenses = [expense_map.get(label, 0) for label in labels]

    return JsonResponse({
        'labels': labels,
        'incomes': incomes,
        'expenses': expenses,
    })
