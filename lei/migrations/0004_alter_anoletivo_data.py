# Generated by Django 4.1 on 2022-08-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lei', '0003_alter_docente_nome_alter_news_cabecalho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anoletivo',
            name='data',
            field=models.CharField(max_length=12),
        ),
    ]