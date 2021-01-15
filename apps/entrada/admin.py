from django.contrib import admin

# Register your models here.

from apps.entrada.models import Categoria, Post
admin.site.register(Categoria)
admin.site.register(Post)


