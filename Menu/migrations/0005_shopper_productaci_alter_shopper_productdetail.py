# Generated by Django 4.1.3 on 2023-02-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_remove_bill_productdetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='productaci',
            field=models.BooleanField(default=False, verbose_name='Acılı var mı ?'),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='productdetail',
            field=models.CharField(max_length=255, verbose_name='Ürün detayı'),
        ),
    ]