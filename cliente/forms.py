from django import forms
from .models import *
from datetime import datetime, timedelta   

class DClienteForm(forms.ModelForm):
    class Meta:
        model = Dcliente
        fields = ['cli_id', 'cli_razaosocial',     'cli_nomefantasia',     'cli_cnpj',     'cli_im',     'cli_ie',     'cli_email1',     'cli_email2',     'cli_telefone1',     'cli_telefone2',     'cli_enderereco',     'cli_complementoenderereco',     'cli_cep',     'cli_bairro',     'cli_cidade',     'cli_estado',     'cli_taxacompra',     'cli_multa',     'cli_juros',     'cli_taxarecompra',     'cli_valortotaloperacao',     'cli_datacadastro']

class DFactoringForm(forms.ModelForm):
    class Meta:
        model = Dfactoring
        fields = ['fac_id', 'fac_razaosocial', 'fac_nomefantasia', 'fac_cnpj', 'fac_im', 'fac_ie', 'fac_email1', 'fac_email2', 'fac_telefone1', 'fac_telefone2', 'fac_enderereco', 'fac_complementoenderereco', 'fac_cep', 'fac_bairro', 'fac_cidade', 'fac_estado', 'fac_taxacompra', 'fac_iof', 'fac_iofadicional', 'fac_pis', 'fac_cofins', 'fac_float', 'fac_multa', 'fac_juros', 'fac_taxarecompra', 'fac_valortotaloperacao', 'fac_datacadastro']

class DpessoasForm(forms.ModelForm):
    class Meta:
        model = Dpessoas
        fields = ['pes_id', 'pes_nome','pes_cpf','pes_rg','pes_estadocivil','pes_nacionalidade','pes_email1','pes_email2','pes_telefone1','pes_telefone2','pes_profissao','pes_enderereco','pes_complementoenderereco','pes_cep','pes_bairro','pes_cidade','pes_estado','cli_id','fac_id','pes_tipopessoa','pes_datacadastro']

class DcontratomaeForm(forms.ModelForm):
    class Meta:
        model = Dcontratomae
        fields = ['cma_id', 'cli_id', 'fac_id', 'cma_validadecontrato','cma_datacadastro']
    # criado para trazer a data de cadastro automáticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pré-preencha o campo cma_datacadastro com a data atual
        self.fields['cma_datacadastro'].initial = datetime.now().strftime('%d/%m/%Y')
        # Pré-preencha o campo cma_validadecontrato com a data atual mais 730 dias
        data_cadastro = datetime.now()
        data_validade = data_cadastro + timedelta(days=730)
        self.fields['cma_validadecontrato'].initial = data_validade.strftime('%d/%m/%Y')
