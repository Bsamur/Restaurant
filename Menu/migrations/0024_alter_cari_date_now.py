# Generated by Django 4.1.3 on 2023-02-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0023_alter_cari_ciro_alter_cari_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cari',
            name='date_now',
            field=models.DateField(auto_now_add=True, db_index=True, null=True, unique=True, verbose_name='Tarih'),
        ),
    ]
