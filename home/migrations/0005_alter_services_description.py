# Generated by Django 5.1.1 on 2024-09-08 13:19

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_services_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
    ]
