# Generated by Django 4.1 on 2022-08-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lei', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='nome',
            field=models.TextField(),
        ),
    ]