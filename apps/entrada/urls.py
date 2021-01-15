from django.conf.urls import url
from apps.entrada.views import inicio

urlpatterns = [
    url(r'^index$', inicio)
]