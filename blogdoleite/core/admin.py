from django.contrib import admin
from .models import Post #Importando a classe criada em models

# Register your models here.
admin.site.register(Post)