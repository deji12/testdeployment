# Generated by Django 4.1 on 2022-09-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lei', '0016_rename_datafim_calendario_data_fim_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendario',
            old_name='data_Fim',
            new_name='dataFim',
        ),
        migrations.RenameField(
            model_name='calendario',
            old_name='data_Inicio',
            new_name='dataInicio',
        ),
    ]
