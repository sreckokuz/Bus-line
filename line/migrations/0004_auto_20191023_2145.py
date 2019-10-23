# Generated by Django 2.2.6 on 2019-10-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0003_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='lat',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='station',
            name='lng',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
