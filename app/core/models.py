from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    permiso = models.CharField(max_length=40,null=True, verbose_name="permiso")


class Principal(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    titulo= models.CharField(max_length=40, verbose_name="titulo pagina",null=False)
    nombre_programador = models.CharField(max_length=40, null=False, verbose_name="Nombre Developer")
    descripcion_corta = models.CharField(max_length=40, null=False, verbose_name="Descripción")
    video_url = models.CharField(max_length=140, null=False, verbose_name="Presentación")
    primer_boton = models.CharField(max_length=40, null=False, verbose_name="Botón 1")
    segundo_boton = models.CharField(max_length=40, null=False, verbose_name="Botón 2")

class Redes(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    icono= models.CharField(max_length=140, verbose_name="Icono",null=False)
    url = models.CharField(max_length=140, null=False, verbose_name="Url")
    red_social = models.CharField(max_length=140, null=False, verbose_name="red social")

class Sobre_mi(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    primer_titulo= models.CharField(max_length=140, verbose_name="titulo",null=False)
    contenido_principal = models.CharField(max_length=1000, null=False, verbose_name="contenido")
    tercer_contenido = models.CharField(max_length=1000, null=False, verbose_name="tercer contenido")
    titulo_uno = models.CharField(max_length=1000, null=False, verbose_name="titulo 1")
    uno = models.CharField(max_length=1000, null=False, verbose_name="contenido 1")
    titulo_dos = models.CharField(max_length=1000, null=False, verbose_name="titulo 2")
    dos = models.CharField(max_length=1000, null=False, verbose_name="contenido 2")
    titulo_tres = models.CharField(max_length=1000, null=False, verbose_name="titulo 3")
    tres = models.CharField(max_length=1000, null=False, verbose_name="contenido 3")
    titulo_cuatro = models.CharField(max_length=1000, null=False, verbose_name="titulo 4")
    cuatro = models.CharField(max_length=1000, null=False, verbose_name="contenido 4")


class Header(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    header_titulo = models.CharField(max_length=140, verbose_name="Titulo",null=False)
    header_contenido = models.CharField(max_length=500, null=False, verbose_name="contenido")
    
class Header_items(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    link = models.CharField(max_length=140, verbose_name="link",null=False)
    texto = models.CharField(max_length=500, null=False, verbose_name="texto")
    id_dos = models.IntegerField(verbose_name="id", null=True)

class Habilidades(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    titulo = models.CharField(max_length=140, verbose_name="titulo",null=False)
    contenido = models.CharField(max_length=500, null=False, verbose_name="contenido")
    skill_titulo = models.CharField(max_length=500, null=True, verbose_name="titulo_contenido")

class Habilidades_items(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    lenguaje = models.CharField(max_length=140, verbose_name="lenguaje",null=False)
    porcentaje = models.CharField(max_length=50, null=False, verbose_name="porcentaje")

class Trabajos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    titulo = models.CharField(max_length=140, verbose_name="titulo",null=False)
    texto = models.CharField(max_length=500, null=False, verbose_name="texto")   

class Trabajos_items(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    id_dos = models.IntegerField(verbose_name="titulo",null=False)
    titulo = models.CharField(max_length=140, verbose_name="titulo",null=False)
    titulo_dos = models.CharField(max_length=140, verbose_name="titulo",null=False)
    contenido = models.CharField(max_length=500, null=False, verbose_name="contenido")
    url = models.CharField(max_length=500, null=False, verbose_name="url")
    nombre_imagen = models.CharField(max_length=140, verbose_name="titulo",null=True)
    url_proyecto = models.CharField(max_length=200, verbose_name="titulo",null=True)

class Contacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    titulo = models.CharField(max_length=140, verbose_name="titulo",null=False)
    titulo_dos = models.CharField(max_length=140, verbose_name="titulo",null=False)
    titulo_tres = models.CharField(max_length=140, verbose_name="titulo",null=False)
    email = models.CharField(max_length=500, null=False, verbose_name="contenido")
    
class Idioma(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    idioma = models.CharField(max_length=140, verbose_name="idioma",null=False)

class Faltante(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    ver_video = models.CharField(max_length=140, verbose_name="video",null=False)
    volver = models.CharField(max_length=140, verbose_name="back",null=False)
    diseno = models.CharField(max_length=140, verbose_name="diseño",null=False)


class Visitas(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    ip = models.CharField(max_length=140, verbose_name="video",null=False)
    fecha = models.DateField()
    pais = models.CharField(max_length=140, verbose_name="video",null=True)

class Country(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id", null=False)
    countrycode = models.CharField(max_length=140, verbose_name="countrycode",null=False)
    countryname = models.CharField(max_length=140, verbose_name="countryname",null=False)
    code = models.CharField(max_length=140, verbose_name="code",null=True)