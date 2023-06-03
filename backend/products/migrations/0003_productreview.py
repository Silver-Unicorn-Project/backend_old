# Generated by Django 4.2 on 2023-06-03 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите свой отзыв', verbose_name='Текст отзыва')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')),
                ('author', models.ForeignKey(help_text='Автор', on_delete=django.db.models.deletion.CASCADE, related_name='productreviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(help_text='Оставьте свой отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='productreviews', to='products.products', verbose_name='Отзывы')),
            ],
        ),
    ]
