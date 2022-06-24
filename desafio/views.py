from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import prueba

# Create your views here.
def una_vista(request):
    return HttpResponse('<h1> mi perro dinamita </h1>')

def un_template(request):
    
    # template = loader.get_template('index.html')
    
    prueba1 = prueba(nombre = 'pepito')
    prueba2 = prueba(nombre= 'ricardo')
    prueba3 = prueba(nombre='jonatan')
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    return render (request, 'index.html',{'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # return HttpResponse(render)