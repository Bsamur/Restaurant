# Generated by Django 4.1.3 on 2023-02-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0021_shopper_time_now'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciro', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ciro')),
                ('date_now', models.DateField(auto_now_add=True, null=True, verbose_name='Sipariş Tarihi')),
                ('time_now', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
