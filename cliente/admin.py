from django.contrib import admin
from .models import *
from .urls import *

# Register your models here.
admin.site.register(Dcliente)
admin.site.register(Dfactoring)
admin.site.register(Dpessoas)
admin.site.register(Dcontratomae)
admin.site.register(Dsimulacao)
admin.site.register(Doperacao)
admin.site.register(Dcarteira)
