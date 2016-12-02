from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^$',index_view,name='index_view'),
	url(r'^signup/$',signup.as_view(),name='signup'),
	url(r'^admin/$',admin,name='admin'),
	url(r'^Crear_Categoria/$',Crear_Categoria.as_view(),name='Crear_Categoria'),
	url(r'^pregunta_detalle/$',pregunta_detalle,name='pregunta_detalle'),
	url(r'^pregunta_lista/$',pregunta_lista,name='pregunta_lista'),
	url(r'^PreguntaAdmin/$',PreguntaAdmin,name='PreguntaAdmin'),
	url(r'^Crear_Pregunta_Opcion/$',Crear_Pregunta_Opcion.as_view(),name='Crear_Pregunta_Opcion'),
	url(r'^Crear_Pregunta_Abierta/$',Crear_Pregunta_Abierta.as_view(),name='Crear_Pregunta_Abierta'),
	url(r'^PreguntaView/$',PreguntaView.as_view(),name='PreguntaView'),
	url(r'^buscar2/$',buscar2,name='buscar2'),
	url(r'^borrar_pregunta/$',name='borrar_pregunta'),
	url(r'^actualizar_pregunta/$',actualizar_pregunta,name='actualizar_pregunta'),

]