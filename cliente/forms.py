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

class DsimulacaoForm(forms.ModelForm):
    class Meta:
        model = Dsimulacao
        fields = [
            'sim_datasimulacao', 'cli_id', 'fac_id', 'sim_taxadecompra','sim_iof', 'sim_iofadicional', 'sim_despesas', 'sim_acrescimos',       'sim_myfloat', 'sim_vencimento1', 'sim_valortotal1', 'sim_prazo1','sim_taxadecompraefetiva1', 'sim_taxaperiodo1', 'sim_valorcompra1','sim_valoriof1', 'sim_valoriofadicional1', 'sim_valorliquido1','sim_vencimento2', 'sim_valortotal2', 'sim_prazo2','sim_taxadecompraefetiva2', 'sim_taxaperiodo2', 'sim_valorcompra2','sim_valoriof2', 'sim_valoriofadicional2', 'sim_valorliquido2','sim_vencimento3', 'sim_valortotal3', 'sim_prazo3','sim_taxadecompraefetiva3', 'sim_taxaperiodo3', 'sim_valorcompra3','sim_valoriof3', 'sim_valoriofadicional3', 'sim_valorliquido3','sim_vencimento4', 'sim_valortotal4', 'sim_prazo4','sim_taxadecompraefetiva4', 'sim_taxaperiodo4', 'sim_valorcompra4','sim_valoriof4', 'sim_valoriofadicional4', 'sim_valorliquido4','sim_vencimento5', 'sim_valortotal5', 'sim_prazo5','sim_taxadecompraefetiva5', 'sim_taxaperiodo5', 'sim_valorcompra5','sim_valoriof5', 'sim_valoriofadicional5', 'sim_valorliquido5','sim_vencimento6', 'sim_valortotal6', 'sim_prazo6','sim_taxadecompraefetiva6', 'sim_taxaperiodo6', 'sim_valorcompra6','sim_valoriof6', 'sim_valoriofadicional6', 'sim_valorliquido6', 'sim_status']

class DoperacaoForm(forms.ModelForm):
    class Meta:
        model = Doperacao
        fields = [
            'ope_datasimulacao', 'cli_id', 'fac_id', 'ope_taxadecompra','ope_iof', 'ope_iofadicional', 'ope_despesas', 'ope_acrescimos',       'ope_myfloat', 'ope_vencimento1', 'ope_valortotal1', 'ope_prazo1','ope_taxadecompraefetiva1', 'ope_taxaperiodo1', 'ope_valorcompra1','ope_valoriof1', 'ope_valoriofadicional1', 'ope_valorliquido1','ope_vencimento2', 'ope_valortotal2', 'ope_prazo2','ope_taxadecompraefetiva2', 'ope_taxaperiodo2', 'ope_valorcompra2','ope_valoriof2', 'ope_valoriofadicional2', 'ope_valorliquido2','ope_vencimento3', 'ope_valortotal3', 'ope_prazo3','ope_taxadecompraefetiva3', 'ope_taxaperiodo3', 'ope_valorcompra3','ope_valoriof3', 'ope_valoriofadicional3', 'ope_valorliquido3','ope_vencimento4', 'ope_valortotal4', 'ope_prazo4','ope_taxadecompraefetiva4', 'ope_taxaperiodo4', 'ope_valorcompra4','ope_valoriof4', 'ope_valoriofadicional4', 'ope_valorliquido4','ope_vencimento5', 'ope_valortotal5', 'ope_prazo5','ope_taxadecompraefetiva5', 'ope_taxaperiodo5', 'ope_valorcompra5','ope_valoriof5', 'ope_valoriofadicional5', 'ope_valorliquido5','ope_vencimento6', 'ope_valortotal6', 'ope_prazo6','ope_taxadecompraefetiva6', 'ope_taxaperiodo6', 'ope_valorcompra6','ope_valoriof6', 'ope_valoriofadicional6', 'ope_valorliquido6', 'ope_status']

