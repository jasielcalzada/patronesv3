from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Pregunta_Opcion, Opcion_Pregunta, Respuesta, Respuesta_Opcion, Categoria


class Userform(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'Email'}))
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Nombre'}))
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Apellido'}))
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Nombre Usuario'}))
	password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Contrasena'}))
	password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Confirmacion Contrasena'}))
	is_superuser = forms.BooleanField(required = False, widget=forms.widgets.CheckboxInput())

	class Meta:
		model = User
		fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_superuser']

class PreguntaOpcionForm(forms.ModelForm):
	opcion = forms.CharField(max_length=64)
	descripcion = forms.CharField(max_length=64)
	ID_Pregunta_Opcion = forms.CharField(max_length=64)

	class Meta:
		model = Opcion_Pregunta
        fields = '__all__'

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta_Opcion,Pregunta_Abierta
        fields = '__all__'
        #exclude = ['fecha_creacion']