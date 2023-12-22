from django.db import models

# Create your models here.
class Dcliente(models.Model):
    cli_id=models.CharField(max_length=12, primary_key=True)
    cli_razaosocial=models.CharField(max_length=50)
    cli_nomefantasia=models.CharField(max_length=50)
    cli_cnpj=models.CharField(max_length=20)
    cli_im=models.CharField(max_length=20)
    cli_ie=models.CharField(max_length=20)
    cli_email1=models.EmailField(max_length=30)
    cli_email2=models.EmailField(max_length=30, blank=True, null=True)
    cli_telefone1=models.CharField(max_length=14)
    cli_telefone2=models.CharField(max_length=14, blank=True, null=True)
    cli_enderereco=models.CharField(max_length=50)
    cli_complementoenderereco=models.CharField(max_length=50)
    cli_cep=models.CharField(max_length=10)
    cli_bairro=models.CharField(max_length=50)
    cli_cidade=models.CharField(max_length=20)
    cli_estado=models.CharField(max_length=20)
    cli_taxacompra=models.DecimalField(max_digits=5, decimal_places=2)
    cli_multa=models.DecimalField(max_digits=5, decimal_places=2)
    cli_juros=models.DecimalField(max_digits=5, decimal_places=2)
    cli_taxarecompra=models.DecimalField(max_digits=10, decimal_places=2)
    cli_valortotaloperacao=models.DecimalField(max_digits=10, decimal_places=2)
    cli_datacadastro=models.DateField()
    def __str__(self):
        return f'{self.cli_id}'

class Dfactoring(models.Model):
    fac_id=models.CharField(max_length=12, primary_key=True)
    fac_razaosocial=models.CharField(max_length=50)
    fac_nomefantasia=models.CharField(max_length=50)
    fac_cnpj=models.CharField(max_length=20)
    fac_im=models.CharField(max_length=20)
    fac_ie=models.CharField(max_length=20)
    fac_email1=models.EmailField(max_length=30)
    fac_email2=models.EmailField(max_length=30, blank=True, null=True)
    fac_telefone1=models.CharField(max_length=14)
    fac_telefone2=models.CharField(max_length=14, blank=True, null=True)
    fac_enderereco=models.CharField(max_length=50)
    fac_complementoenderereco=models.CharField(max_length=50)
    fac_cep=models.CharField(max_length=10)
    fac_bairro=models.CharField(max_length=50)
    fac_cidade=models.CharField(max_length=20)
    fac_estado=models.CharField(max_length=20)
    fac_taxacompra=models.DecimalField(max_digits=5, decimal_places=2)
    fac_iof=models.DecimalField(max_digits=7, decimal_places=2)
    fac_iofadicional=models.DecimalField(max_digits=7, decimal_places=2)
    fac_pis=models.DecimalField(max_digits=5, decimal_places=2)
    fac_cofins=models.DecimalField(max_digits=5, decimal_places=2)
    fac_float=models.IntegerField()
    fac_multa=models.DecimalField(max_digits=5, decimal_places=2)
    fac_juros=models.DecimalField(max_digits=5, decimal_places=2)
    fac_taxarecompra=models.DecimalField(max_digits=10, decimal_places=2)
    fac_valortotaloperacao=models.DecimalField(max_digits=10, decimal_places=2)
    fac_datacadastro=models.DateField()
    def __str__(self):
        return f'{self.fac_id}'

class Dpessoas(models.Model):
    pes_id=models.CharField(max_length=12, primary_key=True)
    pes_nome=models.CharField(max_length=50)
    pes_cpf=models.CharField(max_length=14)
    pes_rg=models.CharField(max_length=14)
    pes_estadocivil=models.CharField(max_length=14)
    pes_nacionalidade=models.CharField(max_length=20)
    pes_email1=models.EmailField(max_length=30)
    pes_email2=models.EmailField(max_length=30, blank=True, null=True)
    pes_telefone1=models.CharField(max_length=14)
    pes_telefone2=models.CharField(max_length=14, blank=True, null=True)
    pes_profissao=models.CharField(max_length=30)
    pes_enderereco=models.CharField(max_length=50)
    pes_complementoenderereco=models.CharField(max_length=50)
    pes_cep=models.CharField(max_length=10)
    pes_bairro=models.CharField(max_length=50)
    pes_cidade=models.CharField(max_length=20)
    pes_estado=models.CharField(max_length=20)
    cli_id=models.ForeignKey(Dcliente, on_delete=models.CASCADE)
    fac_id=models.ForeignKey(Dfactoring, on_delete=models.CASCADE)
    pes_tipopessoa=models.CharField(max_length=6)
    pes_datacadastro=models.DateField()
    def __str__(self):
        return f'{self.pes_id}'

class Dcontratomae(models.Model):
    cma_id=models.CharField(max_length=12, primary_key=True)
    cli_id=models.ForeignKey(Dcliente, on_delete=models.CASCADE)
    fac_id=models.ForeignKey(Dfactoring, on_delete=models.CASCADE)    
    cma_validadecontrato=models.DateField()
    cma_datacadastro=models.DateField()
    def __str__(self):
        return f'{self.cma_id}'
    
class Dsimulacao(models.Model):
    sim_id = models.AutoField(primary_key=True)
    sim_datasimulacao = models.DateField()
    cli_id = models.ForeignKey(Dcliente, on_delete=models.CASCADE)
    fac_id=models.ForeignKey(Dfactoring, on_delete=models.CASCADE)    
    sim_taxadecompra = models.DecimalField(max_digits=10, decimal_places=2)
    sim_iof = models.DecimalField(max_digits=10, decimal_places=7)
    sim_iofadicional = models.DecimalField(max_digits=10, decimal_places=7)
    sim_despesas = models.DecimalField(max_digits=10, decimal_places=2)
    sim_acrescimos = models.DecimalField(max_digits=10, decimal_places=2)
    sim_myfloat = models.IntegerField()
    sim_vencimento1 = models.DateField()
    sim_valortotal1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo1 = models.IntegerField()
    sim_taxadecompraefetiva1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido1 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_vencimento2 = models.DateField()
    sim_valortotal2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo2 = models.IntegerField()
    sim_taxadecompraefetiva2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido2 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_vencimento3 = models.DateField()
    sim_valortotal3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo3 = models.IntegerField()
    sim_taxadecompraefetiva3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido3 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_vencimento4 = models.DateField()
    sim_valortotal4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo4 = models.IntegerField()
    sim_taxadecompraefetiva4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido4 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_vencimento5 = models.DateField()
    sim_valortotal5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo5 = models.IntegerField()
    sim_taxadecompraefetiva5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido5 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_vencimento6 = models.DateField()
    sim_valortotal6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_prazo6 = models.IntegerField()
    sim_taxadecompraefetiva6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_taxaperiodo6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorcompra6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriof6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valoriofadicional6 = models.DecimalField(max_digits=10, decimal_places=2)
    sim_valorliquido6 = models.DecimalField(max_digits=10, decimal_places=2)
    status_CHOICES=(
        ('1', 'SIMULAÇÃO'),
        ('2', 'OPERAÇÃO'),        
    )
    sim_status=models.CharField(max_length=1, choices=status_CHOICES)
    def __str__(self):
        return f'{self.sim_id}'

class Doperacao(models.Model):
    ope_id = models.AutoField(primary_key=True)
    ope_datasimulacao = models.DateField()
    cli_id = models.ForeignKey(Dcliente, on_delete=models.CASCADE)
    fac_id=models.ForeignKey(Dfactoring, on_delete=models.CASCADE)    
    ope_taxadecompra = models.DecimalField(max_digits=10, decimal_places=2)
    ope_iof = models.DecimalField(max_digits=10, decimal_places=7)
    ope_iofadicional = models.DecimalField(max_digits=10, decimal_places=7)
    ope_despesas = models.DecimalField(max_digits=10, decimal_places=2)
    ope_acrescimos = models.DecimalField(max_digits=10, decimal_places=2)
    ope_myfloat = models.IntegerField()
    ope_vencimento1 = models.DateField()
    ope_valortotal1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo1 = models.IntegerField()
    ope_taxadecompraefetiva1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_vencimento2 = models.DateField()
    ope_valortotal2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo2 = models.IntegerField()
    ope_taxadecompraefetiva2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido2 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_vencimento3 = models.DateField()
    ope_valortotal3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo3 = models.IntegerField()
    ope_taxadecompraefetiva3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido3 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_vencimento4 = models.DateField()
    ope_valortotal4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo4 = models.IntegerField()
    ope_taxadecompraefetiva4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido4 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_vencimento5 = models.DateField()
    ope_valortotal5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo5 = models.IntegerField()
    ope_taxadecompraefetiva5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido5 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_vencimento6 = models.DateField()
    ope_valortotal6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo6 = models.IntegerField()
    ope_taxadecompraefetiva6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional6 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido6 = models.DecimalField(max_digits=10, decimal_places=2)
    status_CHOICES=(        
        ('2', 'OPERAÇÃO'),        
    )
    ope_status=models.CharField(max_length=1, choices=status_CHOICES)
    def __str__(self):
        return f'{self.ope_id}'

    