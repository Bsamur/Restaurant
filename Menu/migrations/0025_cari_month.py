# Generated by Django 4.1.3 on 2023-02-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0024_alter_cari_date_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='cari',
            name='month',
            field=models.IntegerField(default=2, verbose_name='Ay'),
        ),
    ]
