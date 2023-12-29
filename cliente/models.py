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
        return f'{self.cli_nomefantasia}'

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
        return f'{self.fac_nomefantasia}'

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
    status_CHOICES=(
        ('RE', 'Responsável Empresa'),
        ('RS', 'Responsável Solidário'),
        ('RT', 'Responsável Testemunha'),
    )
    pes_tipopessoa=models.CharField(max_length=2, choices=status_CHOICES)    
    pes_datacadastro=models.DateField()
    def __str__(self):
        return f'{self.pes_nome}'

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
    sim_vencimento2 = models.DateField(null=True, blank=True)
    sim_valortotal2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_prazo2 = models.IntegerField(null=True, blank=True)
    sim_taxadecompraefetiva2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_taxaperiodo2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorcompra2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriof2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriofadicional2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorliquido2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_vencimento3 = models.DateField(null=True, blank=True)
    sim_valortotal3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_prazo3 = models.IntegerField(null=True, blank=True)
    sim_taxadecompraefetiva3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_taxaperiodo3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorcompra3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriof3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriofadicional3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorliquido3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_vencimento4 = models.DateField(null=True, blank=True)
    sim_valortotal4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_prazo4 = models.IntegerField(null=True, blank=True)
    sim_taxadecompraefetiva4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_taxaperiodo4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorcompra4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriof4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriofadicional4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorliquido4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_vencimento5 = models.DateField(null=True, blank=True)
    sim_valortotal5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_prazo5 = models.IntegerField(null=True, blank=True)
    sim_taxadecompraefetiva5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_taxaperiodo5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorcompra5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriof5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriofadicional5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorliquido5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_vencimento6 = models.DateField(null=True, blank=True)
    sim_valortotal6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_prazo6 = models.IntegerField(null=True, blank=True)
    sim_taxadecompraefetiva6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_taxaperiodo6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorcompra6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriof6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valoriofadicional6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sim_valorliquido6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status_CHOICES=(
        ('1', 'SIMULAÇÃO'),        
    )
    sim_status=models.CharField(max_length=1, choices=status_CHOICES)    
    def __str__(self):
        return f'{self.sim_id}'

class Doperacao(models.Model):    
    ope_id = models.AutoField(primary_key=True)
    ope_dataoperacao = models.DateField()
    cma_id=models.ForeignKey(Dcontratomae, on_delete=models.CASCADE)    
    cli_id = models.ForeignKey(Dcliente, on_delete=models.CASCADE)
    fac_id=models.ForeignKey(Dfactoring, on_delete=models.CASCADE)    
    ope_taxadecompra = models.DecimalField(max_digits=10, decimal_places=7, default=0.00)
    ope_iof = models.DecimalField(max_digits=10, decimal_places=7)
    ope_iofadicional = models.DecimalField(max_digits=10, decimal_places=7)
    ope_despesas = models.DecimalField(max_digits=10, decimal_places=7)
    ope_acrescimos = models.DecimalField(max_digits=10, decimal_places=7)
    ope_myfloat = models.IntegerField()
    ope_numtitulo1 = models.IntegerField(default=0)
    ope_razaosocial1 = models.CharField(max_length=50)
    ope_cnpj1 = models.CharField(max_length=20)
    ope_email1 = models.EmailField(max_length=30)
    ope_telefone1 = models.CharField(max_length=14)
    ope_nomecontato1 = models.CharField(max_length=50)
    ope_endereco1 = models.CharField(max_length=50)
    ope_complementoendereco1 = models.CharField(max_length=50)
    ope_cep1 = models.CharField(max_length=10)
    ope_bairro1 = models.CharField(max_length=50)
    ope_cidade1=models.CharField(max_length=20)
    ope_estado1=models.CharField(max_length=20)
    ope_vencimento1 = models.DateField()
    ope_valortotal1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_prazo1 = models.IntegerField()
    ope_taxadecompraefetiva1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_taxaperiodo1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorcompra1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriof1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valoriofadicional1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_valorliquido1 = models.DecimalField(max_digits=10, decimal_places=2)
    ope_numtitulo2 = models.IntegerField(null=True, blank=True, default=0)
    ope_razaosocial2 = models.CharField(max_length=50, null=True, blank=True)
    ope_cnpj2 = models.CharField(max_length=20, null=True, blank=True)
    ope_email2 = models.EmailField(max_length=30, null=True, blank=True)
    ope_telefone2 = models.CharField(max_length=14, null=True, blank=True)
    ope_nomecontato2 = models.CharField(max_length=50, null=True, blank=True)
    ope_endereco2 = models.CharField(max_length=50, null=True, blank=True)
    ope_complementoendereco2 = models.CharField(max_length=50, null=True, blank=True)
    ope_cep2 = models.CharField(max_length=10, null=True, blank=True)
    ope_bairro2 = models.CharField(max_length=50, null=True, blank=True)
    ope_cidade2 = models.CharField(max_length=20, null=True, blank=True)
    ope_estado2 = models.CharField(max_length=20, null=True, blank=True)
    ope_vencimento2 = models.DateField(null=True, blank=True)
    ope_valortotal2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_prazo2 = models.IntegerField(null=True, blank=True)
    ope_taxadecompraefetiva2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_taxaperiodo2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorcompra2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriof2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriofadicional2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorliquido2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_numtitulo3 = models.IntegerField(null=True, blank=True, default=0)
    ope_razaosocial3 = models.CharField(max_length=50, null=True, blank=True)
    ope_cnpj3 = models.CharField(max_length=20, null=True, blank=True)
    ope_email3 = models.EmailField(max_length=30, null=True, blank=True)
    ope_telefone3 = models.CharField(max_length=14, null=True, blank=True)
    ope_nomecontato3 = models.CharField(max_length=50, null=True, blank=True)
    ope_endereco3 = models.CharField(max_length=50, null=True, blank=True)
    ope_complementoendereco3 = models.CharField(max_length=50, null=True, blank=True)
    ope_cep3 = models.CharField(max_length=10, null=True, blank=True)
    ope_bairro3 = models.CharField(max_length=50, null=True, blank=True)
    ope_cidade3 = models.CharField(max_length=20, null=True, blank=True)
    ope_estado3 = models.CharField(max_length=20, null=True, blank=True)
    ope_vencimento3 = models.DateField(null=True, blank=True)
    ope_valortotal3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_prazo3 = models.IntegerField(null=True, blank=True)
    ope_taxadecompraefetiva3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_taxaperiodo3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorcompra3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriof3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriofadicional3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorliquido3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_numtitulo4 = models.IntegerField(null=True, blank=True, default=0)
    ope_razaosocial4 = models.CharField(max_length=50, null=True, blank=True)
    ope_cnpj4 = models.CharField(max_length=20, null=True, blank=True)
    ope_email4 = models.EmailField(max_length=30, null=True, blank=True)
    ope_telefone4 = models.CharField(max_length=14, null=True, blank=True)
    ope_nomecontato4 = models.CharField(max_length=50, null=True, blank=True)
    ope_endereco4 = models.CharField(max_length=50, null=True, blank=True)
    ope_complementoendereco4 = models.CharField(max_length=50, null=True, blank=True)
    ope_cep4 = models.CharField(max_length=10, null=True, blank=True)
    ope_bairro4 = models.CharField(max_length=50, null=True, blank=True)
    ope_cidade4 = models.CharField(max_length=20, null=True, blank=True)
    ope_estado4 = models.CharField(max_length=20, null=True, blank=True)
    ope_vencimento4 = models.DateField(null=True, blank=True)
    ope_valortotal4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_prazo4 = models.IntegerField(null=True, blank=True)
    ope_taxadecompraefetiva4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_taxaperiodo4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorcompra4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriof4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriofadicional4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorliquido4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_numtitulo5 = models.IntegerField(null=True, blank=True, default=0)
    ope_razaosocial5 = models.CharField(max_length=50, null=True, blank=True)
    ope_cnpj5 = models.CharField(max_length=20, null=True, blank=True)
    ope_email5 = models.EmailField(max_length=30, null=True, blank=True)
    ope_telefone5 = models.CharField(max_length=14, null=True, blank=True)
    ope_nomecontato5 = models.CharField(max_length=50, null=True, blank=True)
    ope_endereco5 = models.CharField(max_length=50, null=True, blank=True)
    ope_complementoendereco5 = models.CharField(max_length=50, null=True, blank=True)
    ope_cep5 = models.CharField(max_length=10, null=True, blank=True)
    ope_bairro5 = models.CharField(max_length=50, null=True, blank=True)
    ope_cidade5 = models.CharField(max_length=20, null=True, blank=True)
    ope_estado5 = models.CharField(max_length=20, null=True, blank=True)
    ope_vencimento5 = models.DateField(null=True, blank=True)
    ope_valortotal5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_prazo5 = models.IntegerField(null=True, blank=True)
    ope_taxadecompraefetiva5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_taxaperiodo5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorcompra5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriof5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriofadicional5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorliquido5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_numtitulo6 = models.IntegerField(null=True, blank=True, default=0)
    ope_razaosocial6 = models.CharField(max_length=50, null=True, blank=True)
    ope_cnpj6 = models.CharField(max_length=20, null=True, blank=True)
    ope_email6 = models.EmailField(max_length=30, null=True, blank=True)
    ope_telefone6 = models.CharField(max_length=14, null=True, blank=True)
    ope_nomecontato6 = models.CharField(max_length=50, null=True, blank=True)
    ope_endereco6 = models.CharField(max_length=50, null=True, blank=True)
    ope_complementoendereco6 = models.CharField(max_length=50, null=True, blank=True)
    ope_cep6 = models.CharField(max_length=10, null=True, blank=True)
    ope_bairro6 = models.CharField(max_length=50, null=True, blank=True)
    ope_cidade6 = models.CharField(max_length=20, null=True, blank=True)
    ope_estado6 = models.CharField(max_length=20, null=True, blank=True)
    ope_vencimento6 = models.DateField(null=True, blank=True)
    ope_valortotal6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_prazo6 = models.IntegerField(null=True, blank=True)
    ope_taxadecompraefetiva6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_taxaperiodo6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorcompra6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriof6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valoriofadicional6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ope_valorliquido6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status_CHOICES=(        
        ('2', 'OPERAÇÃO'),        
    )
    ope_status=models.CharField(max_length=1, choices=status_CHOICES)
    def __str__(self):
        return f'{self.ope_id}'