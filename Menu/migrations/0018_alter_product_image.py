# Generated by Django 4.1.3 on 2023-02-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0017_alter_product_productaci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Fotoğraf'),
        ),
    ]
