# Generated by Django 2.0.4 on 2018-04-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_share', '0002_auto_20180414_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book/images', verbose_name='Imagem'),
        ),
    ]