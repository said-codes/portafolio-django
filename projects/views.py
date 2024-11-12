# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construir el contenido del correo
            email_subject = f"Nuevo mensaje de contacto: {subject}"
            email_message = f"De: {name} <{email}>\n\n{message}"

            # Enviar el correo
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Reemplaza con tu correo destino si es diferente
            )

            messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'projects/contact.html', {'form': form})
