# Generated by Django 4.2.2 on 2023-06-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cad_codigo',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logincadastro',
            name='lc_codigo',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
