# Generated by Django 4.2.2 on 2023-06-13 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_alter_adestramento_ade_raca_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adestramento',
            name='age_codigo',
        ),
        migrations.RemoveField(
            model_name='banhoetosa',
            name='age_codigo',
        ),
        migrations.RemoveField(
            model_name='consultas',
            name='age_codigo',
        ),
    ]
