# Generated by Django 4.1 on 2022-09-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
