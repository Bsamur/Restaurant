# Generated by Django 4.1.3 on 2023-02-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0020_shopper_date_now_shopper_finished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='time_now',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
