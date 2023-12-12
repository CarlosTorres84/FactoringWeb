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

    