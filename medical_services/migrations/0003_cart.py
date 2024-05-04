# Generated by Django 5.0.4 on 2024-05-04 05:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_services', '0002_rename_description_category_category_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='дата и время')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='клиент')),
                ('services', models.ManyToManyField(to='medical_services.service', verbose_name='услуги')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
            },
        ),
    ]
