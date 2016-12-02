from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Usuario, Pregunta_Opcion, Opcion_Pregunta, Respuesta, Respuesta_Opcion, Categoria
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Permission
from django.utils import timezone
from datetime import datetime, date
from django import forms
from itertools import chain
from .forms import Userform, PreguntaOpcionForm, PreguntaForm
# Create your views here.


def index_view(request):
    queryset_list = Post.objects.all().order_by('creado')
    paginator = Paginator(queryset_list, 3)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
        context = {
            "object_list": queryset
        }
    return render(request, 'voto/index.html', context)

class signup(FormView):
    template_name='voto/signup.html'
    form_class = Userform
    success_url = reverse_lazy('index_view')

    def form_valid(self,form):
        user = form.save()
        p = Usuario()
        p.user_perfil = user
        p.email = form.cleaned_data['email']
        p.name = form.cleaned_data['name']
        p.last = form.cleaned_data['last']
        p.save()
        return super(signup,self).form_valid(form)

def admin(request):
    return render(request, 'voto/Admin.html')

class Crear_Categoria(ListView):
    template_name = 'voto/CrearCategoria.html'
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('admin_panel')

def pregunta_detalle(request, id=None):
    pregunta = get_object_or_404(Pregunta, ID_Pregunta=id)
    context = {
        "pregunta": pregunta,
    }
    return render(request, "voto/pregunta_detalle.html", context)

def pregunta_lista(request):
    queryset1 = Pregunta_Opcion.objects.all()
    queryset2 = Pregunta_Abierta.objects.all()
    paginator = paginator(queryset_list, 3)

    result_list = sorted(
    chain(queryset1, queryset2),
    key=attrgetter('-fecha_creacion'))

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset
    }
    return render(request, "voto/pregunta_lista.html")

def PreguntaAdmin(request):
    return render(request, "voto/preguntaadmin.html")

class Crear_Pregunta_Opcion(FormView):
    template_name = 'voto/Crear_Pregunta_Opcion.html'
    form_class = PreguntaOpcionForm
    #success_url = reverse_lazy('pregunta_lista')

    def form_valid(self,form):
        p = Pregunta_Opcion()
        p.pregunta = form.cleaned_data['pregunta']
        p.categoria = form.cleaned_data['categoria']
        #p.fecha_creacion = date.today()
        p.publicado = form.cleaned_data['publicado']
        p.ID_Usuario = form.cleaned_data['ID_Usuario']
        p.save()
        return super(Crear_Pregunta_Opcion, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(Crear_Pregunta_Opcion, self).get_context_data(**kwargs)
        ctx['Categoria'] = Categoria.objects.all()
        ctx['Usuario'] = Usuario.objects.all()
        return ctx

class Crear_Pregunta_Abierta(FormView):
    template_name = 'voto/Crear_Pregunta_Abierta.html'
    form_class = PreguntaAbiertaForm
    success_url = reverse_lazy('pregunta_lista')

    def form_valid(self,form):
        p = Pregunta_Abierta()
        p.pregunta = form.cleaned_data['pregunta']
        p.categoria = form.cleaned_data['categoria']
        p.fecha_creacion = date.today()
        p.publicado = form.cleaned_data['publicado']
        p.ID_Usuario = form.cleaned_data['ID_Usuario']
        p.save()
        return super(Crear_Pregunta_Opcion, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(Crear_Pregunta_Opcion, self).get_context_data(**kwargs)
        ctx['Categoria'] = Categoria.objects.all()
        ctx['Usuario'] = Usuario.objects.all()
        return ctx

class PreguntaView(generic.ListView):
    template_name = 'voto/index.html'
    context_object_name = 'Pregunta_Opcion_list'
    model = Pregunta_Opcion

    def get_queryset(self):
        return Pregunta_Opcion.objects.order_by('fecha_creacion')

class PreguntaView(generic.ListView):
    template_name = 'voto/index.html'
    context_object_name = 'Pregunta_Abierta_list'

    def get_queryset(self):
        return Pregunta_Abierta.objects.order-by('fecha_creacion')


def buscar2(request):
    if request.POST:
        data = request.POST['campo']
        p = PreguntaOpcion.objects.filter(pregunta=data)
        p = Pregunta_Abierta.objects.filter(pregunta=data)
        ctx = {'objects': p}
    else:
        ctx = {'mensaje':'no hay datos'}
    return render (request, 'voto/buscar2.html', ctx)

def borrar_pregunta(request, id=None):
    pregunta = get_object_or_404(Pregunta_Opcion, ID_Pregunta_Opcion=id)
    pregunta2 = get_object_or_404(Pregunta_Abierta, ID_Pregunta_Abierta=id)
    pregunta.delete()
    pregunta2.delete()
    return redirect('pregunta_lista')

def actualizar_pregunta(request, id):
    pregunta = get_object_or_404(Pregunta_Opcion, ID_Pregunta_Opcion=id)
    form = PreguntaForm(request.POST or None, request.FILES or None, instance=pregunta)
    if form.is_valid():
		try:
			pregunta = form.save()
			pregunta.save()
			context = {
				"pregunta":pregunta,
			}
			return render(request, "voto/pregunta_detalle.html", context)
		except:
			print "Un error"
    context = {
		"object_list": "eee",
		"pregunta": pregunta,
		"form":form,
		"Categoria": Categoria.objects.all()
	}
    return render(request, "voto/actualizar_pregunta.html", context)
