from .models import *
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import JsonResponse, HttpResponse
from docx import Document
import logging
from docx.shared import Pt
from django.core.serializers.json import DjangoJSONEncoder
import json
from num2words import num2words
from datetime import datetime
from django.conf import settings
import os
from docxtpl import DocxTemplate

# Create your views here.

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def inserir_clientes(request):
    if request.method == 'POST':
        form = DClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        dados_dfactoring = Dfactoring.objects.get(fac_id=1)
        form = DClienteForm(initial={
            'cli_taxacompra': dados_dfactoring.fac_taxacompra, 
            'cli_multa': dados_dfactoring.fac_multa,
            'cli_juros': dados_dfactoring.fac_juros,
            'cli_taxarecompra': dados_dfactoring.fac_taxarecompra
        })
        # Atribui valores padrão vazios para campos nulos
        form.instance.cli_email2 = form.instance.cli_email2 or ''
        form.instance.cli_complementoendereco = form.instance.cli_complementoendereco or ''
        form.instance.cli_telefone2 = form.instance.cli_telefone2 or ''
    return render(request, 'inserir_clientes.html', {'form': form})
def listar_clientes(request):
    clientes=Dcliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes':clientes})
def editar_clientes(request, id):
    clientes=Dcliente.objects.get(cli_id=id)
    form = DClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
     # Atribui valores padrão vazios para campos nulos
    form.instance.cli_email2 = form.instance.cli_email2 or ''
    form.instance.cli_complementoendereco = form.instance.cli_complementoendereco or ''
    form.instance.cli_telefone2 = form.instance.cli_telefone2 or ''
    return render(request,'inserir_clientes.html', {'form':form})
def remover_clientes(request, id):
    clientes=Dcliente.objects.get(cli_id=id)
    if request.method=='POST':
        clientes.delete()
        return redirect('listar_clientes')
    return render(request, 'remover_clientes.html',{'clientes':clientes}) 

def inserir_factorings(request):
    if request.method == 'POST':
        form = DFactoringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_factorings')
    else:
        form = DFactoringForm()
        # Atribui valores padrão vazios para campos nulos
        form.instance.fac_email2 = form.instance.fac_email2 or ''
        form.instance.fac_complementoendereco = form.instance.fac_complementoendereco or ''
        form.instance.fac_float = form.instance.fac_float or ''
        form.instance.fac_telefone2 = form.instance.fac_telefone2 or ''
    return render(request, 'inserir_factorings.html', {'form': form})
def listar_factorings(request):
    clientes=Dfactoring.objects.all()
    return render(request, 'listar_factorings.html', {'clientes':clientes})
def editar_factorings(request, id):
    clientes=Dfactoring.objects.get(fac_id=id)
    form = DFactoringForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_factorings')
    # Atribui valores padrão vazios para campos nulos
    form.instance.fac_email2 = form.instance.fac_email2 or ''
    form.instance.fac_complementoendereco = form.instance.fac_complementoendereco or ''
    form.instance.fac_float = form.instance.fac_float or ''
    form.instance.fac_telefone2 = form.instance.fac_telefone2 or ''
    return render(request,'inserir_factorings.html', {'form':form})
def remover_factorings(request, id):
    clientes=Dfactoring.objects.get(fac_id=id)
    if request.method=='POST':
        clientes.delete()
        return redirect('listar_factorings')
    return render(request, 'remover_factorings.html',{'clientes':clientes}) 

def inserir_pessoas(request):
    if request.method == 'POST':
        form = DpessoasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = DpessoasForm()
        # Atribui valores padrão vazios para campos nulos
        form.instance.pes_email2 = form.instance.pes_email2 or ''
        form.instance.pes_complementoendereco = form.instance.pes_complementoendereco or ''
        form.instance.pes_telefone2 = form.instance.pes_telefone2 or ''
    return render(request, 'inserir_pessoas.html', {'form': form})
def listar_pessoas(request):
    pessoas=Dpessoas.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas':pessoas})
def editar_pessoas(request, id):
    clientes=Dpessoas.objects.get(pes_id=id)
    form = DpessoasForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_pessoas')
    # Atribui valores padrão vazios para campos nulos
    form.instance.pes_email2 = form.instance.pes_email2 or ''
    form.instance.pes_complementoendereco = form.instance.pes_complementoendereco or ''
    form.instance.pes_telefone2 = form.instance.pes_telefone2 or ''
    return render(request,'inserir_pessoas.html', {'form':form})
def remover_pessoas(request, id):
    pessoas=Dpessoas.objects.get(pes_id=id)
    if request.method=='POST':
        pessoas.delete()
        return redirect('listar_pessoas')
    return render(request, 'remover_pessoas.html',{'pessoas':pessoas}) 

def inserir_contratomae(request):
    if request.method == 'POST':
        form = DcontratomaeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratomae')
    else:
        form = DcontratomaeForm()
    return render(request, 'inserir_contratomae.html', {'form': form})        
def listar_contratomae(request):
    contratomae=Dcontratomae.objects.all()
    return render(request, 'listar_contratomae.html', {'contratomae':contratomae})
def traduzir_estado_civil(abreviacao):
    traducao = {
        'S': 'SOLTEIRO',
        'C': 'CASADO',
        'D': 'DIVORCIADO',
        'V': 'VIÚVO'
    }
    return traducao.get(abreviacao, '')
def gerar_contrato_word(request, cma_id):
    contrato = Dcontratomae.objects.get(cma_id=cma_id)
    cliente_associado = contrato.cli_id
    factoring_associado = contrato.fac_id
    pessoas_associadas_re = Dpessoas.objects.filter(cli_id_id=contrato.cli_id.cli_id, pes_tipopessoa='RE')
    pessoas_associadas_rs = Dpessoas.objects.filter(cli_id_id=contrato.cli_id.cli_id, pes_tipopessoa='RS')
    pessoas_associadas_rt = Dpessoas.objects.filter(fac_id_id=contrato.fac_id.fac_id, pes_tipopessoa='RT')
    
    template_path = r"D:\Users\carlo\OneDrive\Programação\Factoring\Documentos\ContratoPadrao.docx"
    
    # Formatação vencimento
    data_validade_contrato = contrato.cma_validadecontrato
    validade_formatada = data_validade_contrato.strftime('%d/%m/%Y')

    data_fundacao_cliente = cliente_associado.cli_datafundacao.strftime("%d/%m/%Y")

    data_fundacao_factoring = factoring_associado.fac_datafundacao.strftime("%d/%m/%Y")

    data_nascimento_pessoa0 = ''
    data_nascimento_pessoa1 = ''
    if pessoas_associadas_re:
        data_nascimento_pessoa0 = pessoas_associadas_re[0].pes_datanascimento.strftime("%d/%m/%Y")
        if len(pessoas_associadas_re) > 1:
            data_nascimento_pessoa1 = pessoas_associadas_re[1].pes_datanascimento.strftime("%d/%m/%Y")

    data_nascimento_pessoa00 = ''
    data_nascimento_pessoa01 = ''
    if pessoas_associadas_rs:
        data_nascimento_pessoa00 = pessoas_associadas_rs[0].pes_datanascimento.strftime("%d/%m/%Y")
        if len(pessoas_associadas_rs) > 1:
            data_nascimento_pessoa01 = pessoas_associadas_rs[1].pes_datanascimento.strftime("%d/%m/%Y")

    # Caminho base do diretório "Downloads"
    downloads_dir = r"D:\Users\carlo\Downloads"
    # Nome do arquivo
    file_name = f"{contrato.cma_id2} - CONTRATO FOMENTO MERCANTIL - {cliente_associado.cli_nomefantasia}.docx"
    # Caminho completo do arquivo
    output_path = os.path.join(downloads_dir, file_name)
    doc = DocxTemplate(template_path)
    # Salvar o documento gerado no caminho especificado
    doc.save(output_path)

    # Defina os dados a serem inseridos no modelo
    context = {
        'ID_CONTRATO': contrato.cma_id2,
        'VALIDADE_CONTRATO': validade_formatada,
        # 'ID_CLIENTE'
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': f'RAZÃO SOCIAL: ' + cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': f'CNPJ: ' + cliente_associado.cli_cnpj,
        'IM_CLIENTE': f'INSC. MUNICIPAL: {cliente_associado.cli_im}' if cliente_associado.cli_im else '',
        'IE_CLIENTE': f'INSC. ESTADUAL: {cliente_associado.cli_ie}' if cliente_associado.cli_ie else '',
        'DATAFUNDACAO_CLIENTE': f'FUNDAÇÃO: {data_fundacao_cliente}',
        'EMAIL1_CLIENTE': f'E-MAIL: ' + cliente_associado.cli_email1,
        'TELEFONE1_CLIENTE': f'TELEFONE: ' + cliente_associado.cli_telefone1,
        'ENDERECO_CLIENTE': f'ENDEREÇO: ' + cliente_associado.cli_endereco,
        'COMPLEMENTOENDERECO_CLIENTE': f'COMPLEMENTO: {cliente_associado.cli_complementoendereco}' if cliente_associado.cli_complementoendereco else '',
        'CEP_CLIENTE': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO_CLIENTE': f'BAIRRO: ' + cliente_associado.cli_bairro,
        'CIDADE_CLIENTE': f'CIDADE: ' + cliente_associado.cli_cidade,
        'ESTADO_CLIENTE': f'ESTADO: ' + cliente_associado.cli_estado,
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING':f'RAZÃO SOCIAL: ' +  factoring_associado.fac_razaosocial,
        'CNPJ_FACTORING':f'CNPJ: ' +  factoring_associado.fac_cnpj,
        'IM_FACTORING': f'INSC. MUNICIPAL: {factoring_associado.fac_im}' if factoring_associado.fac_im else '',
        'IE_FACTORING': f'INSC. ESTADUAL: {factoring_associado.fac_ie}' if factoring_associado.fac_ie else '',
        'DATAFUNDACAO_FACTORING': f'FUNDAÇÃO: {data_fundacao_factoring}',
        'EMAIL1_FACTORING': f'E-MAIL: ' + factoring_associado.fac_email1,
        'TELEFONE1_FACTORING': f'TELEFONE: ' + factoring_associado.fac_telefone1,
        'ENDERECO_FACTORING': f'ENDEREÇO: ' + factoring_associado.fac_endereco,
        'COMPLEMENTOENDERECO_FACTORING': f'COMPLEMENTO: ' + factoring_associado.fac_complementoendereco,
        'CEP_FACTORING': f'CEP: ' + factoring_associado.fac_cep,
        'BAIRRO_FACTORING': f'BAIRRO: ' + factoring_associado.fac_bairro,
        'CIDADE_FACTORING': f'CIDADE: ' + factoring_associado.fac_cidade,
        'ESTADO_FACTORING': f'ESTADO: ' + factoring_associado.fac_estado,
        # 'PES_ID'
        'NOME_PESSOA0': f'NOME: ' + pessoas_associadas_re[0].pes_nome if pessoas_associadas_re else '',
        'NOME_PESSOA1': f'NOME: ' + pessoas_associadas_re[1].pes_nome if len(pessoas_associadas_re) > 1 else '',
        'CPF_PESSOA0': f'CPF: ' + pessoas_associadas_re[0].pes_cpf if pessoas_associadas_re else '',
        'CPF_PESSOA1': f'CPF: ' + pessoas_associadas_re[1].pes_cpf if len(pessoas_associadas_re) > 1 else '',
        'RG_PESSOA0': f'RG: ' + pessoas_associadas_re[0].pes_rg if pessoas_associadas_re else '',
        'RG_PESSOA1': f'RG: ' + pessoas_associadas_re[1].pes_rg if len(pessoas_associadas_re) > 1 else '',
        'DATANASCIMENTO_PESSOA0': f'NASCIMENTO: {data_nascimento_pessoa0}',
        'DATANASCIMENTO_PESSOA1': f'NASCIMENTO: {data_nascimento_pessoa1}' if data_nascimento_pessoa1 else '',
        'ESTADOCIVIL_PESSOA0': f'ESTADO CÍVIL: ' + traduzir_estado_civil(pessoas_associadas_re[0].pes_estadocivil) if pessoas_associadas_re else '',
        'ESTADOCIVIL_PESSOA1': f'ESTADO CÍVIL: ' + traduzir_estado_civil(pessoas_associadas_re[1].pes_estadocivil) if len(pessoas_associadas_re) > 1 else '',
        'NACIONALIDADE_PESSOA0': f'NACIONALIDADE: ' + pessoas_associadas_re[0].pes_nacionalidade if pessoas_associadas_re else '',
        'NACIONALIDADE_PESSOA1': f'NACIONALIDADE: ' + pessoas_associadas_re[1].pes_nacionalidade if len(pessoas_associadas_re) > 1 else '',
        'EMAIL1_PESSOA0': f'E-MAIL: ' + pessoas_associadas_re[0].pes_email1 if pessoas_associadas_re else '',
        'EMAIL1_PESSOA1': f'E-MAIL: ' + pessoas_associadas_re[1].pes_email1 if len(pessoas_associadas_re) > 1 else '',
        'TELEFONE1_PESSOA0': f'TELEFONE: ' + pessoas_associadas_re[0].pes_telefone1 if pessoas_associadas_re else '',
        'TELEFONE1_PESSOA1': f'TELEFONE: ' + pessoas_associadas_re[1].pes_telefone1 if len(pessoas_associadas_re) > 1 else '',
        'PROFISSAO_PESSOA0': f'PROFISSÃO: ' + pessoas_associadas_re[0].pes_profissao if pessoas_associadas_re else '',
        'PROFISSAO_PESSOA1': f'PROFISSÃO: ' + pessoas_associadas_re[1].pes_profissao if len(pessoas_associadas_re) > 1 else '',
        'ENDERECO_PESSOA0': f'ENDEREÇO: ' + pessoas_associadas_re[0].pes_endereco if pessoas_associadas_re else '',
        'ENDERECO_PESSOA1': f'ENDEREÇO: ' + pessoas_associadas_re[1].pes_endereco if len(pessoas_associadas_re) > 1 else '',
        'COMPLEMENTOENDERECO_PESSOA0': f'COMPLEMENTO: ' + pessoas_associadas_re[0].pes_complementoendereco if pessoas_associadas_re and pessoas_associadas_re[0].pes_complementoendereco else '',
        'COMPLEMENTOENDERECO_PESSOA1': f'COMPLEMENTO: ' + pessoas_associadas_re[1].pes_complementoendereco if len(pessoas_associadas_re) > 1 and pessoas_associadas_re[1].pes_complementoendereco else '',
        'CEP_PESSOA0': f'CEP: ' + pessoas_associadas_re[0].pes_cep if pessoas_associadas_re else '',
        'CEP_PESSOA1': f'CEP: ' + pessoas_associadas_re[1].pes_cep if len(pessoas_associadas_re) > 1 else '',
        'BAIRRO_PESSOA0': f'BAIRRO: ' + pessoas_associadas_re[0].pes_bairro if pessoas_associadas_re else '',
        'BAIRRO_PESSOA1': f'BAIRRO: ' + pessoas_associadas_re[1].pes_bairro if len(pessoas_associadas_re) > 1 else '',
        'CIDADE_PESSOA0': f'CIDADE: ' + pessoas_associadas_re[0].pes_cidade if pessoas_associadas_re else '',
        'CIDADE_PESSOA1': f'CIDADE: ' + pessoas_associadas_re[1].pes_cidade if len(pessoas_associadas_re) > 1 else '',
        'ESTADO_PESSOA0': f'ESTADO: ' + pessoas_associadas_re[0].pes_estado if pessoas_associadas_re else '',
        'ESTADO_PESSOA1': f'ESTADO: ' + pessoas_associadas_re[1].pes_estado if len(pessoas_associadas_re) > 1 else '',
        'NOME_PESSOA00': f'NOME: ' + pessoas_associadas_rs[0].pes_nome if pessoas_associadas_rs else '',
        'NOME_PESSOA01': f'NOME: ' + pessoas_associadas_rs[1].pes_nome if len(pessoas_associadas_rs) > 1 else '',
        'NOME_PESSOA000': f'NOME: ' + pessoas_associadas_rt[0].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'NOME_PESSOA001': f'NOME: ' + pessoas_associadas_rt[1].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA00': f'CPF: ' + pessoas_associadas_rs[0].pes_cpf if pessoas_associadas_rs else '',
        'CPF_PESSOA01': f'CPF: ' + pessoas_associadas_rs[1].pes_cpf if len(pessoas_associadas_rs) > 1 else '',
        'CPF_PESSOA000': f'CPF: ' + pessoas_associadas_rt[0].pes_cpf if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA001': f'CPF: ' + pessoas_associadas_rt[1].pes_cpf if len(pessoas_associadas_rt) > 1 else '',
        'RG_PESSOA00': f'RG: ' + pessoas_associadas_rs[0].pes_rg if pessoas_associadas_rs else '',
        'RG_PESSOA01': f'RG: ' + pessoas_associadas_rs[1].pes_rg if len(pessoas_associadas_rs) > 1 else '',
        'DATANASCIMENTO_PESSOA00': f'NASCIMENTO: {data_nascimento_pessoa00}',
        'DATANASCIMENTO_PESSOA01': f'NASCIMENTO: {data_nascimento_pessoa01}' if data_nascimento_pessoa01 else '',
        'ESTADOCIVIL_PESSOA00': f'ESTADO CÍVIL: ' + traduzir_estado_civil(pessoas_associadas_rs[0].pes_estadocivil) if pessoas_associadas_rs else '',
        'ESTADOCIVIL_PESSOA01': f'ESTADO CÍVIL: ' + traduzir_estado_civil(pessoas_associadas_rs[1].pes_estadocivil) if len(pessoas_associadas_rs) > 1 else '',
        'NACIONALIDADE_PESSOA00': f'NACIONALIDADE: ' + pessoas_associadas_rs[0].pes_nacionalidade if pessoas_associadas_rs else '',
        'NACIONALIDADE_PESSOA01': f'NACIONALIDADE: ' + pessoas_associadas_rs[1].pes_nacionalidade if len(pessoas_associadas_rs) > 1 else '',
        'EMAIL1_PESSOA00': f'E-MAIL: ' + pessoas_associadas_rs[0].pes_email1 if pessoas_associadas_rs else '',
        'EMAIL1_PESSOA01': f'E-MAIL: ' + pessoas_associadas_rs[1].pes_email1 if len(pessoas_associadas_rs) > 1 else '',
        'TELEFONE1_PESSOA00': f'TELEFONE: ' + pessoas_associadas_rs[0].pes_telefone1 if pessoas_associadas_rs else '',
        'TELEFONE1_PESSOA01': f'TELEFONE: ' + pessoas_associadas_rs[1].pes_telefone1 if len(pessoas_associadas_rs) > 1 else '',
        'PROFISSAO_PESSOA00': f'PROFISSÃO: ' + pessoas_associadas_rs[0].pes_profissao if pessoas_associadas_rs else '',
        'PROFISSAO_PESSOA01': f'PROFISSÃO: ' + pessoas_associadas_rs[1].pes_profissao if len(pessoas_associadas_rs) > 1 else '',
        'ENDERECO_PESSOA00': f'ENDEREÇO: ' + pessoas_associadas_rs[0].pes_endereco if pessoas_associadas_rs else '',
        'ENDERECO_PESSOA01': f'ENDEREÇO :' + pessoas_associadas_rs[1].pes_endereco if len(pessoas_associadas_rs) > 1 else '',
        'COMPLEMENTOENDERECO_PESSOA00': f'COMPLEMENTO: ' + pessoas_associadas_rs[0].pes_complementoendereco if pessoas_associadas_rs and pessoas_associadas_rs[0].pes_complementoendereco else '',
        'COMPLEMENTOENDERECO_PESSOA01': f'COMPLEMENTO: ' + pessoas_associadas_rs[1].pes_complementoendereco if len(pessoas_associadas_rs) > 1 and pessoas_associadas_rs[1].pes_complementoendereco else '',
        'CEP_PESSOA00': f'CEP: ' + pessoas_associadas_rs[0].pes_cep if pessoas_associadas_rs else '',
        'CEP_PESSOA01': f'CEP: ' + pessoas_associadas_rs[1].pes_cep if len(pessoas_associadas_rs) > 1 else '',
        'BAIRRO_PESSOA00': f'BAIRRO: ' + pessoas_associadas_rs[0].pes_bairro if pessoas_associadas_rs else '',
        'BAIRRO_PESSOA01': f'BAIRRO: ' + pessoas_associadas_rs[1].pes_bairro if len(pessoas_associadas_rs) > 1 else '',
        'CIDADE_PESSOA00': f'CIDADE: ' + pessoas_associadas_rs[0].pes_cidade if pessoas_associadas_rs else '',
        'CIDADE_PESSOA01': f'CIDADE: ' + pessoas_associadas_rs[1].pes_cidade if len(pessoas_associadas_rs) > 1 else '',
        'ESTADO_PESSOA00': f'ESTADO: ' + pessoas_associadas_rs[0].pes_estado if pessoas_associadas_rs else '',
        'ESTADO_PESSOA01': f'ESTADO: ' + pessoas_associadas_rs[1].pes_estado if len(pessoas_associadas_rs) > 1 else '',
}
    doc.render(context)
    doc.save(output_path)
    with open(output_path, 'rb') as doc_file:
        response = HttpResponse(doc_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={contrato.cma_id2} - CONTRATO FOMENTO MERCANTIL - {cliente_associado.cli_nomefantasia}.docx'
    return response
def editar_contratomae(request, id):
    contratomae=Dcontratomae.objects.get(cma_id=id)
    form = DcontratomaeForm(request.POST or None, instance=contratomae)
    if form.is_valid():
        form.save()
        return redirect('listar_contratomae')
    return render(request,'inserir_contratomae.html', {'form':form})

def inserir_simulacao(request):
    if request.method == 'POST':
        form = DsimulacaoForm(request.POST)
        if form.is_valid():
            nova_simulacao = form.save()            
            novo_id = nova_simulacao.sim_id            
            return redirect('listar_simulacaocopy')
    else:
        dados_dfactoring = Dfactoring.objects.get(fac_id=1)

        form = DsimulacaoForm(initial={
            'sim_taxacompra': dados_dfactoring.fac_taxacompra,
            'sim_iof': dados_dfactoring.fac_iof,
            'sim_iofadicional': dados_dfactoring.fac_iofadicional,
            'sim_float': dados_dfactoring.fac_float
        })
    return render(request, 'inserir_simulacao.html', {'form': form})
def listar_simulacao(request):
    simulacao=Dsimulacao.objects.all()
    return render(request, 'listar_simulacao.html', {'simulacao':simulacao})
def listar_simulacaocopy(request):
    simulacao=Dsimulacao.objects.all()
    return render(request, 'listar_simulacaocopy.html', {'simulacao':simulacao})
def listar_simulacaoid(request, id):
    simulacao_id=Dsimulacao.objects.get(sim_id=id)
    return render(request, 'listar_simulacaoid.html', {'simulacao_id':simulacao_id})
def gerar_simulacao_word(request, sim_id):
    simulacao = Dsimulacao.objects.get(sim_id=sim_id)
    cliente_associado = simulacao.cli_id
    factoring_associado = simulacao.fac_id
    
    template_path = r"D:\Users\carlo\OneDrive\Programação\Factoring\Documentos\SimulacaoPadrao.docx"     
    
    # Caminho base do diretório "Downloads"
    downloads_dir = r"D:\Users\carlo\Downloads"
    # Nome do arquivo
    file_name = f"SIMULACAO OPER {sim_id} {cliente_associado.cli_nomefantasia} {simulacao.sim_datasimulacao}.docx"
    # Caminho completo do arquivo
    output_path = os.path.join(downloads_dir, file_name)
    doc = DocxTemplate(template_path)
    # Salvar o documento gerado no caminho especificado
    doc.save(output_path)
    
    # Defina os dados a serem inseridos no modelo
    context = {
        'ID_SIM': simulacao.sim_id,
        'DATASIMULACAO': simulacao.sim_datasimulacao.strftime('%d/%m/%Y'),
        'PRAZOME': f'{round(((simulacao.sim_prazo1 * simulacao.sim_valortotal1) + (simulacao.sim_prazo2 * simulacao.sim_valortotal2) + (simulacao.sim_prazo3 * simulacao.sim_valortotal3) + (simulacao.sim_prazo4 * simulacao.sim_valortotal4) + (simulacao.sim_prazo5 * simulacao.sim_valortotal5) +  (simulacao.sim_prazo6 * simulacao.sim_valortotal6)) /  (simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6),0):.0f}'.replace('.', ','),
        'FATORNOM': f'{simulacao.sim_taxacompra:.2f}'.replace('.', ',') + '%',
        'TAXAEFE': f'{simulacao.sim_taxadecompraefetiva1}%'.replace('.', ','),
        'FATORPERI': f'{round(((simulacao.sim_taxaperiodo1 * simulacao.sim_valortotal1) + (simulacao.sim_taxaperiodo2 * simulacao.sim_valortotal2) + (simulacao.sim_taxaperiodo3 * simulacao.sim_valortotal3) + (simulacao.sim_taxaperiodo4 * simulacao.sim_valortotal4) + (simulacao.sim_taxaperiodo5 * simulacao.sim_valortotal5) + (simulacao.sim_taxaperiodo6 * simulacao.sim_valortotal6)) / (simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6), 2):.2f}%'.replace('.', ','),    
        'IOF': f'{round((simulacao.sim_iof), 2):.2f}%',
        'IOFA': f'{round((simulacao.sim_iofadicional), 2):.2f}%',
        'TAXA': f'{round((simulacao.sim_taxacompra), 2):.2f}%',
        # 'ID_CLIENTE
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': cliente_associado.cli_cnpj,
        'EMAIL1_CLIENTE': cliente_associado.cli_email1,
        'TELEFONE1_CLIENTE': cliente_associado.cli_telefone1,
        'ENDERECO_CLIENTE': cliente_associado.cli_endereco,
        'COMPLEMENTO_CLIENTE': cliente_associado.cli_complementoendereco if cliente_associado.cli_complementoendereco else '',
        'CEP': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO': f'BAIRRO: ' + cliente_associado.cli_bairro,
        'CIDADE': f'CIDADE: ' + cliente_associado.cli_cidade,
        'ESTADO': f'ESTADO: ' + cliente_associado.cli_estado,
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING': factoring_associado.fac_razaosocial,        
        # 'SIMULACOES 1 A 6'
        'VALTT1': f' {simulacao.sim_valortotal1:,.2f}'.replace(',', '.'),
        'VALTT2': f' {simulacao.sim_valortotal2:,.2f}'.replace(',', '.') if simulacao.sim_valortotal2 else '',
        'VALTT3': f' {simulacao.sim_valortotal3:,.2f}'.replace(',', '.') if simulacao.sim_valortotal3 else '',
        'VALTT4': f' {simulacao.sim_valortotal4:,.2f}'.replace(',', '.') if simulacao.sim_valortotal4 else '',
        'VALTT5': f' {simulacao.sim_valortotal5:,.2f}'.replace(',', '.') if simulacao.sim_valortotal5 else '',
        'VALTT6': f' {simulacao.sim_valortotal6:,.2f}'.replace(',', '.') if simulacao.sim_valortotal6 else '',
        'VENC1': simulacao.sim_vencimento1.strftime('%d/%m/%Y'),
        'VENC2': simulacao.sim_vencimento2.strftime('%d/%m/%Y') if simulacao.sim_vencimento2 else '',
        'VENC3': simulacao.sim_vencimento3.strftime('%d/%m/%Y') if simulacao.sim_vencimento3 else '',
        'VENC4': simulacao.sim_vencimento4.strftime('%d/%m/%Y') if simulacao.sim_vencimento4 else '',
        'VENC5': simulacao.sim_vencimento5.strftime('%d/%m/%Y') if simulacao.sim_vencimento5 else '',
        'VENC6': simulacao.sim_vencimento6.strftime('%d/%m/%Y') if simulacao.sim_vencimento6 else '',
        'FLOAT1': simulacao.sim_float,
        'FLOAT2': simulacao.sim_float if simulacao.sim_valortotal2 else '',
        'FLOAT3': simulacao.sim_float if simulacao.sim_valortotal3 else '',
        'FLOAT4': simulacao.sim_float if simulacao.sim_valortotal4 else '',
        'FLOAT5': simulacao.sim_float if simulacao.sim_valortotal5 else '',
        'FLOAT6': simulacao.sim_float if simulacao.sim_valortotal6 else '',
        'PRAZO1': simulacao.sim_prazo1,
        'PRAZO2': simulacao.sim_prazo2 if simulacao.sim_prazo2 else '',
        'PRAZO3': simulacao.sim_prazo3 if simulacao.sim_prazo3 else '',
        'PRAZO4': simulacao.sim_prazo4 if simulacao.sim_prazo4 else '',
        'PRAZO5': simulacao.sim_prazo5 if simulacao.sim_prazo5 else '',
        'PRAZO6': simulacao.sim_prazo6 if simulacao.sim_prazo6 else '',
        'COMPRA1': f' {simulacao.sim_valorcompra1:,.2f}'.replace(',', '.'),
        'COMPRA2': f' {simulacao.sim_valorcompra2:,.2f}'.replace(',', '.') if simulacao.sim_valorcompra2 else '',
        'COMPRA3': f' {simulacao.sim_valorcompra3:,.2f}'.replace(',', '.') if simulacao.sim_valorcompra3 else '',
        'COMPRA4': f' {simulacao.sim_valorcompra4:,.2f}'.replace(',', '.') if simulacao.sim_valorcompra4 else '',
        'COMPRA5': f' {simulacao.sim_valorcompra5:,.2f}'.replace(',', '.') if simulacao.sim_valorcompra5 else '',
        'COMPRA6': f' {simulacao.sim_valorcompra6:,.2f}'.replace(',', '.') if simulacao.sim_valorcompra6 else '',
        'FATOR1': simulacao.sim_taxaperiodo1,
        'FATOR2': simulacao.sim_taxaperiodo2 if simulacao.sim_taxaperiodo2 else '',
        'FATOR3': simulacao.sim_taxaperiodo3 if simulacao.sim_taxaperiodo3 else '',
        'FATOR4': simulacao.sim_taxaperiodo4 if simulacao.sim_taxaperiodo4 else '',
        'FATOR5': simulacao.sim_taxaperiodo5 if simulacao.sim_taxaperiodo5 else '',
        'FATOR6': simulacao.sim_taxaperiodo6 if simulacao.sim_taxaperiodo6 else '',
        'FCOMPRA1': f' {(simulacao.sim_valortotal1 - simulacao.sim_valorcompra1):,.2f}'.replace(',', '.'),
        'FCOMPRA2': f' {(simulacao.sim_valortotal2 - simulacao.sim_valorcompra2):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra2 else '',
        'FCOMPRA3': f' {(simulacao.sim_valortotal3 - simulacao.sim_valorcompra3):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra3 else '',
        'FCOMPRA4': f' {(simulacao.sim_valortotal4 - simulacao.sim_valorcompra4):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra4 else '',
        'FCOMPRA5': f' {(simulacao.sim_valortotal5 - simulacao.sim_valorcompra5):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra5 else '',
        'FCOMPRA6': f' {(simulacao.sim_valortotal6 - simulacao.sim_valorcompra6):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra6 else '',
        'IOF1': f' {simulacao.sim_valoriof1:,.2f}'.replace(',', '.'),
        'IOF2': f' {simulacao.sim_valoriof2:,.2f}'.replace(',', '.') if simulacao.sim_valoriof2 else '',
        'IOF3': f' {simulacao.sim_valoriof3:,.2f}'.replace(',', '.') if simulacao.sim_valoriof3 else '',
        'IOF4': f' {simulacao.sim_valoriof4:,.2f}'.replace(',', '.') if simulacao.sim_valoriof4 else '',
        'IOF5': f' {simulacao.sim_valoriof5:,.2f}'.replace(',', '.') if simulacao.sim_valoriof5 else '',
        'IOF6': f' {simulacao.sim_valoriof6:,.2f}'.replace(',', '.') if simulacao.sim_valoriof6 else '',
        'IOFAD1': f' {simulacao.sim_valoriofadicional1:,.2f}'.replace(',', '.'),
        'IOFAD2': f' {simulacao.sim_valoriofadicional2:,.2f}'.replace(',', '.') if simulacao.sim_valoriofadicional2 else '',
        'IOFAD3': f' {simulacao.sim_valoriofadicional3:,.2f}'.replace(',', '.') if simulacao.sim_valoriofadicional3 else '',
        'IOFAD4': f' {simulacao.sim_valoriofadicional4:,.2f}'.replace(',', '.') if simulacao.sim_valoriofadicional4 else '',
        'IOFAD5': f' {simulacao.sim_valoriofadicional5:,.2f}'.replace(',', '.') if simulacao.sim_valoriofadicional5 else '',
        'IOFAD6': f' {simulacao.sim_valoriofadicional6:,.2f}'.replace(',', '.') if simulacao.sim_valoriofadicional6 else '',
        'DESP': f' {simulacao.sim_despesas:,.2f}'.replace(',', '.'),
        'ACRE': f' {simulacao.sim_acrescimos:,.2f}'.replace(',', '.'),
        'DEDU': f' {(-simulacao.sim_despesas + simulacao.sim_acrescimos):,.2f}'.replace(',', '.'),
        'DIFE1': f' {(simulacao.sim_valorcompra1 + simulacao.sim_valoriof1 + simulacao.sim_valoriofadicional1 + simulacao.sim_despesas - simulacao.sim_acrescimos):,.2f}'.replace(',', '.'),
        'DIFE2': f' {(simulacao.sim_valorcompra2 + simulacao.sim_valoriof2 + simulacao.sim_valoriofadicional2):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra2 else '',
        'DIFE3': f' {(simulacao.sim_valorcompra3 + simulacao.sim_valoriof3 + simulacao.sim_valoriofadicional3):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra3 else '',
        'DIFE4': f' {(simulacao.sim_valorcompra4 + simulacao.sim_valoriof4 + simulacao.sim_valoriofadicional4):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra4 else '',
        'DIFE5': f' {(simulacao.sim_valorcompra5 + simulacao.sim_valoriof5 + simulacao.sim_valoriofadicional5):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra5 else '',
        'DIFE6': f' {(simulacao.sim_valorcompra6 + simulacao.sim_valoriof6 + simulacao.sim_valoriofadicional6):,.2f}'.replace(',', '.') if simulacao.sim_valorcompra6 else '',
        'LIQUIDO1': f' {simulacao.sim_valorliquido1:,.2f}'.replace(',', '.'),
        'LIQUIDO2': f' {simulacao.sim_valorliquido2:,.2f}'.replace(',', '.') if simulacao.sim_valorliquido2 != 0 else '',
        'LIQUIDO3': f' {simulacao.sim_valorliquido3:,.2f}'.replace(',', '.') if simulacao.sim_valorliquido3 != 0 else '',
        'LIQUIDO4': f' {simulacao.sim_valorliquido4:,.2f}'.replace(',', '.') if simulacao.sim_valorliquido4 != 0 else '',
        'LIQUIDO5': f' {simulacao.sim_valorliquido5:,.2f}'.replace(',', '.') if simulacao.sim_valorliquido5 != 0 else '',
        'LIQUIDO6': f' {simulacao.sim_valorliquido6:,.2f}'.replace(',', '.') if simulacao.sim_valorliquido6 != 0 else '',
        'VALTT': f' {(simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6):,.2f}'.replace(',', '.'),
        'COUNT': (sum(1 for valor in [simulacao.sim_valortotal1, simulacao.sim_valortotal2, simulacao.sim_valortotal3, simulacao.sim_valortotal4, simulacao.sim_valortotal5, simulacao.sim_valortotal6] if valor is not None and valor > 0)),
        'COMPRATT': f' {(simulacao.sim_valorcompra1 + simulacao.sim_valorcompra2 + simulacao.sim_valorcompra3 + simulacao.sim_valorcompra4 + simulacao.sim_valorcompra5 + simulacao.sim_valorcompra6):,.2f}'.replace(',', '.'),
        'FCOMPRATT': f' {(simulacao.sim_valortotal1 - simulacao.sim_valorcompra1) + (simulacao.sim_valortotal2 - simulacao.sim_valorcompra2) + (simulacao.sim_valortotal3 - simulacao.sim_valorcompra3) + (simulacao.sim_valortotal4 - simulacao.sim_valorcompra4) + (simulacao.sim_valortotal5 - simulacao.sim_valorcompra5) + (simulacao.sim_valortotal6 - simulacao.sim_valorcompra6):,.2f}'.replace(',', '.'), 
        'IOFTT': f' {(simulacao.sim_valoriof1 + simulacao.sim_valoriof2 + simulacao.sim_valoriof3 + simulacao.sim_valoriof4 + simulacao.sim_valoriof5 + simulacao.sim_valoriof6):,.2f}'.replace(',', '.'),
        'IOFADTT': f' {(simulacao.sim_valoriofadicional1 + simulacao.sim_valoriofadicional2 + simulacao.sim_valoriofadicional3 + simulacao.sim_valoriofadicional4 + simulacao.sim_valoriofadicional5 + simulacao.sim_valoriofadicional6):,.2f}'.replace(',', '.'), 
        'DIFETT': f' { ((simulacao.sim_valorcompra1 + simulacao.sim_valoriof1 + simulacao.sim_valoriofadicional1 + simulacao.sim_despesas - simulacao.sim_acrescimos) + (simulacao.sim_valorcompra2 + simulacao.sim_valoriof2 + simulacao.sim_valoriofadicional2) + (simulacao.sim_valorcompra3 + simulacao.sim_valoriof3 + simulacao.sim_valoriofadicional3) + (simulacao.sim_valorcompra4 + simulacao.sim_valoriof4 + simulacao.sim_valoriofadicional4) + (simulacao.sim_valorcompra5 + simulacao.sim_valoriof5 + simulacao.sim_valoriofadicional5) + (simulacao.sim_valorcompra6 + simulacao.sim_valoriof6 + simulacao.sim_valoriofadicional6)):,.2f}'.replace(',', '.'),
        'LIQTT': f' {(simulacao.sim_valorliquido1 + simulacao.sim_valorliquido2 + simulacao.sim_valorliquido3 + simulacao.sim_valorliquido4 + simulacao.sim_valorliquido5 + simulacao.sim_valorliquido6):,.2f}'.replace(',', '.'),
        'VLIQUIDOTT': f' {((simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6) - (simulacao.sim_valorcompra1 + simulacao.sim_valorcompra2 + simulacao.sim_valorcompra3 + simulacao.sim_valorcompra4 + simulacao.sim_valorcompra5 + simulacao.sim_valorcompra6) - (simulacao.sim_valoriof1 + simulacao.sim_valoriof2 + simulacao.sim_valoriof3 + simulacao.sim_valoriof4 + simulacao.sim_valoriof5 + simulacao.sim_valoriof6) - (simulacao.sim_valoriofadicional1 + simulacao.sim_valoriofadicional2 + simulacao.sim_valoriofadicional3 + simulacao.sim_valoriofadicional4 + simulacao.sim_valoriofadicional5 + simulacao.sim_valoriofadicional6)):,.2f}'.replace(',', '.'),
    }
    doc.render(context)
    doc.save(output_path)
    with open(output_path, 'rb') as doc_file:
        response = HttpResponse(doc_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=SIMULACAO OPER {sim_id} {cliente_associado.cli_nomefantasia} {simulacao.sim_datasimulacao}.docx'
    return response
def editar_simulacao(request, id):
    simulacao=Dsimulacao.objects.get(sim_id=id)
    form = DsimulacaoForm(request.POST or None, instance=simulacao)
    if form.is_valid():
        form.save()
        return redirect('listar_simulacaocopy')
    return render(request, 'inserir_simulacao.html', {'form':form})

def inserir_operacao(request, sim_id):
    try:
        # Obter informações da simulação
        simulacao = Dsimulacao.objects.get(sim_id=sim_id)   
        if request.method == 'POST':
            form = DoperacaoForm(request.POST)
            if form.is_valid():
                nova_operacao = form.save()
                novo_id = nova_operacao.ope_id                
                return redirect('listar_operacaoid', id=novo_id)
            else:
                print("Formulário não é válido")
                print(f"Erros no formulário: {form.errors}")
        else:     
            form = DoperacaoForm(initial={
                'ope_dataoperacao': simulacao.sim_datasimulacao,
                'cli_id': simulacao.cli_id,
                'fac_id': simulacao.fac_id,
                'ope_taxacompra': simulacao.sim_taxacompra,
                'ope_iof': simulacao.sim_iof,
                'ope_iofadicional': simulacao.sim_iofadicional,
                'ope_despesas': simulacao.sim_despesas,
                'ope_acrescimos': simulacao.sim_acrescimos,
                'ope_float': simulacao.sim_float,
                'ope_vencimento1' : simulacao.sim_vencimento1,
                'ope_vencimento2' : simulacao.sim_vencimento2,
                'ope_vencimento3' : simulacao.sim_vencimento3,
                'ope_vencimento4' : simulacao.sim_vencimento4,
                'ope_vencimento5' : simulacao.sim_vencimento5,
                'ope_vencimento6' : simulacao.sim_vencimento6,
                'ope_valortotal1' : simulacao.sim_valortotal1,
                'ope_valortotal2' : simulacao.sim_valortotal2,
                'ope_valortotal3' : simulacao.sim_valortotal3,
                'ope_valortotal4' : simulacao.sim_valortotal4,
                'ope_valortotal5' : simulacao.sim_valortotal5,
                'ope_valortotal6' : simulacao.sim_valortotal6
            })               
    except Exception as e:
        print(f"Erro ao inserir operação: {e}")
        raise
    return render(request, 'inserir_operacao.html', {'form': form})
def listar_operacao(request):
    operacao=Doperacao.objects.all()
    return render(request, 'listar_operacao.html', {'operacao':operacao})
def listar_operacaoid(request, id):
    operacao_id = Doperacao.objects.get(ope_id=id)
    return render(request, 'listar_operacaoid.html', {'i': operacao_id})
def editar_operacao(request, id):
    operacao=Doperacao.objects.get(ope_id=id)
    form = DoperacaoForm(request.POST or None, instance=operacao)
    if form.is_valid():
        form.save()
        return redirect('listar_operacao')
    return render(request, 'inserir_operacao.html', {'form':form})
def gerar_operacao_word(request, ope_id):
    operacao = Doperacao.objects.get(ope_id=ope_id)
    contratomae_associado = operacao.cma_id
    cliente_associado = operacao.cli_id
    factoring_associado = operacao.fac_id       
    pessoas_associadas_rs = Dpessoas.objects.filter(cli_id_id=operacao.cli_id.cli_id, pes_tipopessoa='RS')
    pessoas_associadas_rt = Dpessoas.objects.filter(fac_id_id=operacao.fac_id.fac_id, pes_tipopessoa='RT')

    template_path = r"D:\Users\carlo\OneDrive\Programação\Factoring\Documentos\OperacaoPadrao.docx"     

    # Caminho base do diretório "Downloads"
    downloads_dir = r"D:\Users\carlo\Downloads"
    # Nome do arquivo
    file_name = f"ADITIVO OPER {ope_id} {cliente_associado.cli_nomefantasia} {operacao.ope_dataoperacao}.docx"
  # Caminho completo do arquivo
    output_path = os.path.join(downloads_dir, file_name)
    doc = DocxTemplate(template_path)
    # Salvar o documento gerado no caminho especificado
    doc.save(output_path)

    # Defina os dados a serem inseridos no modelo
    context = {        
        'ID_OPE': operacao.ope_id,
        'DATAOPERACAO': operacao.ope_dataoperacao.strftime('%d/%m/%Y'),
        # 'ID_CONTRATOMAE
        "CONTRATOMAE" : contratomae_associado.cma_id2,
        "DATACONTRATOMAE" : contratomae_associado.cma_datacadastro.strftime('%d/%m/%Y'),
        # 'ID_CLIENTE
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': f'EMPRESA: ' + cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': f'CNPJ: ' + cliente_associado.cli_cnpj,        
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING': f'EMPRESA: ' + factoring_associado.fac_razaosocial,
        'CNPJ_FACTORING': f'CNPJ: ' + factoring_associado.fac_cnpj,
        # 'OPERAÇÕES1 A 6'
        'NUMTITULO1': operacao.ope_numtitulo1,
        'NUMTITULO2': operacao.ope_numtitulo2 if operacao.ope_numtitulo2 else '',
        'NUMTITULO3': operacao.ope_numtitulo3 if operacao.ope_numtitulo3 else '',
        'NUMTITULO4': operacao.ope_numtitulo4 if operacao.ope_numtitulo4 else '',
        'NUMTITULO5': operacao.ope_numtitulo5 if operacao.ope_numtitulo5 else '',
        'NUMTITULO6': operacao.ope_numtitulo6 if operacao.ope_numtitulo6 else '',
        'NOMESACADO1': operacao.ope_razaosocial1,
        'NOMESACADO2': operacao.ope_razaosocial2 if operacao.ope_numtitulo2 else '',
        'NOMESACADO3': operacao.ope_razaosocial3 if operacao.ope_numtitulo3 else '',
        'NOMESACADO4': operacao.ope_razaosocial4 if operacao.ope_numtitulo4 else '',
        'NOMESACADO5': operacao.ope_razaosocial5 if operacao.ope_numtitulo5 else '',
        'NOMESACADO6': operacao.ope_razaosocial6 if operacao.ope_numtitulo6 else '',
        'VALTT1': f' {operacao.ope_valortotal1:,.2f}'.replace(',', '.'),
        'VALTT2': f' {operacao.ope_valortotal2:,.2f}'.replace(',', '.') if operacao.ope_valortotal2 else '',
        'VALTT3': f' {operacao.ope_valortotal3:,.2f}'.replace(',', '.') if operacao.ope_valortotal3 else '',
        'VALTT4': f' {operacao.ope_valortotal4:,.2f}'.replace(',', '.') if operacao.ope_valortotal4 else '',
        'VALTT5': f' {operacao.ope_valortotal5:,.2f}'.replace(',', '.') if operacao.ope_valortotal5 else '',
        'VALTT6': f' {operacao.ope_valortotal6:,.2f}'.replace(',', '.') if operacao.ope_valortotal6 else '',
        'VENC1': operacao.ope_vencimento1.strftime('%d/%m/%Y'),
        'VENC2': operacao.ope_vencimento2.strftime('%d/%m/%Y') if operacao.ope_vencimento2 else '',
        'VENC3': operacao.ope_vencimento3.strftime('%d/%m/%Y') if operacao.ope_vencimento3 else '',
        'VENC4': operacao.ope_vencimento4.strftime('%d/%m/%Y') if operacao.ope_vencimento4 else '',
        'VENC5': operacao.ope_vencimento5.strftime('%d/%m/%Y') if operacao.ope_vencimento5 else '',
        'VENC6': operacao.ope_vencimento6.strftime('%d/%m/%Y') if operacao.ope_vencimento6 else '',
        'DESP': f' {operacao.ope_despesas:,.2f}'.replace(',', '.'),
        'ACRE': f' {operacao.ope_acrescimos:,.2f}'.replace(',', '.'),
        'RECO': f' {operacao.ope_recompra:,.2f}'.replace(',', '.'),
        'JURO': f' {operacao.ope_juros:,.2f}'.replace(',', '.'),
        'VALTT': f' {(operacao.ope_valortotal1 + operacao.ope_valortotal2 + operacao.ope_valortotal3 + operacao.ope_valortotal4 + operacao.ope_valortotal5 + operacao.ope_valortotal6):,.2f}'.replace(',', '.'),
        'COUNT': (sum(1 for valor in [operacao.ope_valortotal1, operacao.ope_valortotal2, operacao.ope_valortotal3, operacao.ope_valortotal4, operacao.ope_valortotal5, operacao.ope_valortotal6] if valor is not None and valor > 0)),
        'COMPRATT': f' {(operacao.ope_valorcompra1 + operacao.ope_valorcompra2 + operacao.ope_valorcompra3 + operacao.ope_valorcompra4 + operacao.ope_valorcompra5 + operacao.ope_valorcompra6):,.2f}'.replace(',', '.'),
        'IOFTT': f' {(operacao.ope_valoriof1 + operacao.ope_valoriof2 + operacao.ope_valoriof3 + operacao.ope_valoriof4 + operacao.ope_valoriof5 + operacao.ope_valoriof6):,.2f}'.replace(',', '.'),
        'IOFADTT': f' {(operacao.ope_valoriofadicional1 + operacao.ope_valoriofadicional2 + operacao.ope_valoriofadicional3 + operacao.ope_valoriofadicional4 + operacao.ope_valoriofadicional5 + operacao.ope_valoriofadicional6):,.2f}'.replace(',', '.'), 
        'LIQTT': f' {(operacao.ope_valorliquido1 + operacao.ope_valorliquido2 + operacao.ope_valorliquido3 + operacao.ope_valorliquido4 + operacao.ope_valorliquido5 + operacao.ope_valorliquido6):,.2f}'.replace(',', '.'),
        # 'PES_ID'
        'NOME_PESSOA00': f'NOME: ' + pessoas_associadas_rs[0].pes_nome if pessoas_associadas_rs else '',
        'NOME_PESSOA01': f'NOME: ' + pessoas_associadas_rs[1].pes_nome if len(pessoas_associadas_rs) > 1 else '',
        'NOME_PESSOA000': f'NOME: ' + pessoas_associadas_rt[0].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'NOME_PESSOA001': f'NOME: ' + pessoas_associadas_rt[1].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA00': f'CPF: ' + pessoas_associadas_rs[0].pes_cpf if pessoas_associadas_rs else '',
        'CPF_PESSOA01': f'CPF: ' + pessoas_associadas_rs[1].pes_cpf if len(pessoas_associadas_rs) > 1 else '',
        'CPF_PESSOA000': f'CPF: ' + pessoas_associadas_rt[0].pes_cpf if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA001': f'CPF: ' + pessoas_associadas_rt[1].pes_cpf if len(pessoas_associadas_rt) > 1 else '',

    }
    doc.render(context)
    doc.save(output_path)
    with open(output_path, 'rb') as doc_file:
        response = HttpResponse(doc_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=ADITIVO OPER {ope_id} {cliente_associado.cli_nomefantasia} {operacao.ope_dataoperacao}.docx'
    return response
def gerar_promissoria_word(request, ope_id):
    operacao = Doperacao.objects.get(ope_id=ope_id)    
    cliente_associado = operacao.cli_id
    factoring_associado = operacao.fac_id       
    pessoas_associadas_rs = Dpessoas.objects.filter(cli_id_id=operacao.cli_id.cli_id, pes_tipopessoa='RS')
    pessoas_associadas_rt = Dpessoas.objects.filter(fac_id_id=operacao.fac_id.fac_id, pes_tipopessoa='RT')
    COMPRATT = (operacao.ope_valortotal1 + operacao.ope_valortotal2 + operacao.ope_valortotal3 + operacao.ope_valortotal4 + operacao.ope_valortotal5 + operacao.ope_valortotal6)
    parte_inteira = str(COMPRATT).split('.')[0]
    numero = int(parte_inteira)
    numero_por_extenso = num2words(numero, lang='pt_BR')
    if '.' in str(COMPRATT):
        parte_decimal = str(COMPRATT).split('.')[1]
        numero_por_extenso += f" vírgula {num2words(parte_decimal, lang='pt_BR')}"
    datas = [operacao.ope_vencimento1, operacao.ope_vencimento2, operacao.ope_vencimento3, operacao.ope_vencimento4, operacao.ope_vencimento5, operacao.ope_vencimento6]
    datas_validas = filter(None, datas)  # Filtra os valores None
    maior_data = max(datas_validas, default=None)
    if maior_data:
        maior_data_formatada = maior_data.strftime('%d/%m/%Y')
    else:
        maior_data_formatada = ''
    
    # Caminho para arquivo Padrão
    template_path = r"D:\Users\carlo\OneDrive\Programação\Factoring\Documentos\NotaPromissoriaPadrao.docx"     

    # Caminho base do diretório "Downloads"
    downloads_dir = r"D:\Users\carlo\Downloads"  
    #Nome do arquivo
    file_name = f"PROMISSORIA OPER {ope_id} {cliente_associado.cli_nomefantasia} {operacao.ope_dataoperacao}.docx"
    # Caminho completo do arquivo
    output_path = os.path.join(downloads_dir, file_name)
    doc = DocxTemplate(template_path)
    # Salvar o documento gerado no caminho especificado
    doc.save(output_path)

    # Defina os dados a serem inseridos no modelo
    context = {        
        'ID_OPE': operacao.ope_id,
        'DATAOPERACAO': operacao.ope_dataoperacao.strftime('%d/%m/%Y'),        
        # 'ID_CLIENTE
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': f'Empresa: ' + cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': f'CNPJ: ' + cliente_associado.cli_cnpj,        
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING': f'Empresa: ' + factoring_associado.fac_razaosocial,
        'CNPJ_FACTORING': f'CNPJ: ' + factoring_associado.fac_cnpj,
        'ENDERECO_CLIENTE': f'ENDEREÇO: ' + cliente_associado.cli_endereco,
        'COMPLEMENTOENDERECO_CLIENTE': cliente_associado.cli_complementoendereco,
        'CEP_CLIENTE': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO_CLIENTE': cliente_associado.cli_bairro,
        'CIDADE_CLIENTE': cliente_associado.cli_cidade,
        'ESTADO_CLIENTE': cliente_associado.cli_estado,
        # 'OPERAÇÕES1 A 6'                        
        'VENC1': maior_data_formatada,        
        'VALTT': f' {(operacao.ope_valortotal1 + operacao.ope_valortotal2 + operacao.ope_valortotal3 + operacao.ope_valortotal4 + operacao.ope_valortotal5 + operacao.ope_valortotal6):,.2f}'.replace(',', '.'),        
        'COMPRATT_POR_EXTENSO': numero_por_extenso,
        # 'PES_ID'
        'NOME_PESSOA00': f'NOME: ' + pessoas_associadas_rs[0].pes_nome if pessoas_associadas_rs else '',
        'NOME_PESSOA01': f'NOME: ' + pessoas_associadas_rs[1].pes_nome if len(pessoas_associadas_rs) > 1 else '',
        'NOME_PESSOA000': f'NOME: ' + pessoas_associadas_rt[0].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'NOME_PESSOA001': f'NOME: ' + pessoas_associadas_rt[1].pes_nome if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA00': f'CPF: ' + pessoas_associadas_rs[0].pes_cpf if pessoas_associadas_rs else '',
        'CPF_PESSOA01': f'CPF: ' + pessoas_associadas_rs[1].pes_cpf if len(pessoas_associadas_rs) > 1 else '',
        'CPF_PESSOA000': f'CPF: ' + pessoas_associadas_rt[0].pes_cpf if len(pessoas_associadas_rt) > 1 else '',
        'CPF_PESSOA001': f'CPF: ' + pessoas_associadas_rt[1].pes_cpf if len(pessoas_associadas_rt) > 1 else '',
        'ENDERECO_PES00': f'Endereço:: ' + pessoas_associadas_rs[0].pes_endereco if pessoas_associadas_rs else '',
        'ENDERECO_PES01': f'Endereço: ' + pessoas_associadas_rs[1].pes_endereco if len(pessoas_associadas_rs) > 1 else '',
        'COMPLEENDE_PES00': pessoas_associadas_rs[0].pes_complementoendereco if pessoas_associadas_rs else '',
        'COMPLEENDE_PES01': pessoas_associadas_rs[1].pes_complementoendereco if len(pessoas_associadas_rs) > 1 else '',
        'BAIRRO_PES00': pessoas_associadas_rs[0].pes_bairro if pessoas_associadas_rs else '',
        'BAIRRO_PES01': pessoas_associadas_rs[1].pes_bairro if len(pessoas_associadas_rs) > 1 else '',
        'CIDADE_PES00': pessoas_associadas_rs[0].pes_cidade if pessoas_associadas_rs else '',
        'CIDADE_PES01': pessoas_associadas_rs[1].pes_cidade if len(pessoas_associadas_rs) > 1 else '',
        'ESTADO_PES00': pessoas_associadas_rs[0].pes_estado if pessoas_associadas_rs else '',
        'ESTADO_PES01': pessoas_associadas_rs[1].pes_estado if len(pessoas_associadas_rs) > 1 else '',
        'CEP_PES00': f'CEP: ' + pessoas_associadas_rs[0].pes_cep if pessoas_associadas_rs else '',
        'CEP_PES01': f'CEP: ' + pessoas_associadas_rs[1].pes_cep if len(pessoas_associadas_rs) > 1 else '',

    }
    doc.render(context)
    doc.save(output_path)
    with open(output_path, 'rb') as doc_file:
        response = HttpResponse(doc_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=PROMISSORIA OPER {ope_id} {cliente_associado.cli_nomefantasia} {operacao.ope_dataoperacao}.docx'
    return response

def listar_carteira(request):
    operacao=Doperacao.objects.all()
    carteira=Dcarteira.objects.all()
    return render(request, 'listar_carteira.html', {'operacao':operacao, 'carteira':carteira})
def inserir_pagamentos(request):
    operacao=Doperacao.objects.all()
    form = DcarteiraForm()
    try:
        if request.method == 'POST':
            form = DcarteiraForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listar_carteira')
            else:
                print("Formulário não é válido")
                print(f"Erros no formulário: {form.errors}")
    except Exception as e:
        print(f"Erro ao inserir operação: {e}")
        raise
    return render(request, 'inserir_pagamentos.html', {'form': form, 'operacao':operacao})
def listar_pagamentos(request):
    operacao=Doperacao.objects.all()
    carteira=Dcarteira.objects.all()
    return render(request, 'listar_pagamentos.html', {'operacao':operacao, 'carteira':carteira})
