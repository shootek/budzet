from django.shortcuts import render, redirect
from .models import Entry, Category
from .forms import EntryForm
from django.db.models import Sum

def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    return render(request, 'budget/add_entry.html', {'form': form})


def home(request):
    entry_type = request.GET.get('type')
    category_id = request.GET.get('category')

    # Nowe filtry: data i kwota
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    min_amount = request.GET.get('min_amount')
    max_amount = request.GET.get('max_amount')

    entries = Entry.objects.all().order_by('-date')

    # Filtrowanie typu (income/expense)
    if entry_type in ['income', 'expense']:
        entries = entries.filter(type=entry_type)

    # Filtrowanie po kategorii
    if category_id:
        entries = entries.filter(category_id=category_id)

    # Filtrowanie po dacie
    if start_date:
        entries = entries.filter(date__gte=start_date)
    if end_date:
        entries = entries.filter(date__lte=end_date)

    # Filtrowanie po kwocie
    if min_amount:
        entries = entries.filter(amount__gte=min_amount)
    if max_amount:
        entries = entries.filter(amount__lte=max_amount)

    total_income = Entry.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Entry.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    categories = Category.objects.all()

    return render(request, 'budget/home.html', {
        'entries': entries,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'categories': categories,
        'selected_type': entry_type,
        'selected_category': category_id,
        'start_date': start_date,
        'end_date': end_date,
        'min_amount': min_amount,
        'max_amount': max_amount,
    })
