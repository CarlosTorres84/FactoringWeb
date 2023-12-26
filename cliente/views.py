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
        form = DClienteForm()
    return render(request, 'inserir_clientes.html', {'form': form})
def listar_clientes(request):
    clientes=Dcliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes':clientes})
def editar_clientes(request, id):
    clientes = get_object_or_404(Dcliente, cli_id=id)
    if request.method == 'POST':
        clientes.cli_id = request.POST.get('cli_id')
        clientes.cli_razaosocial = request.POST.get('cli_razaosocial')
        clientes.cli_nomefantasia = request.POST.get('cli_nomefantasia')
        clientes.cli_cnpj = request.POST.get('cli_cnpj')
        clientes.cli_im = request.POST.get('cli_im')
        clientes.cli_ie = request.POST.get('cli_ie')
        clientes.cli_email1 = request.POST.get('cli_email1')
        clientes.cli_email2 = request.POST.get('cli_email2')
        clientes.cli_telefone1 = request.POST.get('cli_telefone1')
        clientes.cli_telefone2 = request.POST.get('cli_telefone2')
        clientes.cli_enderereco = request.POST.get('cli_enderereco')
        clientes.cli_complementoenderereco = request.POST.get('cli_complementoenderereco')
        clientes.cli_cep = request.POST.get('cli_cep')
        clientes.cli_bairro = request.POST.get('cli_bairro')
        clientes.cli_cidade = request.POST.get('cli_cidade')
        clientes.cli_estado = request.POST.get('cli_estado')
        
        taxacomprastr = request.POST.get('cli_taxacompra')
        taxacomprastr = taxacomprastr.replace(',', '.')
        clientes.cli_taxacompra = float(taxacomprastr)

        multastr = request.POST.get('cli_multa')
        multastr = multastr.replace(',', '.')
        clientes.cli_multa = float(multastr)

        jurosstr = request.POST.get('cli_juros')
        jurosstr = jurosstr.replace(',', '.')
        clientes.cli_juros = float(jurosstr)

        taxarecomprastr = request.POST.get('cli_taxarecompra')
        taxarecomprastr = taxarecomprastr.replace(',', '.')
        clientes.cli_taxarecompra = float(taxarecomprastr)

        valortotaloperacaostr = request.POST.get('cli_valortotaloperacao')
        valortotaloperacaostr = valortotaloperacaostr.replace(',', '.')
        clientes.cli_valortotaloperacao = float(valortotaloperacaostr)
        # Certifique-se de que cliente.data_cadastro é um objeto datetime
        clientes.cli_datacadastro = datetime.strptime(request.POST.get('cli_datacadastro'), '%Y-%m-%d')
        datacadastro_formatada = clientes.cli_datacadastro.strftime('%Y-%m-%d')
        clientes.save()
        return redirect('listar_clientes')
    return render(request, 'editar_clientes.html', {'clientes': clientes})
def editar_clientes2(request, id):
    clientes=Dcliente.objects.get(cli_id=id)
    form = DClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
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
    return render(request, 'inserir_factorings.html', {'form': form})
def listar_factorings(request):
    clientes=Dfactoring.objects.all()
    return render(request, 'listar_factorings.html', {'clientes':clientes})
def editar_factorings(request, id):
    clientes = get_object_or_404(Dfactoring, fac_id=id)
    if request.method == 'POST':
        clientes.fac_id = request.POST.get('fac_id')
        clientes.fac_razaosocial = request.POST.get('fac_razaosocial')
        clientes.fac_nomefantasia = request.POST.get('fac_nomefantasia')
        clientes.fac_cnpj = request.POST.get('fac_cnpj')
        clientes.fac_im = request.POST.get('fac_im')
        clientes.fac_ie = request.POST.get('fac_ie')
        clientes.fac_email1 = request.POST.get('fac_email1')
        clientes.fac_email2 = request.POST.get('fac_email2')
        clientes.fac_telefone1 = request.POST.get('fac_telefone1')
        clientes.fac_telefone2 = request.POST.get('fac_telefone2')
        clientes.fac_enderereco = request.POST.get('fac_enderereco')
        clientes.fac_complementoenderereco = request.POST.get('fac_complementoenderereco')
        clientes.fac_cep = request.POST.get('fac_cep')
        clientes.fac_bairro = request.POST.get('fac_bairro')
        clientes.fac_cidade = request.POST.get('fac_cidade')
        clientes.fac_estado = request.POST.get('fac_estado')
        
        taxacomprastr = request.POST.get('fac_taxacompra')
        taxacomprastr = taxacomprastr.replace(',', '.')
        clientes.fac_taxacompra = float(taxacomprastr)

        iofstr = request.POST.get('fac_iof')
        iofstr = iofstr.replace(',', '.')
        clientes.fac_iof = float(iofstr)

        iofadicionalstr = request.POST.get('fac_iofadicional')
        iofadicionalstr = iofadicionalstr.replace(',', '.')
        clientes.fac_iofadicional = float(iofadicionalstr)

        pisstr = request.POST.get('fac_pis')
        pisstr = pisstr.replace(',', '.')
        clientes.fac_pis = float(pisstr)

        cofinsstr = request.POST.get('fac_cofins')
        cofinsstr = cofinsstr.replace(',', '.')
        clientes.fac_cofins = float(cofinsstr)

        floatstr = request.POST.get('fac_float')
        floatstr = floatstr.replace(',', '.')
        clientes.fac_float = float(floatstr)

        multastr = request.POST.get('fac_multa')
        multastr = multastr.replace(',', '.')
        clientes.fac_multa = float(multastr)

        jurosstr = request.POST.get('fac_juros')
        jurosstr = jurosstr.replace(',', '.')
        clientes.fac_juros = float(jurosstr)

        taxarecomprastr = request.POST.get('fac_taxarecompra')
        taxarecomprastr = taxarecomprastr.replace(',', '.')
        clientes.fac_taxarecompra = float(taxarecomprastr)

        valortotaloperacaostr = request.POST.get('fac_valortotaloperacao')
        valortotaloperacaostr = valortotaloperacaostr.replace(',', '.')
        clientes.fac_valortotaloperacao = float(valortotaloperacaostr)
        # Certifique-se de que factoring.data_cadastro é um objeto datetime
        clientes.fac_datacadastro = datetime.strptime(request.POST.get('fac_datacadastro'), '%Y-%m-%d')
        datacadastro_formatada = clientes.fac_datacadastro.strftime('%Y-%m-%d')
        clientes.save()
        return redirect('listar_factorings')
    return render(request, 'editar_factorings.html', {'clientes': clientes})
def editar_factorings2(request, id):
    clientes=Dfactoring.objects.get(fac_id=id)
    form = DFactoringForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_factorings')
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
    return render(request, 'inserir_pessoas.html', {'form': form})
def listar_pessoas(request):
    pessoas=Dpessoas.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas':pessoas})
def editar_pessoas(request, id):
    pessoas = get_object_or_404(Dpessoas, pes_id=id)
    if request.method == 'POST':
        pessoas.pes_id = request.POST.get('pes_id')
        pessoas.pes_nome = request.POST.get('pes_nome')
        pessoas.pes_cpf = request.POST.get('pes_cpf')
        pessoas.pes_rg = request.POST.get('pes_rg')
        pessoas.pes_estadocivil = request.POST.get('pes_estadocivil')
        pessoas.pes_nacionalidade = request.POST.get('pes_nacionalidade')
        pessoas.pes_email1 = request.POST.get('pes_email1')
        pessoas.pes_email2 = request.POST.get('pes_email2')
        pessoas.pes_telefone1 = request.POST.get('pes_telefone1')
        pessoas.pes_telefone2 = request.POST.get('pes_telefone2')
        pessoas.pes_profissao = request.POST.get('pes_profissao')
        pessoas.pes_enderereco = request.POST.get('pes_enderereco')
        pessoas.pes_complementoenderereco = request.POST.get('pes_complementoenderereco')
        pessoas.pes_cep = request.POST.get('pes_cep')
        pessoas.pes_bairro = request.POST.get('pes_bairro')
        pessoas.pes_cidade = request.POST.get('pes_cidade')
        pessoas.pes_estado = request.POST.get('pes_estado')
        pessoas.pes_datacadastro = datetime.strptime(request.POST.get('pes_datacadastro'), '%Y-%m-%d')
        datacadastro_formatada = pessoas.pes_datacadastro.strftime('%Y-%m-%d')
        pessoas.save()
        return redirect('listar_pessoas')
    return render(request, 'editar_pessoas.html', {'pessoas': pessoas})
def editar_pessoas2(request, id):
    clientes=Dpessoas.objects.get(pes_id=id)
    form = DpessoasForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_pessoas')
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
def gerar_contrato_word(request, cma_id):
    contrato = Dcontratomae.objects.get(cma_id=cma_id)
    cliente_associado = contrato.cli_id
    factoring_associado = contrato.fac_id
    pessoas_associadas_re = Dpessoas.objects.filter(cli_id_id=contrato.cli_id.cli_id, pes_tipopessoa='RE')
    pessoas_associadas_rs = Dpessoas.objects.filter(cli_id_id=contrato.cli_id.cli_id, pes_tipopessoa='RS')
    pessoas_associadas_rt = Dpessoas.objects.filter(fac_id_id=contrato.fac_id.fac_id, pes_tipopessoa='RT')
    template_path = r"D:\Users\carlo\OneDrive - Serviço Nacional de Aprendizagem Comercial - SENAC RN\DEVE\Python_Django\Factoring\Documentos\ContratoPadrao.docx"
    # Formatação vencimento
    data_validade_contrato = contrato.cma_validadecontrato
    validade_formatada = data_validade_contrato.strftime('%d/%m/%Y')
    # Caminho de saída do documento gerado
    output_path = f"CONTRATO FOMENTO MERCANTIL - {cma_id}.docx"
    doc = DocxTemplate(template_path)
    # Defina os dados a serem inseridos no modelo
    context = {
        'ID_CONTRATO': contrato.cma_id,
        'VALIDADE_CONTRATO': validade_formatada,
        # 'ID_CLIENTE'
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': f'RAZÃO SOCIAL: ' + cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': f'CNPJ: ' + cliente_associado.cli_cnpj,
        'IM_CLIENTE': f'INSC. MUNICIPAL: ' + cliente_associado.cli_im,
        'IE_CLIENTE': f'INSC. ESTADUAL: ' + cliente_associado.cli_ie,
        'EMAIL1_CLIENTE': f'E-MAIL: ' + cliente_associado.cli_email1,
        'TELEFONE1_CLIENTE': f'TELEFONE: ' + cliente_associado.cli_telefone1,
        'ENDERECO_CLIENTE': f'ENDEREÇO: ' + cliente_associado.cli_enderereco,
        'COMPLEMENTOENDERECO_CLIENTE':f'COMPLEMENTO: ' +  cliente_associado.cli_complementoenderereco,
        'CEP_CLIENTE': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO_CLIENTE': f'BAIRRO: ' + cliente_associado.cli_bairro,
        'CIDADE_CLIENTE': f'CIDADE: ' + cliente_associado.cli_cidade,
        'ESTADO_CLIENTE': f'ESTADO: ' + cliente_associado.cli_estado,
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING':f'RAZÃO SOCIAL: ' +  factoring_associado.fac_razaosocial,
        'CNPJ_FACTORING':f'CNPJ: ' +  factoring_associado.fac_cnpj,
        'IM_FACTORING': f'INSC. MUNICIPAL: ' + factoring_associado.fac_im,
        'IE_FACTORING': f'INSC. ESTADUAL: ' + factoring_associado.fac_ie,
        'EMAIL1_FACTORING': f'E-MAIL: ' + factoring_associado.fac_email1,
        'TELEFONE1_FACTORING': f'TELEFONE: ' + factoring_associado.fac_telefone1,
        'ENDERECO_FACTORING': f'ENDEREÇO: ' + factoring_associado.fac_enderereco,
        'COMPLEMENTOENDERECO_FACTORING': f'COMPLEMENTO: ' + factoring_associado.fac_complementoenderereco,
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
        'ESTADOCIVIL_PESSOA0': f'ESTADO CÍVIL: ' + pessoas_associadas_re[0].pes_estadocivil if pessoas_associadas_re else '',
        'ESTADOCIVIL_PESSOA1': f'ESTADO CÍVIL: ' + pessoas_associadas_re[1].pes_estadocivil if len(pessoas_associadas_re) > 1 else '',
        'NACIONALIDADE_PESSOA0': f'NACIONALIDADE: ' + pessoas_associadas_re[0].pes_nacionalidade if pessoas_associadas_re else '',
        'NACIONALIDADE_PESSOA1': f'NACIONALIDADE: ' + pessoas_associadas_re[1].pes_nacionalidade if len(pessoas_associadas_re) > 1 else '',
        'EMAIL1_PESSOA0': f'E-MAIL: ' + pessoas_associadas_re[0].pes_email1 if pessoas_associadas_re else '',
        'EMAIL1_PESSOA1': f'E-MAIL: ' + pessoas_associadas_re[1].pes_email1 if len(pessoas_associadas_re) > 1 else '',
        'TELEFONE1_PESSOA0': f'TELEFONE: ' + pessoas_associadas_re[0].pes_telefone1 if pessoas_associadas_re else '',
        'TELEFONE1_PESSOA1': f'TELEFONE: ' + pessoas_associadas_re[1].pes_telefone1 if len(pessoas_associadas_re) > 1 else '',
        'PROFISSAO_PESSOA0': f'PROFISSÃO: ' + pessoas_associadas_re[0].pes_profissao if pessoas_associadas_re else '',
        'PROFISSAO_PESSOA1': f'PROFISSÃO: ' + pessoas_associadas_re[1].pes_profissao if len(pessoas_associadas_re) > 1 else '',
        'ENDERECO_PESSOA0': f'ENDEREÇO: ' + pessoas_associadas_re[0].pes_enderereco if pessoas_associadas_re else '',
        'ENDERECO_PESSOA1': f'ENDEREÇO: ' + pessoas_associadas_re[1].pes_enderereco if len(pessoas_associadas_re) > 1 else '',
        'COMPLEMENTOENDERECO_PESSOA0': f'COMPLEMENTO: ' + pessoas_associadas_re[0].pes_complementoenderereco if pessoas_associadas_re else '',
        'COMPLEMENTOENDERECO_PESSOA1': f'COMPLEMENTO: ' + pessoas_associadas_re[1].pes_complementoenderereco if len(pessoas_associadas_re) > 1 else '',
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
        'ESTADOCIVIL_PESSOA00': f'ESTADO CÍVIL: ' + pessoas_associadas_rs[0].pes_estadocivil if pessoas_associadas_rs else '',
        'ESTADOCIVIL_PESSOA01': f'ESTADO CÍVIL: ' + pessoas_associadas_rs[1].pes_estadocivil if len(pessoas_associadas_rs) > 1 else '',
        'NACIONALIDADE_PESSOA00': f'NACIONALIDADE: ' + pessoas_associadas_rs[0].pes_nacionalidade if pessoas_associadas_rs else '',
        'NACIONALIDADE_PESSOA01': f'NACIONALIDADE: ' + pessoas_associadas_rs[1].pes_nacionalidade if len(pessoas_associadas_rs) > 1 else '',
        'EMAIL1_PESSOA00': f'E-MAIL: ' + pessoas_associadas_rs[0].pes_email1 if pessoas_associadas_rs else '',
        'EMAIL1_PESSOA01': f'E-MAIL: ' + pessoas_associadas_rs[1].pes_email1 if len(pessoas_associadas_rs) > 1 else '',
        'TELEFONE1_PESSOA00': f'TELEFONE: ' + pessoas_associadas_rs[0].pes_telefone1 if pessoas_associadas_rs else '',
        'TELEFONE1_PESSOA01': f'TELEFONE: ' + pessoas_associadas_rs[1].pes_telefone1 if len(pessoas_associadas_rs) > 1 else '',
        'PROFISSAO_PESSOA00': f'PROFISSÃO: ' + pessoas_associadas_rs[0].pes_profissao if pessoas_associadas_rs else '',
        'PROFISSAO_PESSOA01': f'PROFISSÃO: ' + pessoas_associadas_rs[1].pes_profissao if len(pessoas_associadas_rs) > 1 else '',
        'ENDERECO_PESSOA00': f'ENDEREÇO: ' + pessoas_associadas_rs[0].pes_enderereco if pessoas_associadas_rs else '',
        'ENDERECO_PESSOA01': f'ENDEREÇO :' + pessoas_associadas_rs[1].pes_enderereco if len(pessoas_associadas_rs) > 1 else '',
        'COMPLEMENTOENDERECO_PESSOA00': f'COMPLEMENTO: ' + pessoas_associadas_rs[0].pes_complementoenderereco if pessoas_associadas_rs else '',
        'COMPLEMENTOENDERECO_PESSOA01': f'COMPLEMENTO: ' + pessoas_associadas_rs[1].pes_complementoenderereco if len(pessoas_associadas_rs) > 1 else '',
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
        response['Content-Disposition'] = f'attachment; filename=CONTRATO FOMENTO MERCANTIL - {cma_id}.docx'
    return response
def editar_contratomae2(request, id):
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
            return redirect('listar_simulacaoid', id=novo_id)
    else:
        form = DsimulacaoForm()
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
    template_path = r"D:\Users\carlo\OneDrive - Serviço Nacional de Aprendizagem Comercial - SENAC RN\DEVE\Python_Django\Factoring\Documentos\SimulacaoPadrao.docx"     
    # Caminho de saída do documento gerado
    output_path = f"SIMULACAO OPERACAO DE FOMENTO MERCANTIL - {sim_id}.docx"
    doc = DocxTemplate(template_path)
    # Defina os dados a serem inseridos no modelo
    context = {
        'ID_SIM': simulacao.sim_id,
        'DATASIMULACAO': simulacao.sim_datasimulacao.strftime('%d/%m/%Y'),
        'PRAZOME': f'{round(((simulacao.sim_prazo1 * simulacao.sim_valortotal1) + (simulacao.sim_prazo2 * simulacao.sim_valortotal2) + (simulacao.sim_prazo3 * simulacao.sim_valortotal3) + (simulacao.sim_prazo4 * simulacao.sim_valortotal4) + (simulacao.sim_prazo5 * simulacao.sim_valortotal5) +  (simulacao.sim_prazo6 * simulacao.sim_valortotal6)) /  (simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6),0):.0f}'.replace('.', ','),
        'FATORNOM': f'{simulacao.sim_taxadecompra}%'.replace('.', ','),
        'TAXAEFE': f'{simulacao.sim_taxadecompraefetiva1}%'.replace('.', ','),
        'FATORPERI': f'{round(((simulacao.sim_taxaperiodo1 * simulacao.sim_valortotal1) + (simulacao.sim_taxaperiodo2 * simulacao.sim_valortotal2) + (simulacao.sim_taxaperiodo3 * simulacao.sim_valortotal3) + (simulacao.sim_taxaperiodo4 * simulacao.sim_valortotal4) + (simulacao.sim_taxaperiodo5 * simulacao.sim_valortotal5) + (simulacao.sim_taxaperiodo6 * simulacao.sim_valortotal6)) / (simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6), 2):.2f}%'.replace('.', ','),    
        'IOF': f'{round((simulacao.sim_iof), 2):.2f}%',
        'IOFA': f'{round((simulacao.sim_iofadicional), 2):.2f}%',
        'TAXA': f'{round((simulacao.sim_taxadecompra), 2):.2f}%',
        # 'ID_CLIENTE
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': cliente_associado.cli_cnpj,
        'EMAIL1_CLIENTE': cliente_associado.cli_email1,
        'TELEFONE1_CLIENTE': cliente_associado.cli_telefone1,
        'ENDERECO_CLIENTE': cliente_associado.cli_enderereco,
        'COMPLEMENTO_CLIENTE': cliente_associado.cli_complementoenderereco,
        'CEP': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO': f'BAIRRO: ' + cliente_associado.cli_bairro,
        'CIDADE': f'CIDADE: ' + cliente_associado.cli_cidade,
        'ESTADO': f'ESTADO: ' + cliente_associado.cli_estado,
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING': factoring_associado.fac_razaosocial,        
        # 'SIMULACOES 1 A 6'
        'VALTT1': f' {simulacao.sim_valortotal1:,.2f}'.replace(',', '.'),
        'VALTT2': f' {simulacao.sim_valortotal2:,.2f}'.replace(',', '.'),
        'VALTT3': f' {simulacao.sim_valortotal3:,.2f}'.replace(',', '.'),
        'VALTT4': f' {simulacao.sim_valortotal4:,.2f}'.replace(',', '.'),
        'VALTT5': f' {simulacao.sim_valortotal5:,.2f}'.replace(',', '.'),
        'VALTT6': f' {simulacao.sim_valortotal6:,.2f}'.replace(',', '.'),
        'VENC1': simulacao.sim_vencimento1.strftime('%d/%m/%Y'),
        'VENC2': simulacao.sim_vencimento2.strftime('%d/%m/%Y'),
        'VENC3': simulacao.sim_vencimento3.strftime('%d/%m/%Y'),
        'VENC4': simulacao.sim_vencimento4.strftime('%d/%m/%Y'),
        'VENC5': simulacao.sim_vencimento5.strftime('%d/%m/%Y'),
        'VENC6': simulacao.sim_vencimento6.strftime('%d/%m/%Y'),
        'FLOAT': simulacao.sim_myfloat,
        'PRAZO1': simulacao.sim_prazo1,
        'PRAZO2': simulacao.sim_prazo2,
        'PRAZO3': simulacao.sim_prazo3,
        'PRAZO4': simulacao.sim_prazo4,
        'PRAZO5': simulacao.sim_prazo5,
        'PRAZO6': simulacao.sim_prazo6,
        'COMPRA1': f' {simulacao.sim_valorcompra1:,.2f}'.replace(',', '.'),
        'COMPRA2': f' {simulacao.sim_valorcompra2:,.2f}'.replace(',', '.'),
        'COMPRA3': f' {simulacao.sim_valorcompra3:,.2f}'.replace(',', '.'),
        'COMPRA4': f' {simulacao.sim_valorcompra4:,.2f}'.replace(',', '.'),
        'COMPRA5': f' {simulacao.sim_valorcompra5:,.2f}'.replace(',', '.'),
        'COMPRA6': f' {simulacao.sim_valorcompra6:,.2f}'.replace(',', '.'),
        'FATOR1': simulacao.sim_taxaperiodo1,
        'FATOR2': simulacao.sim_taxaperiodo2,
        'FATOR3': simulacao.sim_taxaperiodo3,
        'FATOR4': simulacao.sim_taxaperiodo4,
        'FATOR5': simulacao.sim_taxaperiodo5,
        'FATOR6': simulacao.sim_taxaperiodo6,
        'FCOMPRA1': f' {(simulacao.sim_valortotal1 - simulacao.sim_valorcompra1):,.2f}'.replace(',', '.'),
        'FCOMPRA2': f' {(simulacao.sim_valortotal2 - simulacao.sim_valorcompra2):,.2f}'.replace(',', '.'),
        'FCOMPRA3': f' {(simulacao.sim_valortotal3 - simulacao.sim_valorcompra3):,.2f}'.replace(',', '.'),
        'FCOMPRA4': f' {(simulacao.sim_valortotal4 - simulacao.sim_valorcompra4):,.2f}'.replace(',', '.'),
        'FCOMPRA5': f' {(simulacao.sim_valortotal5 - simulacao.sim_valorcompra5):,.2f}'.replace(',', '.'),
        'FCOMPRA6': f' {(simulacao.sim_valortotal6 - simulacao.sim_valorcompra6):,.2f}'.replace(',', '.'),
        'IOF1': f' {simulacao.sim_valoriof1:,.2f}'.replace(',', '.'),
        'IOF2': f' {simulacao.sim_valoriof2:,.2f}'.replace(',', '.'),
        'IOF3': f' {simulacao.sim_valoriof3:,.2f}'.replace(',', '.'),
        'IOF4': f' {simulacao.sim_valoriof4:,.2f}'.replace(',', '.'),
        'IOF5': f' {simulacao.sim_valoriof5:,.2f}'.replace(',', '.'),
        'IOF6': f' {simulacao.sim_valoriof6:,.2f}'.replace(',', '.'),
        'IOFAD1': f' {simulacao.sim_valoriofadicional1:,.2f}'.replace(',', '.'),
        'IOFAD2': f' {simulacao.sim_valoriofadicional2:,.2f}'.replace(',', '.'),
        'IOFAD3': f' {simulacao.sim_valoriofadicional3:,.2f}'.replace(',', '.'),
        'IOFAD4': f' {simulacao.sim_valoriofadicional4:,.2f}'.replace(',', '.'),
        'IOFAD5': f' {simulacao.sim_valoriofadicional5:,.2f}'.replace(',', '.'),
        'IOFAD6': f' {simulacao.sim_valoriofadicional6:,.2f}'.replace(',', '.'),
        'DESP': f' {simulacao.sim_despesas:,.2f}'.replace(',', '.'),
        'ACRE': f' {simulacao.sim_acrescimos:,.2f}'.replace(',', '.'),
        'DEDU': f' {(-simulacao.sim_despesas + simulacao.sim_acrescimos):,.2f}'.replace(',', '.'),
        'DIFE1': f' {(simulacao.sim_valorcompra1 + simulacao.sim_valoriof1 + simulacao.sim_valoriofadicional1 + simulacao.sim_despesas - simulacao.sim_acrescimos):,.2f}'.replace(',', '.'),
        'DIFE2': f' {(simulacao.sim_valorcompra2 + simulacao.sim_valoriof2 + simulacao.sim_valoriofadicional2):,.2f}'.replace(',', '.'),
        'DIFE3': f' {(simulacao.sim_valorcompra3 + simulacao.sim_valoriof3 + simulacao.sim_valoriofadicional3):,.2f}'.replace(',', '.'),
        'DIFE4': f' {(simulacao.sim_valorcompra4 + simulacao.sim_valoriof4 + simulacao.sim_valoriofadicional4):,.2f}'.replace(',', '.'),
        'DIFE5': f' {(simulacao.sim_valorcompra5 + simulacao.sim_valoriof5 + simulacao.sim_valoriofadicional5):,.2f}'.replace(',', '.'),
        'DIFE6': f' {(simulacao.sim_valorcompra6 + simulacao.sim_valoriof6 + simulacao.sim_valoriofadicional6):,.2f}'.replace(',', '.'),
        'LIQUIDO1': f' {simulacao.sim_valorliquido1:,.2f}'.replace(',', '.'),
        'LIQUIDO2': f' {simulacao.sim_valorliquido2:,.2f}'.replace(',', '.'),
        'LIQUIDO3': f' {simulacao.sim_valorliquido3:,.2f}'.replace(',', '.'),
        'LIQUIDO4': f' {simulacao.sim_valorliquido4:,.2f}'.replace(',', '.'),
        'LIQUIDO5': f' {simulacao.sim_valorliquido5:,.2f}'.replace(',', '.'),
        'LIQUIDO6': f' {simulacao.sim_valorliquido6:,.2f}'.replace(',', '.'),
        'VALTT': f' {(simulacao.sim_valortotal1 + simulacao.sim_valortotal2 + simulacao.sim_valortotal3 + simulacao.sim_valortotal4 + simulacao.sim_valortotal5 + simulacao.sim_valortotal6):,.2f}'.replace(',', '.'),
        'COUNT': (sum(1 for valor in [simulacao.sim_valortotal1, simulacao.sim_valortotal2, simulacao.sim_valortotal3, simulacao.sim_valortotal4, simulacao.sim_valortotal5, simulacao.sim_valortotal6] if valor is not None)),
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
        response['Content-Disposition'] = f'attachment; filename=SIMULACAO OPERACAO DE FOMENTO MERCANTIL - {sim_id}.docx'
    return response
def editar_simulacao2(request, id):
    simulacao=Dsimulacao.objects.get(sim_id=id)
    form = DsimulacaoForm(request.POST or None, instance=simulacao)
    if form.is_valid():
        form.save()
        return redirect('listar_simulacaocopy')
    return render(request, 'inserir_simulacao.html', {'form':form})

def inserir_operacao(request, id):
    try:
        print("Entrou na função inserir_operacao")
        if request.method == 'POST':
            print("Método é POST")
            form = DoperacaoForm(request.POST)
            if form.is_valid():
                nova_operacao = form.save()
                novo_id = nova_operacao.ope_id
                print(f"Nova operação inserida com ID: {novo_id}")
                return redirect('listar_operacaoid', id=novo_id)
            else:
                print("Formulário não é válido")
                print(f"Erros no formulário: {form.errors}")
        else:
            print("Método não é POST")
            form = DoperacaoForm()
    except Exception as e:
        print(f"Erro ao inserir operação: {e}")
        raise
    print("Saindo da função inserir_operacao")
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
    template_path = r"D:\Users\carlo\OneDrive - Serviço Nacional de Aprendizagem Comercial - SENAC RN\DEVE\Python_Django\Factoring\Documentos\OperacaoPadrao.docx"     
    # Caminho de saída do documento gerado
    output_path = f"OPERACAO DE FOMENTO MERCANTIL - {ope_id}.docx"
    doc = DocxTemplate(template_path)
    # Defina os dados a serem inseridos no modelo
    context = {        
        'ID_OPE': operacao.ope_id,
        'DATAOPERACAO': operacao.ope_dataoperacao.strftime('%d/%m/%Y'),
        # 'ID_CONTRATOMAE
        "CONTRATOMAE" : contratomae_associado.cma_id,
        "DATACONTRATOMAE" : contratomae_associado.cma_datacadastro.strftime('%d/%m/%Y'),
        # 'ID_CLIENTE
        'ID_CLIENTE': cliente_associado.cli_id,
        'RAZAOSOCIAL_CLIENTE': f'Empresa: ' + cliente_associado.cli_razaosocial,
        'CNPJ_CLIENTE': f'CNPJ: ' + cliente_associado.cli_cnpj,        
        # 'ID_FACTORING'
        'ID_FACTORING': factoring_associado.fac_id,
        'RAZAOSOCIAL_FACTORING': f'Empresa: ' + factoring_associado.fac_razaosocial,
        'CNPJ_FACTORING': f'CNPJ: ' + factoring_associado.fac_cnpj,
        # 'OPERAÇÕES1 A 6'
        'NUMTITULO1': operacao.ope_numtitulo1,
        'NUMTITULO2': operacao.ope_numtitulo2,
        'NUMTITULO3': operacao.ope_numtitulo3,
        'NUMTITULO4': operacao.ope_numtitulo4,
        'NUMTITULO5': operacao.ope_numtitulo5,
        'NUMTITULO6': operacao.ope_numtitulo6,
        'NOMESACADO1': operacao.ope_razaosocial1,
        'NOMESACADO2': operacao.ope_razaosocial2,
        'NOMESACADO3': operacao.ope_razaosocial3,
        'NOMESACADO4': operacao.ope_razaosocial4,
        'NOMESACADO5': operacao.ope_razaosocial5,
        'NOMESACADO6': operacao.ope_razaosocial6,        
        'VALTT1': f' {operacao.ope_valortotal1:,.2f}'.replace(',', '.'),
        'VALTT2': f' {operacao.ope_valortotal2:,.2f}'.replace(',', '.'),
        'VALTT3': f' {operacao.ope_valortotal3:,.2f}'.replace(',', '.'),
        'VALTT4': f' {operacao.ope_valortotal4:,.2f}'.replace(',', '.'),
        'VALTT5': f' {operacao.ope_valortotal5:,.2f}'.replace(',', '.'),
        'VALTT6': f' {operacao.ope_valortotal6:,.2f}'.replace(',', '.'),
        'VENC1': operacao.ope_vencimento1.strftime('%d/%m/%Y'),
        'VENC2': operacao.ope_vencimento2.strftime('%d/%m/%Y'),
        'VENC3': operacao.ope_vencimento3.strftime('%d/%m/%Y'),
        'VENC4': operacao.ope_vencimento4.strftime('%d/%m/%Y'),
        'VENC5': operacao.ope_vencimento5.strftime('%d/%m/%Y'),
        'VENC6': operacao.ope_vencimento6.strftime('%d/%m/%Y'),
        'DESP': f' {operacao.ope_despesas:,.2f}'.replace(',', '.'),
        'ACRE': f' {operacao.ope_acrescimos:,.2f}'.replace(',', '.'),
        'VALTT': f' {(operacao.ope_valortotal1 + operacao.ope_valortotal2 + operacao.ope_valortotal3 + operacao.ope_valortotal4 + operacao.ope_valortotal5 + operacao.ope_valortotal6):,.2f}'.replace(',', '.'),
        'COUNT': (sum(1 for valor in [operacao.ope_valortotal1, operacao.ope_valortotal2, operacao.ope_valortotal3, operacao.ope_valortotal4, operacao.ope_valortotal5, operacao.ope_valortotal6] if valor is not None)),
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
        response['Content-Disposition'] = f'attachment; filename=OPERACAO DE FOMENTO MERCANTIL - {ope_id}.docx'
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
    template_path = r"D:\Users\carlo\OneDrive - Serviço Nacional de Aprendizagem Comercial - SENAC RN\DEVE\Python_Django\Factoring\Documentos\NotaPromissoriaPadrao.docx"         
    output_path = f"NOTA PROMISSORIA - {ope_id}.docx"
    doc = DocxTemplate(template_path)
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
        'ENDERECO_CLIENTE': f'ENDEREÇO: ' + cliente_associado.cli_enderereco,
        'COMPLEMENTOENDERECO_CLIENTE':f'COMPLEMENTO: ' +  cliente_associado.cli_complementoenderereco,
        'CEP_CLIENTE': f'CEP: ' + cliente_associado.cli_cep,
        'BAIRRO_CLIENTE': cliente_associado.cli_bairro,
        'CIDADE_CLIENTE': cliente_associado.cli_cidade,
        'ESTADO_CLIENTE': cliente_associado.cli_estado,
        # 'OPERAÇÕES1 A 6'                        
        'VENC1': operacao.ope_vencimento1.strftime('%d/%m/%Y'),
        'VENC2': operacao.ope_vencimento2.strftime('%d/%m/%Y'),
        'VENC3': operacao.ope_vencimento3.strftime('%d/%m/%Y'),
        'VENC4': operacao.ope_vencimento4.strftime('%d/%m/%Y'),
        'VENC5': operacao.ope_vencimento5.strftime('%d/%m/%Y'),
        'VENC6': operacao.ope_vencimento6.strftime('%d/%m/%Y'),        
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
        'ENDERECO_PES00': f'Endereço:: ' + pessoas_associadas_rs[0].pes_enderereco if pessoas_associadas_rs else '',
        'ENDERECO_PES01': f'Endereço: ' + pessoas_associadas_rs[1].pes_enderereco if len(pessoas_associadas_rs) > 1 else '',
        'COMPLEENDE_PES00': pessoas_associadas_rs[0].pes_complementoenderereco if pessoas_associadas_rs else '',
        'COMPLEENDE_PES01': pessoas_associadas_rs[1].pes_complementoenderereco if len(pessoas_associadas_rs) > 1 else '',
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
        response['Content-Disposition'] = f'attachment; filename=NOTA PROMISSORIA - {ope_id}.docx'
    return response