# Generated by Django 4.1.3 on 2023-02-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0018_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Toplam Tutar'),
        ),
    ]
