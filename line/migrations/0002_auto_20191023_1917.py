# Generated by Django 2.2.6 on 2019-10-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='line_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='line',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]