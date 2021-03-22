from django.urls import path 
from . import views

#A estrutura de urls é como uma escada. O arquivo urls principal importa os arquivos urls dos apps e estes podem possuir outros caminhos urls.

app_name ='core' #Essa variável tem que ter o mesmo nome que foi declarado no namespace. A variável é opcional.

urlpatterns = [
   path('',views.index, name='index'),
   path('post/<int:id>/',views.detail, name='detail'),
]