# Generated by Django 4.1.3 on 2023-02-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=255, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.BooleanField(default=False, verbose_name='Kampanya var mı?'),
        ),
    ]
