from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    documento = "<html><body><h1> Hola esto es un test  </h1></body></html>"

    return HttpResponse(documento)


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1> 
    Fecha y hora actuales %s 
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)


def calculaEdad(request, agno):
    edadActual = 18
    periodo = agno - 2019
    edadFutura = edadActual + periodo
    documento = "<html><body<h2> En el año %s tendrás %s años</h2></body></html>" % (agno, edadFutura)

    return HttpResponse(documento)


def saludoPlantilla(request):

    nombre = "Juan"
    apellido = "Díaz"
    doc_externo = open("templates/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona":nombre, "apellido_persona": apellido})
    documento = plt.render(ctx)

    return HttpResponse(documento)
