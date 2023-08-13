from django.db import models
from django.contrib.auth.models import AbstractUser

# funcion para la carga de imagenes del user
# def upload_image(instance, filename):
#     return 'img/users/{id}/{filename}'.format(id=instance.pk, filename=filename)

# Create your models here.
class User(AbstractUser):
    TIPODOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadania'),
        ('CE', 'Cedula Extranjeria'),
        ('TI', 'Tarjeta Identidad'),
        ('PA', 'Passaporte'),
        ('RC', 'Registro Civil'),
        ('OTRO', 'Otro')        
    ]
    # sobre escritura campo username
    email = models.EmailField(max_length=40, verbose_name='Correo Electronico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    tipo_id = models.CharField(max_length=20, verbose_name='Tipo Identificacion', choices=TIPODOCUMENTO_CHOICES, blank=True)
    identificacion = models.CharField(max_length=20, verbose_name='Numero de Identificacion')
    # photo = models.ImageField(verbose_name='Foto del Perfil', upload_to=upload_image, null=True, blank=True)
    country=models.CharField(verbose_name='Pais Origen', max_length=255)
    city=models.CharField(verbose_name='Ciudad', max_length=255)
    addres=models.CharField(verbose_name='Direccion', max_length=255)
    phone=models.CharField(verbose_name='Telefono', max_length=255)
    birthday=models.DateField(verbose_name='Fecha Nacimiento', max_length=255, null=True, blank=True)
    ocupation_job=models.CharField(verbose_name='Ocupacion', max_length=255)
    relocate=models.BooleanField(verbose_name='Reubicacion', max_length=255, default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
