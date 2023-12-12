from .models import *
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import JsonResponse, HttpResponse
from docx import Document
from docx.shared import Pt
from django.core.serializers.json import DjangoJSONEncoder
import json
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
    template_path = r"D:\Users\carlo\OneDrive - Serviço Nacional de Aprendizagem Comercial - SENAC RN\DEVE\Python_Django\Factoring\modelo.docx"  
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
