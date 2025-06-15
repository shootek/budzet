from django.http import JsonResponse
from budget.models import Entry
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def expenses_chart_view(request):
    # Grupowanie wydatków (typ=expense) po miesiącach
    data = (
        Entry.objects.filter(type='expense')
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    labels = [d['month'].strftime('%B') for d in data]
    values = [float(d['total']) for d in data]

    return JsonResponse({
        'labels': labels,
        'values': values,
    })
