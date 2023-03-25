from django.forms import ModelForm
from .models import Postagem


class FormularioPostagem(ModelForm):

    class Meta:
        model = Postagem
        fields = ['titulo', 'conteudo', 'clube_futebol', 'jogador_favorito']
        