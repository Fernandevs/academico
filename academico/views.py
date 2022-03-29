from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, redirect
from django.template import Template, Context

def saludo(request): #cada función es una funcion vista
    doc_externo=open("C:/Users/ASUS/Documents/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/Plantilla1.html") #Carga un documento que posteriormente será renderizado
    
    plt=Template(doc_externo.read()) #carga el documento con la cadena de texto y lo lee
    
    doc_externo.close() #cierra el flujo del documento para ahorrar recursos
    
    ctx=Context() #se crea el contexto que si es conveniente, lleva atributos, funciones, (contexto de funcionalidad)
    
    documento=plt.render(ctx) #renderiza el contexto y listo para mostrar en navegador
    return HttpResponse(documento)

def damefecha(request):#pide la hora
    fecha_actual=datetime.datetime.now() #da la hora del servidor
    
    documento="""
    <html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>
    """ % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, anio):
    edadActual=18
    periodo=anio-2022
    edadFutura=edadActual+periodo
    documento="<html><body><h2> En el año %s tendras %s años" %(anio, edadFutura)
    
    return HttpResponse(documento)

def eliminar_usuarios(request, id):
    usuario=get_object_or_404(usuario, id= id)
    usuario.delete()
    return redirect(to="listar usuario")