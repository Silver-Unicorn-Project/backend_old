# Generated by Django 4.2 on 2023-06-12 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productreview_options_productreview_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='score',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1'), django.core.validators.MaxValueValidator(10, 'Максимум 10')], verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]
