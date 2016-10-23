from django.shortcuts import render
from apps.seguimiento.forms import *
from apps.seguimiento.models import *
from apps.personal.models import designacion

from django.http import HttpResponseRedirect

# Create your views here. D:\Maritza-2012\PUNA-Proy Ecoturistico Thalaqocha\A-PROPUESTA\1-TDRs

from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

# crear proyecto
class crearProyecto(CreateView):
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')

# lista proyectos
class listaProyectos(CreateView,ListView):
	model = proyecto
	form_class = searchForm
	template_name = 'seguimiento/listaproyecto.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaProyectos, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.all().order_by('id')
		return object_list
# crea un item para un proyecto en especifico
class crearItem(CreateView):
	model_pk = proyecto
	form_class = crearItemsForm
	template_name = 'seguimiento/nuevoitem.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.proyecto = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateItem(UpdateView):
	model =item
	form_class = crearItemsForm
	template_name = 'seguimiento/nuevoitem.html'
	success_url = 'seguimiento:listaitems'
	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs = {'pk': self.get_object().proyecto.pk})

# lista los items de un proyecto en espesifico
class listaItems(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'seguimiento/listaitems.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaItems, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			context['form'] = self.form_class()
			context['pk1'] = pk1
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id, proyecto = pk1)
		else:
			object_list = self.model.objects.filter(proyecto = pk1).order_by('id')
		return object_list

class updateProyecto(UpdateView):
	model = proyecto
	form_class = crearProyectoForm
	template_name = 'seguimiento/nuevoproyecto.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateProyecto, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			import datetime
			ins = self.model.objects.get(pk=pk1)
			print(ins.fecha_inicio)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			
			context['form'] = self.form_class(instance=ins, initial={'fecha':str(ins.fecha_inicio)})
		return context

class listaPersonalProyecto(CreateView,ListView):
	model = designacion
	form_class = searchForm
	template_name = 'seguimiento/listapersonalpro.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPersonalProyecto, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(proyecto = proyecto.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(proyecto = proyecto.objects.filter(id=pk1)).order_by('id')
		return object_list

class peticionMaterial(CreateView):
	model_pk = item
	form_class = crearPeticionMaterialForm
	template_name = 'seguimiento/peticionmaterial.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionMaterial(UpdateView):
	model = peticion_materiales
	form_class = crearPeticionMaterialForm
	template_name = 'seguimiento/peticionmaterial.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionMaterial, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaPeticionMaterial(CreateView,ListView):
	model = peticion_materiales
	form_class = searchForm
	template_name = 'seguimiento/listamaterialalmacen.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPeticionMaterial, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class peticionInsumos(CreateView):
	model_pk = item
	form_class = crearPeticionInsumosForm
	template_name = 'seguimiento/peticioninsumos.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionInsumos(UpdateView):
	model = peticion_insumos
	form_class = crearPeticionInsumosForm
	template_name = 'seguimiento/peticioninsumos.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionInsumos, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaPeticionInsumos(CreateView,ListView):
	model = peticion_insumos
	form_class = searchForm
	template_name = 'seguimiento/listainsumosalmacen.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaPeticionInsumos, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoPersonal(CreateView):
	model_pk = item
	form_class = crearRequerimientoPersonalForm
	template_name = 'seguimiento/requerimientopersonal.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoPersonal(UpdateView):
	model = requerimiento_personal
	form_class = crearRequerimientoPersonalForm
	template_name = 'seguimiento/requerimientopersonal.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoPersonal, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoPersonal(CreateView,ListView):
	model = requerimiento_personal
	form_class = searchForm
	template_name = 'seguimiento/listarequerimientopersonal.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoPersonal, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoMaHe(CreateView):
	model_pk = item
	form_class = crearRequerimientoMaHeForm
	template_name = 'seguimiento/requerimientomahe.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoMaHe(UpdateView):
	model = requerimiento_maq_he
	form_class = crearRequerimientoMaHeForm
	template_name = 'seguimiento/requerimientomahe.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoMaHe, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoMaHe(CreateView,ListView):
	model = requerimiento_maq_he
	form_class = searchForm
	template_name = 'seguimiento/listaRequerimientomahe.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoMaHe, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class requerimientoMaterialesLocales(CreateView):
	model_pk = item
	form_class = crearRequerimientoMaterialLocalForm
	template_name = 'seguimiento/requerimientomaterlocal.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateRequerimientoMaterialesLocales(UpdateView):
	model = materiales_locales
	form_class = crearRequerimientoMaterialLocalForm
	template_name = 'seguimiento/requerimientomaterlocal.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateRequerimientoMaterialesLocales, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoMaterialeLocales(CreateView,ListView):
	model = materiales_locales
	form_class = searchForm
	template_name = 'seguimiento/listaRequerimientomaterialelocales.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoMaterialeLocales, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list


class requerimientoHerramientas(CreateView):
	model_pk = item
	form_class = crearPeticionHerramientas
	template_name = 'seguimiento/requerimientoherramientas.html'
	success_url = 'seguimiento:listaitems'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': self.model_pk.objects.get(id=pk1).proyecto.id}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updatePeticionHerramientas(UpdateView):
	model = peticion_Herramientas
	form_class = crearPeticionHerramientas
	template_name = 'seguimiento/requerimientoherramientas.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updatePeticionHerramientas, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class listaRequerimientoHerramientas(CreateView,ListView):
	model = peticion_Herramientas
	form_class = searchForm
	template_name = 'seguimiento/listapeticionherramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaRequerimientoHerramientas, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class crearInforme(CreateView):
	model_pk = item
	form_class = crearReportesAvanceForm
	template_name = 'seguimiento/crearinforme.html'
	success_url = 'seguimiento:informefotografico'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form = form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.save()
			#print (form)
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': form.pk }))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class updateCrearInforme(UpdateView):
	model = reportes_avance
	form_class = crearReportesAvanceForm
	template_name = 'seguimiento/crearinforme.html'
	success_url = reverse_lazy('seguimiento:listaproyectos')
	def get_context_data(self, **kwargs):
		context = super (updateCrearInforme, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			ins = self.model.objects.get(pk=pk1)
			#print(datetime.datetime.strptime(str(ins.fecha_inicio), '%Y-%m-%d').strftime('%d-%m-%Y'))
			context['form'] = self.form_class(instance=ins)
		return context

class crearInformeFotografico(CreateView):
	model_pk = reportes_avance
	form_class = crearFotosReporteForm
	template_name = 'seguimiento/crearinformefotografico.html'
	success_url = 'seguimiento:informefotografico'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.reportes_avance = self.model_pk.objects.get(id=pk1)
			form.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1 }))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaInformes(CreateView,ListView):
	model = reportes_avance
	form_class = searchForm
	template_name = 'seguimiento/listapeInformes.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaInformes, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk1=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1), id = id)
		else:
			object_list = self.model.objects.filter(item = item.objects.filter(id=pk1)).order_by('id')
		return object_list

class listaInformesFotos(ListView):
	model = reporte_fotografico
	template_name = 'seguimiento/listainformefotos.html'
	paginate_by = 10

	def get_queryset(self):
		pk1=self.kwargs['pk']
		print(pk1)
		object_list = self.model.objects.filter(reportes_avance = reportes_avance.objects.filter(id=pk1))
		return object_list