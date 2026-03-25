from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Imagem, Categoria
from .forms import ImagemForm


class ImagemListView(ListView):
    model = Imagem
    template_name = 'galeria/imagem_list.html'
    context_object_name = 'imagens'

    def get_queryset(self):
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            return Imagem.objects.filter(categoria_id=categoria_id)
        return Imagem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            context['categoria_ativa'] = Categoria.objects.filter(id=categoria_id).first()
        else:
            context['categoria_ativa'] = None
        return context


class ImagemCreateView(CreateView):
    model = Imagem
    form_class = ImagemForm
    template_name = 'galeria/form_imagem.html'
    success_url = reverse_lazy('lista_imagens')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Imagem'
        return context


class ImagemUpdateView(UpdateView):
    model = Imagem
    form_class = ImagemForm
    template_name = 'galeria/form_imagem.html'
    success_url = reverse_lazy('lista_imagens')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Imagem'
        return context


class ImagemDeleteView(DeleteView):
    model = Imagem
    template_name = 'galeria/confirmar_delete.html'
    context_object_name = 'imagem'
    success_url = reverse_lazy('lista_imagens')