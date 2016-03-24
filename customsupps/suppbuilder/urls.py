from django.conf.urls import url

from .views import (endurance,strength,energy)

urlpatterns = [
    url(r'^endurance/$', "suppbuilder.views.endurance"),
    url(r'^strength/$', "suppbuilder.views.strength"),
    url(r'^energy/$', "suppbuilder.views.energy"),
]