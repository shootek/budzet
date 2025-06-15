from django.views.decorators.csrf import csrf_exempt


def send_report_email(request):
    if request.method == 'POST':
        recipient = request.POST.get('email')  # pobierz adres e-mail z formularza
        if not recipient:
            return HttpResponse("Brak adresu e-mail.", status=400)

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
            'your_email@gmail.com',  # adres nadawcy (taki jak EMAIL_HOST_USER)
            [recipient],
        )
        email.attach('raport.pdf', pdf_file.read(), 'application/pdf')
        email.send()
        return HttpResponse(f"Mail wysłany na {recipient}.")
    
    return HttpResponse("Tylko POST dozwolony.", status=405)
