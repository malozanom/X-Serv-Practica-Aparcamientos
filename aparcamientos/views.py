from django.shortcuts import render, render_to_response
from aparcamientos.models import Aparcamiento, Comentario
from aparcamientos.models import Preferencia, Seleccione
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.contrib.auth.models import User
from django.utils import timezone
import xml.etree.ElementTree as ET
from urllib.request import urlopen


# Create your views here.


@csrf_exempt
def pagPrincipal(request):
    plantilla = get_template('principal.html')
    if request.method == "POST":
        if "boton" in request.POST:
            opcion = request.POST['boton']
            if opcion == "Activar":
                masComentados = Aparcamiento.objects.annotate(
                                num_com=Count('comentario')).filter(
                                accesibilidad=1).order_by('-num_com')[:5]
                accesibilidad = True
        else:
            opcion = ""
            # Parsear en Python3 con ElementTree una URL:
            # http://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib2
            xmlFile = urlopen("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
            arbol = ET.parse(xmlFile)
            raiz = arbol.getroot()

            for elem in arbol.iter():
                if "ID-ENTIDAD" in elem.attrib.values():   # Es un diccionario
                    nuevoAparcamiento = Aparcamiento(idEntidad=elem.text)
                elif "NOMBRE" in elem.attrib.values():
                    nuevoAparcamiento.nombre = elem.text
                elif "DESCRIPCION" in elem.attrib.values():
                    nuevoAparcamiento.descripcion = elem.text
                elif "ACCESIBILIDAD" in elem.attrib.values():
                    nuevoAparcamiento.accesibilidad = elem.text
                elif "CONTENT-URL" in elem.attrib.values():
                    nuevoAparcamiento.contentUrl = elem.text
                elif "NOMBRE-VIA" in elem.attrib.values():
                    nuevoAparcamiento.nombreVia = elem.text
                elif "CLASE-VIAL" in elem.attrib.values():
                    nuevoAparcamiento.claseVial = elem.text
                elif "TIPO-NUM" in elem.attrib.values():
                    nuevoAparcamiento.tipoNum = elem.text
                elif "NUM" in elem.attrib.values():
                    nuevoAparcamiento.num = elem.text
                elif "ORIENTACION" in elem.attrib.values():
                    nuevoAparcamiento.orientacion = elem.text
                elif "LOCALIDAD" in elem.attrib.values():
                    nuevoAparcamiento.localidad = elem.text
                elif "PROVINCIA" in elem.attrib.values():
                    nuevoAparcamiento.provincia = elem.text
                elif "CODIGO-POSTAL" in elem.attrib.values():
                    nuevoAparcamiento.codigoPostal = elem.text
                elif "BARRIO" in elem.attrib.values():
                    nuevoAparcamiento.barrio = elem.text
                elif "DISTRITO" in elem.attrib.values():
                    nuevoAparcamiento.distrito = elem.text
                elif "COORDENADA-X" in elem.attrib.values():
                    nuevoAparcamiento.coordenadaX = elem.text
                elif "COORDENADA-Y" in elem.attrib.values():
                    nuevoAparcamiento.coordenadaY = elem.text
                elif "LATITUD" in elem.attrib.values():
                    nuevoAparcamiento.latitud = elem.text
                elif "LONGITUD" in elem.attrib.values():
                    nuevoAparcamiento.longitud = elem.text
                elif "TELEFONO" in elem.attrib.values():
                    nuevoAparcamiento.telefono = elem.text
                elif "EMAIL" in elem.attrib.values():
                    nuevoAparcamiento.email = elem.text
                elif "TIPO" in elem.attrib.values():
                    nuevoAparcamiento.save()
                else:
                    pass

    if request.method == "GET" or opcion == "Desactivar" or opcion == "":
        # Agrupar los aparcamientos por los 5 más comentados:
        # https://docs.djangoproject.com/en/1.8/topics/db/aggregation/
        masComentados = Aparcamiento.objects.annotate(
                        num_com=Count('comentario')).order_by('-num_com')[:5]
        accesibilidad = False

    listaPreferencias = Preferencia.objects.all()
    listaUsuarios = User.objects.all()
    if len(listaPreferencias) != len(listaUsuarios):
        for usuario in listaUsuarios:
            try:
                user = Preferencia.objects.get(usuario=usuario)
            except Preferencia.DoesNotExist:
                user = Preferencia(usuario=usuario)
                user.save()

        listaPreferencias = Preferencia.objects.all()

    listaAparcamientos = Aparcamiento.objects.all()
    if len(listaAparcamientos) == 0:
        cargar = True
    else:
        cargar = False

    # Renderizar correctamente todo el contexto (el login y las variables):
    # https://docs.djangoproject.com/en/1.8/ref/templates/api/#playing-with-context-objects
    contexto = RequestContext(request, {'listaUsuarios': listaPreferencias,
                                        'accesibilidad': accesibilidad,
                                        'masComentados': masComentados,
                                        'cargar': cargar})

    return HttpResponse(plantilla.render(contexto))


def css(request):
    plantilla = get_template('css/style.css')
    if request.user.is_authenticated():
        usuario = User.objects.get(username=request.user.username)
        try:
            usuario = Preferencia.objects.get(usuario=usuario)
        except:
            return HttpResponse(plantilla.render(), content_type="text/css")

        contexto = Context({'color': usuario.colorFondo,
                            'tamanio': usuario.tamanioLetra})

        return HttpResponse(plantilla.render(contexto),
                            content_type="text/css")

    else:
        return HttpResponse(plantilla.render(), content_type="text/css")


# Como hacer una view personalizada para hacer login:
# https://www.fir3net.com/Web-Development/Django/django.html
@csrf_exempt
def loginUsuario(request):
    if request.method == "POST":
        nombreUsuario = request.POST['username']
        contrasena = request.POST['password']
        usuario = authenticate(username=nombreUsuario, password=contrasena)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)

    return HttpResponseRedirect('/')


@csrf_exempt
def logoutUsuario(request):
    if request.method == "POST":
        logout(request)

    return HttpResponseRedirect('/')


@csrf_exempt
def pagUsuario(request, nombreUsuario):
    if request.method == "GET":
        try:
            usuario = User.objects.get(username=nombreUsuario)
        except User.DoesNotExist:
            plantilla = get_template('error.html')

            return HttpResponse(plantilla.render(), status=404)

        # Como obtener una query string:
        # https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.META
        qs = request.META['QUERY_STRING']

    else:
        qs = ""
        if request.user.is_authenticated():
            usuario = User.objects.get(username=request.user.username)
            try:
                usuario = Preferencia.objects.get(usuario=usuario)
            except:
                user = User.objects.get(username=request.user.username)
                usuario = Preferencia(usuario=user)

            if 'titulo' in request.POST:
                usuario.titulo = request.POST['titulo']
            else:
                usuario.tamanioLetra = request.POST['tamanioLetra']
                usuario.colorFondo = request.POST['colorFondo']
            usuario.save()

    plantilla = get_template('usuario.html')
    usuario = User.objects.get(username=nombreUsuario)
    if qs == "":
        seleccionados = Seleccione.objects.filter(usuario=usuario)
    else:
        # Como extraer entradas utilizando los operadores de desigualdad:
        # http://stackoverflow.com/questions/10040143/how-to-do-a-less-than-or-equal-to-filter-in-django-queryset
        restantes = Seleccione.objects.filter(id__gt=(int(qs)))
        seleccionados = restantes.filter(usuario=usuario)

    if len(seleccionados) <= 5:
        fin = True
    else:
        fin = False

    try:
        usuario = Preferencia.objects.get(usuario=usuario)
    except:
        usuario = ""

    contexto = RequestContext(request, {'usuario': usuario,
                                        'nombreUsuario': nombreUsuario,
                                        'seleccionados': seleccionados,
                                        'fin': fin})

    return HttpResponse(plantilla.render(contexto))


@csrf_exempt
def aparcamientos(request):
    plantilla = get_template('aparcamientos.html')
    if request.method == "POST":
        if "opciones" in request.POST:
            distrito = request.POST['opciones']
            if distrito == "Todos":
                listaAparcamientos = Aparcamiento.objects.all()
            else:
                listaAparcamientos = Aparcamiento.objects.filter(
                                     distrito=distrito)
        else:
            if "marcar" in request.POST:
                recibido = request.POST['marcar']
                idEntidad = recibido.split(',')[0]
                nombreUsuario = recibido.split(',')[1]
                aparcamiento = Aparcamiento.objects.get(idEntidad=idEntidad)
                usuario = User.objects.get(username=nombreUsuario)
                # Obtener la fecha y hora actual:
                # http://stackoverflow.com/questions/37607411/django-runtimewarning-datetimefield-received-a-naive-datetime-while-time-zon
                fechaHora = timezone.now()
                nuevaSeleccion = Seleccione(aparcamiento=aparcamiento,
                                            usuario=usuario,
                                            fechaHora=fechaHora)
                nuevaSeleccion.save()
            else:
                recibido = request.POST['desmarcar']
                idEntidad = recibido.split(',')[0]
                nombreUsuario = recibido.split(',')[1]
                aparcamiento = Aparcamiento.objects.get(idEntidad=idEntidad)
                usuario = User.objects.get(username=nombreUsuario)
                borrarSeleccion = Seleccione.objects.get(
                                  aparcamiento=aparcamiento, usuario=usuario)
                borrarSeleccion.delete()

    if request.method == "GET" or "opciones" not in request.POST:
        listaAparcamientos = Aparcamiento.objects.all()
        distrito = "Todos"

    # Obtener todos los valores de la BD para un campo del modelo:
    # http://stackoverflow.com/questions/6653382/python-django-load-column-from-database-into-list
    listaDistritos = Aparcamiento.objects.all().values_list('distrito')

    # Obtener los valores únicos de una lista:
    # http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    listaDistritosUnicos = list(set(listaDistritos))

    # Convertir lista de tuplas en lista:
    # http://stackoverflow.com/questions/10941229/convert-list-of-tuples-to-list
    listaDistritosUnicos = [distrito[0] for distrito in listaDistritosUnicos]

    if request.user.is_authenticated():
        seleccionados = Seleccione.objects.all().values_list(
                        'aparcamiento').filter(usuario=request.user)
        listaSeleccionados = [seleccionado[0] for seleccionado
                              in seleccionados]
    else:
        listaSeleccionados = ""

    contexto = RequestContext(request, {'listaDistritos': listaDistritosUnicos,
                                        'aparcamientos': listaAparcamientos,
                                        'distrito': distrito,
                                        'seleccionados': listaSeleccionados})

    return HttpResponse(plantilla.render(contexto))


@csrf_exempt
def pagAparcamiento(request, idEntidad):
    if request.method == "GET":
        try:
            aparcamiento = Aparcamiento.objects.get(idEntidad=idEntidad)
        except Aparcamiento.DoesNotExist:
            plantilla = get_template('error.html')

            return HttpResponse(plantilla.render(), status=404)

    else:
        comentario = request.POST['texto']
        aparcamiento = Aparcamiento.objects.get(idEntidad=idEntidad)
        nuevoComentario = Comentario(texto=comentario,
                                     aparcamiento=aparcamiento)
        nuevoComentario.save()

    plantilla = get_template('pag_aparcamiento.html')
    comentarios = Comentario.objects.filter(aparcamiento=aparcamiento)
    contexto = RequestContext(request, {'aparcamiento': aparcamiento,
                              'comentarios': comentarios})

    return HttpResponse(plantilla.render(contexto))


def xml(request, nombreUsuario):
    try:
        usuario = User.objects.get(username=nombreUsuario)
    except User.DoesNotExist:
        plantilla = get_template('error.html')

        return HttpResponse(plantilla.render(), status=404)

    plantilla = get_template('xml/canal_usuario.xml')
    seleccionados = Seleccione.objects.filter(usuario=usuario)
    contexto = RequestContext(request, {'usuario': usuario,
                              'seleccionados': seleccionados})

    return HttpResponse(plantilla.render(contexto), content_type="text/xml")


def about(request):
    plantilla = get_template('about.html')
    contexto = RequestContext(request)

    return HttpResponse(plantilla.render(contexto))
