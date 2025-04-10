# Generated by Django 4.1.7 on 2023-05-31 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_remove_feedback_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('link', models.CharField(max_length=200, unique=True, verbose_name='Ссылка')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
                ('status', models.IntegerField(choices=[(0, 'Главные документы'), (1, 'Стандарты внешнего муниципального финансового контроля'), (2, 'Методические материалы'), (3, 'Нормативные правовые акты')], default=0, verbose_name='Тип документа')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=False, upload_to='images', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Слог'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Доступ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Загружено'),
        ),
    ]
