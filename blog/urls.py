from django.urls import path
from .views import home, create, leitura_postagem, update, delete


urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('post/<int:pk>/', leitura_postagem, name='leitura_postagem'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]
