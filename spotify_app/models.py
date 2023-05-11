from django.db import models
from django.utils import timezone
from django.shortcuts import reverse 

class Post(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)
    slug = models.SlugField('Ссылка', max_length=150, unique=True)
    image = models.ImageField('Картинка', blank=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"

    def __str__(self):
        return self.title

# Create your models here.
