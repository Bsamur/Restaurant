# Generated by Django 4.1.3 on 2023-02-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to=None, verbose_name='Ürün Fotoğrafı'),
        ),
    ]