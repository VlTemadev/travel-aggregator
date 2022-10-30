from django.db import models
from datetime import datetime
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model): 
    postImage = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField('Заголовок', max_length=40)
    content = models.TextField("Описание")
    source = models.CharField("Источник", max_length=50)
    postDate = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=150)
    buyUrl = models.TextField(max_length=150, null=True, blank=True,)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postDetail", args=[self.pk])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title

