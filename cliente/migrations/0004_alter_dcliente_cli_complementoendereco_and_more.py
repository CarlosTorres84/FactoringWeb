# Generated by Django 4.2.7 on 2024-01-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_rename_cli_complementoenderereco_dcliente_cli_complementoendereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcliente',
            name='cli_complementoendereco',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcliente',
            name='cli_ie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dcliente',
            name='cli_im',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dfactoring',
            name='fac_complementoendereco',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dfactoring',
            name='fac_im',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dpessoas',
            name='pes_complementoendereco',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dpessoas',
            name='pes_estadocivil',
            field=models.CharField(choices=[('S', 'SOLTEIRO(A)'), ('C', 'CASADO(A)'), ('D', 'DIVORCIADO(A)'), ('V', 'VIÚVO(A)')], max_length=14),
        ),
    ]
