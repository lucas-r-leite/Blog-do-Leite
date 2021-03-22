from django.db import models
from django.utils.text import slugify #Biblioteca necessária para gerar as slugs automaticamente
from ckeditor.fields import RichTextField
# Create your models here.
#O Django cria um id automatico no banco de dados

class Post(models.Model):
    title = models.CharField('Título',max_length=150, blank=False, null=False)

    resume = models.TextField(default='')

    content = RichTextField()
    #content = models.TextField('Conteúdo', blank=False, null=False)
    date_published = models.DateTimeField('Data de publicação', auto_now=True) #Auto_now_add é utilizado para salvar as datas de modificações
    slug = models.SlugField('Slug', editable=False)#url baseada no título

    def __str__(self): 
        return self.title #Melhora a vizualização no banco de dados. Mostra o titulo

    def save(self, *args, **kwargs):#Cria a slug automaticamente
        value = self.title #salva o titulo na variável
        self.slug = slugify(value, allow_unicode=True) #Cria o slug a partir do título
        '''
        if(Post.objects.filter(slug = self.slug)
            self.slug += '--1'
        '''
        super().save(*args, **kwargs) #Segue o caminho normal após salvar