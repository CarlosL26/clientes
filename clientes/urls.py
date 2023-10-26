from django.urls import path
from .views import index,listado,nueva,editor,contacto,clientespaginacion

urlpatterns = [
    path('', index, name='index'),
    path('listado/', listado, name='listado'),
    path('nueva/', nueva, name='nueva'),
    path('editar/<int:id>',editor,name='editor'),
    path('contacto/', contacto, name='contacto'),
    path('clientespaginacion/', clientespaginacion,name='clientespaginacion')
]
