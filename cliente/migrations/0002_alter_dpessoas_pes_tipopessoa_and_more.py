# Generated by Django 4.2.7 on 2023-12-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpessoas',
            name='pes_tipopessoa',
            field=models.CharField(choices=[('RE', 'Responsável Empresa'), ('RS', 'Responsável Solidário'), ('RT', 'Responsável Testemunha')], max_length=2),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_prazo2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_prazo3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_prazo4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_prazo5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_prazo6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxadecompraefetiva2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxadecompraefetiva3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxadecompraefetiva4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxadecompraefetiva5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxadecompraefetiva6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxaperiodo2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxaperiodo3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxaperiodo4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxaperiodo5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_taxaperiodo6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorcompra2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorcompra3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorcompra4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorcompra5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorcompra6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriof2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriof3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriof4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriof5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriof6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriofadicional2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriofadicional3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriofadicional4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriofadicional5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valoriofadicional6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorliquido2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorliquido3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorliquido4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorliquido5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valorliquido6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valortotal2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valortotal3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valortotal4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valortotal5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_valortotal6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_vencimento2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_vencimento3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_vencimento4',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_vencimento5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_vencimento6',
            field=models.DateField(blank=True, null=True),
        ),
    ]
