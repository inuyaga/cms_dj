from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    # pass (para no declarar nada)
    image_profile = models.ImageField(upload_to="perfiles", verbose_name="Imagen de perfil")
    class Meta:
        db_table = 'auth_user' 