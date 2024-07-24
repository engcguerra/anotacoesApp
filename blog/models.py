from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=300, null=True, blank=True)
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        if self.titulo is not None:
            return self.titulo
        else:
            return f"imagem: {self.imagem.url}"
