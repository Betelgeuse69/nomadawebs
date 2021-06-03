from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
            contact_form = ContactForm(data = request.POST)
            if contact_form.is_valid():
                name = request.POST.get('name', '')
                email = request.POST.get('email', '')
                content = request.POST.get('content', '')
                #Enviamos email y redireccionamos:
                email = EmailMessage(
                    "La Caffettiera: Nuevo mensaje de contacto",
                    "De {} <{}>\n\n{}".format(name, email, content),
                    "no-contestar@inbox.mailtrap.io",
                    ["betelgeuse.cazador@gmail.com"],
                    reply_to = [email]
                )

                try:
                    email.send()
                    #Envío correcto:
                    return redirect(reverse('contact')+"?ok") #Con reverse conseguimos no tener que poner literalmente la url a donde vamos a redirigir poniendo en su lugar la ruta de urls.py
                except:
                    #Algo ha fallado:
                    return redirect(reverse('contact')+"?fail")

    return render(request,"contact/contact.html", {'form':contact_form})