# Generated by Django 4.2.7 on 2024-01-04 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_dcliente_cli_telefone1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dcliente',
            old_name='cli_complementoenderereco',
            new_name='cli_complementoendereco',
        ),
        migrations.RenameField(
            model_name='dcliente',
            old_name='cli_enderereco',
            new_name='cli_endereco',
        ),
        migrations.RenameField(
            model_name='dfactoring',
            old_name='fac_complementoenderereco',
            new_name='fac_complementoendereco',
        ),
        migrations.RenameField(
            model_name='dfactoring',
            old_name='fac_enderereco',
            new_name='fac_endereco',
        ),
        migrations.RenameField(
            model_name='dpessoas',
            old_name='pes_complementoenderereco',
            new_name='pes_complementoendereco',
        ),
        migrations.RenameField(
            model_name='dpessoas',
            old_name='pes_enderereco',
            new_name='pes_endereco',
        ),
    ]