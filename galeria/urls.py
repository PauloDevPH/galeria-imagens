from django.urls import path
from .views import (
    ImagemListView,
    ImagemCreateView,
    ImagemUpdateView,
    ImagemDeleteView,
)

urlpatterns = [
    path('', ImagemListView.as_view(), name='lista_imagens'),
    path('nova/', ImagemCreateView.as_view(), name='criar_imagem'),
    path('editar/<int:pk>/', ImagemUpdateView.as_view(), name='editar_imagem'),
    path('deletar/<int:pk>/', ImagemDeleteView.as_view(), name='deletar_imagem'),
]