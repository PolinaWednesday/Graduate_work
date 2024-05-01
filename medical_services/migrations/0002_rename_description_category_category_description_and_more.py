# Generated by Django 5.0.4 on 2024-04-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='category_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='category_image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category_title',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='description',
            new_name='services_description',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='image',
            new_name='services_image',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='services_title',
        ),
        migrations.AlterField(
            model_name='service',
            name='deadline',
            field=models.CharField(max_length=100, verbose_name='срок выполнения'),
        ),
    ]
