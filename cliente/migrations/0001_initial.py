# Generated by Django 4.2.7 on 2024-01-02 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dcliente',
            fields=[
                ('cli_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('cli_razaosocial', models.CharField(max_length=50)),
                ('cli_nomefantasia', models.CharField(max_length=50)),
                ('cli_cnpj', models.CharField(max_length=20)),
                ('cli_im', models.CharField(max_length=20)),
                ('cli_ie', models.CharField(max_length=20)),
                ('cli_email1', models.EmailField(max_length=30)),
                ('cli_email2', models.EmailField(blank=True, max_length=30, null=True)),
                ('cli_telefone1', models.CharField(max_length=14)),
                ('cli_telefone2', models.CharField(blank=True, max_length=14, null=True)),
                ('cli_enderereco', models.CharField(max_length=50)),
                ('cli_complementoenderereco', models.CharField(max_length=50)),
                ('cli_cep', models.CharField(max_length=10)),
                ('cli_bairro', models.CharField(max_length=50)),
                ('cli_cidade', models.CharField(max_length=20)),
                ('cli_estado', models.CharField(max_length=20)),
                ('cli_taxacompra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cli_multa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cli_juros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cli_taxarecompra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cli_valortotaloperacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cli_datacadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dcontratomae',
            fields=[
                ('cma_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('cma_validadecontrato', models.DateField()),
                ('cma_datacadastro', models.DateField()),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dcliente')),
            ],
        ),
        migrations.CreateModel(
            name='Dfactoring',
            fields=[
                ('fac_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('fac_razaosocial', models.CharField(max_length=50)),
                ('fac_nomefantasia', models.CharField(max_length=50)),
                ('fac_cnpj', models.CharField(max_length=20)),
                ('fac_im', models.CharField(max_length=20)),
                ('fac_ie', models.CharField(max_length=20)),
                ('fac_email1', models.EmailField(max_length=30)),
                ('fac_email2', models.EmailField(blank=True, max_length=30, null=True)),
                ('fac_telefone1', models.CharField(max_length=14)),
                ('fac_telefone2', models.CharField(blank=True, max_length=14, null=True)),
                ('fac_enderereco', models.CharField(max_length=50)),
                ('fac_complementoenderereco', models.CharField(max_length=50)),
                ('fac_cep', models.CharField(max_length=10)),
                ('fac_bairro', models.CharField(max_length=50)),
                ('fac_cidade', models.CharField(max_length=20)),
                ('fac_estado', models.CharField(max_length=20)),
                ('fac_taxacompra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fac_iof', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fac_iofadicional', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fac_pis', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fac_cofins', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fac_float', models.IntegerField()),
                ('fac_multa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fac_juros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fac_taxarecompra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fac_valortotaloperacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fac_datacadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dsimulacao',
            fields=[
                ('sim_id', models.AutoField(primary_key=True, serialize=False)),
                ('sim_datasimulacao', models.DateField()),
                ('sim_taxadecompra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_iof', models.DecimalField(decimal_places=7, max_digits=10)),
                ('sim_iofadicional', models.DecimalField(decimal_places=7, max_digits=10)),
                ('sim_despesas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_acrescimos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_myfloat', models.IntegerField()),
                ('sim_vencimento1', models.DateField()),
                ('sim_valortotal1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_prazo1', models.IntegerField()),
                ('sim_taxadecompraefetiva1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_taxaperiodo1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_valorcompra1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_valoriof1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_valoriofadicional1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_valorliquido1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sim_vencimento2', models.DateField(blank=True, null=True)),
                ('sim_valortotal2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_prazo2', models.IntegerField(blank=True, null=True)),
                ('sim_taxadecompraefetiva2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_taxaperiodo2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorcompra2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriof2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriofadicional2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorliquido2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_vencimento3', models.DateField(blank=True, null=True)),
                ('sim_valortotal3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_prazo3', models.IntegerField(blank=True, null=True)),
                ('sim_taxadecompraefetiva3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_taxaperiodo3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorcompra3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriof3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriofadicional3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorliquido3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_vencimento4', models.DateField(blank=True, null=True)),
                ('sim_valortotal4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_prazo4', models.IntegerField(blank=True, null=True)),
                ('sim_taxadecompraefetiva4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_taxaperiodo4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorcompra4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriof4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriofadicional4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorliquido4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_vencimento5', models.DateField(blank=True, null=True)),
                ('sim_valortotal5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_prazo5', models.IntegerField(blank=True, null=True)),
                ('sim_taxadecompraefetiva5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_taxaperiodo5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorcompra5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriof5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriofadicional5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorliquido5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_vencimento6', models.DateField(blank=True, null=True)),
                ('sim_valortotal6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_prazo6', models.IntegerField(blank=True, null=True)),
                ('sim_taxadecompraefetiva6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_taxaperiodo6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorcompra6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriof6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valoriofadicional6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_valorliquido6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sim_status', models.CharField(choices=[('1', 'SIMULAÇÃO')], max_length=1)),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dcliente')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dfactoring')),
            ],
        ),
        migrations.CreateModel(
            name='Dpessoas',
            fields=[
                ('pes_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('pes_nome', models.CharField(max_length=50)),
                ('pes_cpf', models.CharField(max_length=14)),
                ('pes_rg', models.CharField(max_length=14)),
                ('pes_estadocivil', models.CharField(max_length=14)),
                ('pes_nacionalidade', models.CharField(max_length=20)),
                ('pes_email1', models.EmailField(max_length=30)),
                ('pes_email2', models.EmailField(blank=True, max_length=30, null=True)),
                ('pes_telefone1', models.CharField(max_length=14)),
                ('pes_telefone2', models.CharField(blank=True, max_length=14, null=True)),
                ('pes_profissao', models.CharField(max_length=30)),
                ('pes_enderereco', models.CharField(max_length=50)),
                ('pes_complementoenderereco', models.CharField(max_length=50)),
                ('pes_cep', models.CharField(max_length=10)),
                ('pes_bairro', models.CharField(max_length=50)),
                ('pes_cidade', models.CharField(max_length=20)),
                ('pes_estado', models.CharField(max_length=20)),
                ('pes_tipopessoa', models.CharField(choices=[('RE', 'Responsável Empresa'), ('RS', 'Responsável Solidário'), ('RT', 'Responsável Testemunha')], max_length=2)),
                ('pes_datacadastro', models.DateField()),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dcliente')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dfactoring')),
            ],
        ),
        migrations.CreateModel(
            name='Doperacao',
            fields=[
                ('ope_id', models.AutoField(primary_key=True, serialize=False)),
                ('ope_dataoperacao', models.DateField()),
                ('ope_taxadecompra', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ope_iof', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ope_iofadicional', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ope_despesas', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ope_acrescimos', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ope_myfloat', models.IntegerField()),
                ('ope_numtitulo1', models.IntegerField(default=0)),
                ('ope_razaosocial1', models.CharField(max_length=50)),
                ('ope_cnpj1', models.CharField(max_length=20)),
                ('ope_email1', models.EmailField(max_length=30)),
                ('ope_telefone1', models.CharField(max_length=14)),
                ('ope_nomecontato1', models.CharField(max_length=50)),
                ('ope_endereco1', models.CharField(max_length=50)),
                ('ope_complementoendereco1', models.CharField(max_length=50)),
                ('ope_cep1', models.CharField(max_length=10)),
                ('ope_bairro1', models.CharField(max_length=50)),
                ('ope_cidade1', models.CharField(max_length=20)),
                ('ope_estado1', models.CharField(max_length=20)),
                ('ope_vencimento1', models.DateField()),
                ('ope_valortotal1', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ope_prazo1', models.IntegerField()),
                ('ope_taxadecompraefetiva1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_taxaperiodo1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_valorcompra1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_valoriof1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_valoriofadicional1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_valorliquido1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ope_numtitulo2', models.IntegerField(blank=True, default=0, null=True)),
                ('ope_razaosocial2', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cnpj2', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_email2', models.EmailField(blank=True, max_length=30, null=True)),
                ('ope_telefone2', models.CharField(blank=True, max_length=14, null=True)),
                ('ope_nomecontato2', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_endereco2', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_complementoendereco2', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cep2', models.CharField(blank=True, max_length=10, null=True)),
                ('ope_bairro2', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cidade2', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_estado2', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_vencimento2', models.DateField(blank=True, null=True)),
                ('ope_valortotal2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('ope_prazo2', models.IntegerField(blank=True, null=True)),
                ('ope_taxadecompraefetiva2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_taxaperiodo2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorcompra2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriof2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriofadicional2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorliquido2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_numtitulo3', models.IntegerField(blank=True, default=0, null=True)),
                ('ope_razaosocial3', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cnpj3', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_email3', models.EmailField(blank=True, max_length=30, null=True)),
                ('ope_telefone3', models.CharField(blank=True, max_length=14, null=True)),
                ('ope_nomecontato3', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_endereco3', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_complementoendereco3', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cep3', models.CharField(blank=True, max_length=10, null=True)),
                ('ope_bairro3', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cidade3', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_estado3', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_vencimento3', models.DateField(blank=True, null=True)),
                ('ope_valortotal3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('ope_prazo3', models.IntegerField(blank=True, null=True)),
                ('ope_taxadecompraefetiva3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_taxaperiodo3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorcompra3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriof3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriofadicional3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorliquido3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_numtitulo4', models.IntegerField(blank=True, default=0, null=True)),
                ('ope_razaosocial4', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cnpj4', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_email4', models.EmailField(blank=True, max_length=30, null=True)),
                ('ope_telefone4', models.CharField(blank=True, max_length=14, null=True)),
                ('ope_nomecontato4', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_endereco4', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_complementoendereco4', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cep4', models.CharField(blank=True, max_length=10, null=True)),
                ('ope_bairro4', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cidade4', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_estado4', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_vencimento4', models.DateField(blank=True, null=True)),
                ('ope_valortotal4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('ope_prazo4', models.IntegerField(blank=True, null=True)),
                ('ope_taxadecompraefetiva4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_taxaperiodo4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorcompra4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriof4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriofadicional4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorliquido4', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_numtitulo5', models.IntegerField(blank=True, default=0, null=True)),
                ('ope_razaosocial5', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cnpj5', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_email5', models.EmailField(blank=True, max_length=30, null=True)),
                ('ope_telefone5', models.CharField(blank=True, max_length=14, null=True)),
                ('ope_nomecontato5', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_endereco5', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_complementoendereco5', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cep5', models.CharField(blank=True, max_length=10, null=True)),
                ('ope_bairro5', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cidade5', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_estado5', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_vencimento5', models.DateField(blank=True, null=True)),
                ('ope_valortotal5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('ope_prazo5', models.IntegerField(blank=True, null=True)),
                ('ope_taxadecompraefetiva5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_taxaperiodo5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorcompra5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriof5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriofadicional5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorliquido5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_numtitulo6', models.IntegerField(blank=True, default=0, null=True)),
                ('ope_razaosocial6', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cnpj6', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_email6', models.EmailField(blank=True, max_length=30, null=True)),
                ('ope_telefone6', models.CharField(blank=True, max_length=14, null=True)),
                ('ope_nomecontato6', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_endereco6', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_complementoendereco6', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cep6', models.CharField(blank=True, max_length=10, null=True)),
                ('ope_bairro6', models.CharField(blank=True, max_length=50, null=True)),
                ('ope_cidade6', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_estado6', models.CharField(blank=True, max_length=20, null=True)),
                ('ope_vencimento6', models.DateField(blank=True, null=True)),
                ('ope_valortotal6', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('ope_prazo6', models.IntegerField(blank=True, null=True)),
                ('ope_taxadecompraefetiva6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_taxaperiodo6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorcompra6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriof6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valoriofadicional6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_valorliquido6', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_status', models.CharField(choices=[('2', 'OPERAÇÃO')], max_length=1)),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dcliente')),
                ('cma_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dcontratomae')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dfactoring')),
            ],
        ),
        migrations.AddField(
            model_name='dcontratomae',
            name='fac_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.dfactoring'),
        ),
        migrations.CreateModel(
            name='Dcarteira',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_datapgto', models.DateField()),
                ('car_valorpgto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('car_titulonumero', models.IntegerField(blank=True, null=True)),
                ('car_valortotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ope_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.doperacao')),
            ],
        ),
    ]
