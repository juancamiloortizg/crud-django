from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm

def inicio(request):
    personas = Persona.objects.all()    # select * from Persona
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html', contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)