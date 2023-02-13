from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import person, sale

def index(request):
    return render (request, "ventas/index.html")

def registrar(request):
    return render (request, "ventas/register.html")

def search(request):
    ls_personas = person.objects.all()
    return render(request, "ventas/search.html", {
        "lista_personas" : ls_personas
    })

def search_b(request):
    docID = request.POST['doc']
    ls_persona = person.objects.filter(document = docID)
    if(len(ls_persona) == 0):
        return HttpResponse ("<h1>No se encntro ningun registro, o el documento de identidad no existe.</h1>")
    else:
        key = person.objects.get(document = docID)
        ventas = sale.objects.filter(document_p = key.pk)
        return render(request, "ventas/searchb.html", {
            "lista_ventas" : ventas,
            "doc" : docID
        })

#RECIBIR DATOS Y GUARDARLOS
def save(request):
    error = "<h1>Error en uno de los campos:</h1><h3>Documento de Identidad : 8 digitos</h3><h3>Nombres : Mayor a 3 digitos</h3><h3>Correo : Terminar en @gmail</h3><h3>Monto : Mayor a 0</h3>"
    docID = request.POST['doc']
    nombre = request.POST['nam']
    correo = request.POST['email']
    monto = request.POST['monto']
    #Comprobar @gmail.com => 10 caracteres
    termino = correo[-10:]
    try:
        monto = float(monto)
        #COMPROBACION DE DATOS
        if(len(docID) == 8 and len(nombre) > 3 and termino == "@gmail.com" and monto > 0):
            #Comprobar si la persona ya existe
            persona = person.objects.filter(document = docID)
            if(len(persona) == 0):
                #No registrada (Nuevo)
                person.objects.create(document = docID, name = nombre, mail = correo)
                sl = sale(document_p = person.objects.get(document=docID), amount = monto, date = "2022-06-11 00:00:00")
                sl.save()
                return HttpResponse("<h1>Registrado con exito</h1>")
            else:
                #Existe (Registrada)
                saveS(docID, monto)
                return HttpResponse ("<h1>Registrado con exito</h1>")
        else:
            return HttpResponse (error)
    except ValueError:
        return HttpResponse (error)
#Guardar ventas de Personas ya registradas
def saveS(doc, monto):
    venta = sale(document_p = person.objects.get(document = doc), amount = monto, date = "2022-06-11 00:00:00")
    venta.save()
