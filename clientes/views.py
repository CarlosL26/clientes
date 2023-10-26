from tracemalloc import get_object_traceback
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Clientes
from .forms import FormClientes
from .forms import ContactoForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    return render(request, 'persona\index.html')

def listado(request):
    personas = Clientes.objects.all(),
    return render(request, 'persona\listado.html',{"personas":personas})

def nueva(request):
    if request.method == "POST":
        formpersona = FormClientes(request.POST)
        if formpersona.is_valid():
            formpersona.save()
            return redirect('listado')
    else:
        formpersona = FormClientes()
    return render(request,'persona/nueva.html',{"formpersona":formpersona})

def editor(request):
    Persona= get_object_traceback

def contacto(request):
    Contacto_Form = ContactoForm()

    if request.method == "POST":
        Contacto_Form = ContactoForm(request.POST)
        if Contacto_Form.is_valid():
            nombre = request.POST['nombre']
            email = request.POST['email']
            mensaje = request.POST['mensaje']

            send_mail('Contacto',
                      f'Nombre:{nombre}\nEmail:{email}\nMensaje:{mensaje}',
                      'tu_email@dominio.com',
                      ['correo_destino@dominio.com'],
                      fail_silently=False,
            )
            messages.success(request, 'Correo enviado con éxito')
        else:
            messages.error(request, 'Error')  # Agrega "request" para especificar el contexto de mensajes.

    return render(request, 'persona/contacto.html', {'Contacto_Form': Contacto_Form})

def clientespaginacion(request):
    clientes = Clientes.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(clientes, 2)  #  paginate_by 5
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)
    return render(request, "persona/clientespaginacion.html", {"clientes": clientes})