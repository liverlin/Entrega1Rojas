
from django.http import HttpResponse
import random
from django.template import Context, Template

def inicio(request):
    return HttpResponse('Hola, soy la nueva pagina')

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1<h1/>
                        ''')
    
def numero_random(request):
    numero= random.randrange(15,100)
    texto = f'Este es tu numero random{numero}'
    return HttpResponse(texto)

def numero_de_usuario(request, numero):
    texto = f'<h1> Este es tu numero de usuario: {numero} </h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    plantilla = open(r"C:\Users\user\Documents\Python\EntregaFinalRojas\miproyecto\plantillas\mi_plantilla_1.html")
    
    template= Template(plantilla.read())
    context = Context() 
    plantilla_preparada = template.render(context)
    #acomoda el tempalte para que HttpsResponse lo entienda
    
    return HttpResponse(plantilla_preparada)