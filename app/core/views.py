from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .forms import UsuarioRegisterForm
from django.contrib import messages
from .models import *
from django.urls import reverse
import datetime
import urllib, json
from urllib.request import urlopen, Request
from django.db import connection


def addDays(days):
   newDate = datetime.date.today() + datetime.timedelta(days=days)
   return newDate

def idioma(request,id):
    url = reverse('index')
    html = HttpResponseRedirect(url)
    #html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('idioma', id, max_age = None)
    return html
    #return redirect(index)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    idioma = request.COOKIES.get('idioma')
    if idioma is None:
        idioma = 1
    principal = get_object_or_404(Principal, id = idioma)
    sobre_mi = get_object_or_404(Sobre_mi, id = idioma)
    header = get_object_or_404(Header, id = idioma)
    habilidades = get_object_or_404(Habilidades, id = idioma)
    trabajos = get_object_or_404(Trabajos, id = idioma)
    falta = get_object_or_404(Faltante, id = idioma)
    contacto = get_object_or_404(Contacto, id = idioma)
    redes = Redes.objects.all()
    habilidades_items = Habilidades_items.objects.all()
    trabajos_items = Trabajos_items.objects.filter(id_dos = idioma)
    header_items = Header_items.objects.filter(id_dos = idioma)
    hoy = addDays(0)
    ip_user = get_client_ip(request)
    if ip_user != '127.0.0.1':
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        url = "https://api.geoiplookup.net/?query=179.60.65.97&json=true"
        req = Request(url, headers=hdr)
        #url = "https://api.geoiplookup.net/?query=" + '179.60.65.97' + "&json=true"
        response = urlopen(req)
        data = json.loads(response.read())
        pais = data['countrycode']
    else:
        pais = 'CL'
    datos = Visitas.objects.filter(ip = ip_user)
    existe = Visitas.objects.filter(ip = ip_user, fecha = hoy).exists()
    if existe==False:
        visita = Visitas(ip = ip_user,fecha = hoy, pais = pais)
        visita.save()
    context = {'principal' : principal, 'redes' : redes,'sobre_mi' : sobre_mi, 'header' : header, 'headers_items' : header_items, 'habilidades' : habilidades, 'habilidades_items' : habilidades_items , 'trabajos' : trabajos, 'trabajos_items' : trabajos_items , 'contacto' : contacto, 'falta' : falta, 'pais' : pais }
    return render(request, 'core/index.html',context)

def login(request):
    return render(request, 'core/login.html')



def register(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario "{username}" se creo exitosamente')
    else:
        form = UsuarioRegisterForm()
    context = {'form' : form}
    return render(request, 'core/register.html',context)

def panel(request):
    hoy = addDays(0)
    ayer = addDays(-1)
    fecha_3 = addDays(-2)
    fecha_4 = addDays(-3)
    fecha_5 = addDays(-4)
    fecha_6 = addDays(-5)
    visitas_1 = Visitas.objects.filter(fecha = hoy).count()
    visitas_2 = Visitas.objects.filter(fecha = ayer).count()
    visitas_3 = Visitas.objects.filter(fecha = fecha_3).count()
    visitas_4 = Visitas.objects.filter(fecha = fecha_4).count()
    visitas_5 = Visitas.objects.filter(fecha = fecha_5).count()
    visitas_6 = Visitas.objects.filter(fecha = fecha_6).count()
    visitas = Visitas.objects.all().count()
    cursor = connection.cursor()
    cursor.execute("SELECT pais,count(pais) FROM core_visitas GROUP BY pais ORDER BY -count(pais)")
    result = cursor.fetchall()
    contador = 0
    nombre_pais_1 = "No existe";
    visitas_pais_1 = 0
    porcentaje_1 = 0
    codigo_1 = "cl"
    nombre_pais_2 = "No existe";
    visitas_pais_2 = 0
    porcentaje_2 = 0
    codigo_2 = "cl"
    nombre_pais_3 = "No existe";
    visitas_pais_3 = 0
    porcentaje_3 = 0
    codigo_3 = "cl"
    nombre_pais_4 = "No existe";
    visitas_pais_4 = 0
    porcentaje_4 = 0
    codigo_4 = "cl"
    nombre_pais_5 = "No existe";
    visitas_pais_5 = 0
    porcentaje_5 = 0
    codigo_5 = "cl"
    nombre_pais_6 = "No existe";
    visitas_pais_6 = 0
    porcentaje_6 = 0
    codigo_6 = "cl"
    while contador <= 6:
        try:
            nombre = get_object_or_404(Country, code = result[contador][0])
        except:
            break
        if contador == 0:
            nombre_pais_1 = nombre.countryname
            visitas_pais_1 = result[contador][1]
            porcentaje_1 = round((100/visitas)*visitas_pais_1,2)
            codigo_1 = result[contador][0].lower()
        if contador == 1:
            nombre_pais_2 = nombre.countryname
            visitas_pais_2 = result[contador][1]
            porcentaje_2 = round((100/visitas)*visitas_pais_2,2)
            codigo_2 = result[contador][0].lower()
        if contador == 2:
            nombre_pais_3 = nombre.countryname
            visitas_pais_3 = result[contador][1]
            porcentaje_3 = round((100/visitas)*visitas_pais_3,2)
            codigo_3 = result[contador][0].lower()
        if contador == 3:
            nombre_pais_4 = nombre.countryname
            visitas_pais_4 = result[contador][1]
            porcentaje_4 = round((100/visitas)*visitas_pais_4,2)
            codigo_4 = result[contador][0].lower()
        if contador == 4:
            nombre_pais_5 = nombre.countryname
            visitas_pais_5 = result[contador][1]
            porcentaje_5 = round((100/visitas)*visitas_pais_5,2)
            codigo_5 = result[contador][0].lower()
        if contador == 5:
            nombre_pais_6 = nombre.countryname
            visitas_pais_6 = result[contador][1]
            porcentaje_6 = round((100/visitas)*visitas_pais_6,2)
            codigo_6 = result[contador][0].lower()
        contador += 1
    context = {'ante_ayer' : fecha_3 , 'visitas_1' : visitas_1,'visitas_2' : visitas_2,'visitas_3' : visitas_3,'visitas_4' : visitas_4,'visitas_5' : visitas_5,'visitas_6' : visitas_6,'fecha_4' : fecha_4, 'fecha_5' : fecha_5, 'fecha_6' : fecha_6, 'nombre_pais_1' : nombre_pais_1,'nombre_pais_2' : nombre_pais_2,'nombre_pais_3' : nombre_pais_3,'nombre_pais_4' : nombre_pais_4,'nombre_pais_5' : nombre_pais_5,'nombre_pais_6' : nombre_pais_6, 'visitas_pais_1' : visitas_pais_1,'visitas_pais_2' : visitas_pais_2,'visitas_pais_3' : visitas_pais_3,'visitas_pais_4' : visitas_pais_4,'visitas_pais_5' : visitas_pais_5,'visitas_pais_6' : visitas_pais_6, 'porcentaje_1' : porcentaje_1, 'porcentaje_2' : porcentaje_2, 'porcentaje_3' : porcentaje_3, 'porcentaje_4' : porcentaje_4, 'porcentaje_5' : porcentaje_5, 'porcentaje_6' : porcentaje_6 , 'codigo_1' : codigo_1, 'codigo_2' : codigo_2, 'codigo_3' : codigo_3, 'codigo_4' : codigo_4, 'codigo_5' : codigo_5, 'codigo_6' : codigo_6 }
    return render(request, 'core/admin.html', context)

def user(request):
    return render(request, 'core/user.html')

def chart(request):
    return render(request, 'core/chartjs.html')