
import matplotlib.pyplot as plt
from io import BytesIO
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.db.models import Sum
from budzet.models import Expense


def expenses_chart_view(request):
    data = Expense.objects.values('category__name').annotate(total=Sum('amount'))
    labels = [item['category__name'] for item in data]
    values = [item['total'] for item in data]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Wydatki wg kategorii")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')


def generate_pdf_view(request):
    expenses = Expense.objects.all()
    total = sum(e.amount for e in expenses)
    template = get_template('report_template.html')
    html = template.render({'expenses': expenses, 'total': total})
    response = HttpResponse(content_type='application/pdf')
    pisa.CreatePDF(html, dest=response)
    return response


def send_report_email(request):
    expenses = Expense.objects.all()
    total = sum(e.amount for e in expenses)
    template = get_template('report_template.html')
    html = template.render({'expenses': expenses, 'total': total})

    pdf_file = BytesIO()
    pisa.CreatePDF(html, dest=pdf_file)
    pdf_file.seek(0)

    email = EmailMessage(
        'Twój raport wydatków',
        'W załączniku przesyłamy Twój raport PDF.',
        'your_email@gmail.com',
        ['odbiorca@example.com'],
    )
    email.attach('raport.pdf', pdf_file.read(), 'application/pdf')
    email.send()
    return HttpResponse("Mail wysłany.")
