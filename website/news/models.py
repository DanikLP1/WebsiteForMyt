from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.urls import reverse
import os


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

TYPE = (
    (0, "Главные документы"),
    (1, "Стандарты внешнего муниципального финансового контроля"),
    (2, "Методические материалы"),
    (3, "Нормативные правовые акты")
)

TYPE_2 = (
    (0, 'Годовой отчет'),
    (1, 'Контрольные мероприятия'),
    (2, 'Экспертно-аналитические мероприятия'),
    (3, 'Коллегия'),
    (4, 'Информация о заключенных соглашениях'),
    (5, 'Официальные выступления и заявления'),
    (6, 'Сведения о внесенных мероприятиях'),
    (7, 'Сведения о принятых решениях'),
    (8, 'План работы КСП'),
    (9, 'Публикации в СМИ'),
    (10, 'План внутреннего финансового аудита'),
)

TYPE_3 = (
    (0, 'Сведения о доходах и имуществе'),
    (1, 'Методические материалы'),
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слог')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts', verbose_name='Автор')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Загружено')
    content = models.TextField(verbose_name='Описание')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='Доступ')
    cover = models.ImageField(upload_to='images', default=False, verbose_name='Картинка')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_my_model_name(self):
        return self._meta.model_name

class FeedBack(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема')
    email = models.EmailField(max_length=200, verbose_name='Email')
    content = models.TextField(verbose_name='Содержимое')
    answer = models.TextField(verbose_name='Ответ', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    ip_address = models.GenericIPAddressField(verbose_name='IP Адрес', blank=True, null=True)

    def get_my_model_name(self):
        return self._meta.model_name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ('-created_at',)
        db_table = 'app-feedback'
    
    def __str__(self):
        return f'Вам письмо: {self.email}'

class Documents(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name='Название')
    document = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Документ', blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата')
    status = models.IntegerField(choices=TYPE, default=0, verbose_name='Тип документа')

    def get_absolute_url(self):
        return self.document.url if self.document else None
    
    def get_my_model_name(self):
        return self._meta.model_name

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Документ: {self.title}'
    
    
    def file_exists(self):
        if self.document:
            return os.path.exists(self.document.path)
        return False
    
class Activities(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name='Название')
    document = models.FileField(upload_to='activities/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Документ', blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата')
    status = models.IntegerField(choices=TYPE_2, default=0, verbose_name='Тип документа')

    def get_absolute_url(self):
        return self.document.url
    
    def get_my_model_name(self):
        return self._meta.model_name

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
        ordering = ['-created_at']

    def __str__(self):
        return f'Документ: {self.title}'
    
class Anti_corrupsion(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    document = models.FileField(upload_to='anti-corruption/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Документ', blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата')
    status = models.IntegerField(choices=TYPE_3, default=0, verbose_name='Тип документа')

    def get_absolute_url(self):
        return self.document.url

    def get_my_model_name(self):
        return self._meta.model_name
    
    class Meta:
        verbose_name = 'Противодействие коррупции'
        verbose_name_plural = 'Противодействие коррупции'
        ordering = ['-created_at']

    def __str__(self):
        return f'Документ: {self.title}'
    
class Plans(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    document = models.FileField(upload_to='plans/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Документ', blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата')

    def get_absolute_url(self):
        return self.document.url

    def get_my_model_name(self):
        return self._meta.model_name
    
    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'План'
        ordering = ['-created_at']

    def __str__(self):
        return f'Документ: {self.title}'
    
class Examinations(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    document = models.FileField(upload_to='examinations/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Документ', blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата')

    def get_absolute_url(self):
        return self.document.url

    def get_my_model_name(self):
        return self._meta.model_name
    
    class Meta:
        verbose_name = 'Экспертизы'
        verbose_name_plural = 'Экспертизы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Документ: {self.title}'