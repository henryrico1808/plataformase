from django.urls import path
from . import views
from . import views

#app_name="visitante"

urlpatterns = [
    path('', views.index, name='index'),
    path('notificacionsc/validar/signuprv/', views.regUser, name='signuprv'),
    path('menuinstitucion/', views.menuinstitucion, name='menuinstitucion'),
    path('menuparticular/', views.menuparticular, name='menuparticular'),
    path('menuadmin/', views.menuadmin, name='menuadmin'),
    path('menudepartamento/', views.menudepartamento, name='menudepartamento'),
    path('control/', views.control, name='control'),
    path('menuvisitante/', views.menuvisitante, name='menuvisitante'),
     path('cuentavisitante/', views.cuentavisitante, name='cuentavisitante'),
     path('perfiluser/', views.perfiluser, name='perfiluser'),
     path('actualizarperfilusr/', views.actualizarperfilusr, name='actualizarperfilusr'),
     path('notificacion/', views.notificacion, name='notificacion'),
     path('notificaciones/', views.notificacionadmon, name='notificacionadmon'),
     path('solicitudcuenta/', views.regVisit, name='solicitudcuenta'),
     path('solicitudenviada/', views.modal, name='solicitudenviada'),
     path('notificacionsc/', views.notificacionsc, name='notificacionsc'),
     path('notificacionsc/validar/<email>/',views.validar, name='validar'),
     path('notificacionsc/validar/<email2>/cancelarsolicitud/<email>',views.cancelarsolicitud, name='cancelarsolicitud'),
<<<<<<< HEAD
    #  path('signuprv/',views.regUser, name='signuprv'),
    path('configuracionpdf/', views.configuracionpdf, name='configuracionpdf'),
    path('GuardarFormatoPDF/', views.GuardarFormatoPDF, name='GuardarFormatoPDF'),
        
=======
     path('signuprv/<email>',views.regUser, name='signuprv'),
    path('configuracionpdf/', views.configuracionpdf, name='configuracionpdf'),
    path('GuardarFormatoPDF/', views.GuardarFormatoPDF, name='GuardarFormatoPDF'),

    path('cct/', views.cct, name='cct'),
>>>>>>> 336c7c9c5b3edb1eb969590ceadded3e3d9095b1
]