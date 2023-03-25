from django.db import models


class Postagem(models.Model):
    titulo = models.CharField(max_length=80)

    conteudo = models.TextField()

    data_publicacao = models.DateField(auto_now_add=True)
    
    clube_futebol = models.CharField(max_length=80)

    jogador_favorito = models.CharField(max_length=80)

    def __str__(self):
        return self.titulo