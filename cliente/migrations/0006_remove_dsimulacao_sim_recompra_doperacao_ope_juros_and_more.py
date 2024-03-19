# Generated by Django 4.2.7 on 2024-03-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_dcliente_cli_datafundacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsimulacao',
            name='sim_recompra',
        ),
        migrations.AddField(
            model_name='doperacao',
            name='ope_juros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dcliente',
            name='cli_datafundacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dfactoring',
            name='fac_datafundacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dpessoas',
            name='pes_datanascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dpessoas',
            name='pes_tipopessoa',
            field=models.CharField(choices=[('RE', 'RESPONSÁVEL EMPRESA'), ('RS', 'RESPONSÁVEL SOLIDÁRIO'), ('RT', 'RESPONSÁVEL TESTEMUNHA')], max_length=2),
        ),
    ]
