
// Funções para a máscara nos campos
// HTML Inserir Factoring
$(document).ready(function(){
    $('#fac_cnpj').mask('00.000.000/0000-00');
    $('#fac_im').mask('000.000.000');
    $('#fac_ie').mask('000.000.000.000');
    $('#fac_telefone1').mask('00 00000-0000');
    $('#fac_telefone2').mask('00 00000-0000');
    $('#fac_cep').mask('00000-000');
    $('#fac_taxacompra').mask('0.00');
    $('#fac_iof').mask('0.00');
    $('#fac_iofadicional').mask('0.00');
    $('#fac_pis').mask('0.00');
    $('#fac_cofins').mask('0.00');
    $('#fac_multa').mask('0.00');
    $('#fac_juros').mask('0.00');
    $('#fac_taxarecompra').mask('0.00');
    $('#fac_valortotaloperacao').mask('00000.00');
});
// HTML Inserir Cliente
$(document).ready(function(){
    $('#cli_cnpj').mask('00.000.000/0000-00');
    $('#cli_im').mask('000.000.000');
    $('#cli_ie').mask('000.000.000.000');
    $('#cli_telefone1').mask('00 00000-0000');
    $('#cli_telefone2').mask('00 00000-0000');
    $('#cli_cep').mask('00000-000');
    $('#cli_taxacompra').mask('0.00');
    $('#cli_multa').mask('0.00');
    $('#cli_juros').mask('0.00');
    $('#cli_taxarecompra').mask('0.00');
    $('#cli_valortotaloperacao').mask('00000.00');
});
// HTML Inserir Pessoas
$(document).ready(function(){
    $('#pes_cpf').mask('000.000.000-00')
    $('#pes_telefone1').mask('00 00000-0000')
    $('#pes_telefone2').mask('00 00000-0000')
    $('#pes_cep').mask('00000-000');

});
// HTML Inserir Simulação
$(document).ready(function(){
  $('#sim_taxacompra').mask('0.00');
  $('#sim_iof').mask('0.00');
  $('#sim_iofadicional').mask('0.00');
  $('#sim_despesas').mask('0.00');
  $('#sim_acrescimos').mask('0.00');
  $('#sim_float').mask('0');
});
// HTML Inserir Operação
$(document).ready(function(){
  $('#ope_cnpj1').mask('00.000.000/0000-00');
  $('#ope_telefone1').mask('00 00000-0000')
  $('#ope_cep1').mask('00000-000');
  $('#ope_cnpj2').mask('00.000.000/0000-00');
  $('#ope_telefone2').mask('00 00000-0000')
  $('#ope_cep2').mask('00000-000');
  $('#ope_cnpj3').mask('00.000.000/0000-00');
  $('#ope_telefone3').mask('00 00000-0000')
  $('#ope_cep3').mask('00000-000');
  $('#ope_cnpj4').mask('00.000.000/0000-00');
  $('#ope_telefone4').mask('00 00000-0000')
  $('#ope_cep4').mask('00000-000');
  $('#ope_cnpj5').mask('00.000.000/0000-00');
  $('#ope_telefone5').mask('00 00000-0000')
  $('#ope_cep5').mask('00000-000');
  $('#ope_cnpj6').mask('00.000.000/0000-00');
  $('#ope_telefone6').mask('00 00000-0000')
  $('#ope_cep6').mask('00000-000');
  $('#ope_taxacompra').mask('0.00');
  $('#ope_iof').mask('0.00');
  $('#ope_iofadicional').mask('0.00');
  $('#ope_despesas').mask('0000.00');
  $('#ope_acrescimos').mask('0000.00');
  $('#ope_recompra').mask('0000.00');
  $('#ope_juros').mask('0000.00');
  $('#ope_float').mask('0');
});

// Funções para calculos
// Funções para Calcular Simulação
function calcularsimulacao() {
  var dataSimulacao = new Date(document.getElementsByName('sim_datasimulacao')[0].value);
  var myFloat = parseFloat(document.getElementsByName('sim_float')[0].value) || 0;

  for (var i = 1; i <= 6; i++) {
    var campoVencimento = document.getElementsByName('sim_vencimento' + i)[0];
    var campoPrazo = document.getElementsByName('sim_prazo' + i)[0];
    var campoTaxaPeriodo = document.getElementsByName('sim_taxaperiodo' + i)[0];
    var campoValorCompra = document.getElementsByName('sim_valorcompra' + i)[0];
    var campoValorIOF = document.getElementsByName('sim_valoriof' + i)[0];
    var campoValorIOFadicional = document.getElementsByName('sim_valoriofadicional' + i)[0];
    var campoValorLiquido = document.getElementsByName('sim_valorliquido' + i)[0];
    var campoDespesas = document.getElementsByName('sim_despesas')[0];
    var campoAcrescimos = document.getElementsByName('sim_acrescimos')[0];

    if (campoVencimento && campoPrazo && campoTaxaPeriodo && campoValorCompra && campoValorIOF && campoValorIOFadicional && campoValorLiquido && campoDespesas && campoAcrescimos) {
      var vencimento = new Date(campoVencimento.value);
      var diferencaEmDias = Math.ceil((vencimento - dataSimulacao) / (1000 * 60 * 60 * 24));
      var resultadoComFloat = diferencaEmDias + myFloat + 2;

      if (isNaN(resultadoComFloat)) {
        campoPrazo.value = 0;
        campoTaxaPeriodo.value = 0;
        campoValorCompra.value = 0;
        campoValorIOF.value = 0;
        campoValorIOFadicional.value = 0;
        campoValorLiquido.value = 0;
      } else {
        campoPrazo.value = resultadoComFloat;

        var taxaCompra = parseFloat(document.getElementsByName('sim_taxacompra')[0].value) || 0;
        var taxaPeriodo = (taxaCompra / 30) * resultadoComFloat;
        campoTaxaPeriodo.value = taxaPeriodo.toFixed(2);

        var valortotal = parseFloat(document.getElementsByName('sim_valortotal' + i)[0].value) || 0;
        var valorCompra = (valortotal * taxaPeriodo) / 100;
        campoValorCompra.value = valorCompra.toFixed(2);

        var iof = parseFloat(document.getElementsByName('sim_iof')[0].value) || 0;
        var valoriof = (((iof / 365) * resultadoComFloat) * (valortotal - valorCompra)) / 100;
        campoValorIOF.value = valoriof.toFixed(2);

        var iofadicional = parseFloat(document.getElementsByName('sim_iofadicional')[0].value) || 0;
        var valoriofadicional = (iofadicional * (valortotal - valorCompra)) / 100;
        campoValorIOFadicional.value = valoriofadicional.toFixed(2);

        if (i === 1) {
          var despesas = parseFloat(campoDespesas.value) || 0;
          var acrescimos = parseFloat(campoAcrescimos.value) || 0;
          var valorLiquido1 = valortotal - valorCompra - valoriof - valoriofadicional - despesas + acrescimos;
          campoValorLiquido.value = valorLiquido1.toFixed(2);
        } else {
          var valorLiquido = valortotal - valorCompra - valoriof - valoriofadicional;
          campoValorLiquido.value = valorLiquido.toFixed(2);
        }
      }
    } else {              
      campoPrazo.value = 0;
      campoTaxaPeriodo.value = 0;
      campoValorCompra.value = 0;
      campoValorIOF.value = 0;
      campoValorIOFadicional.value = 0;
      campoValorLiquido.value = 0;
    }

    var campoValortotal = document.getElementsByName('sim_valortotal' + i)[0];
    var campoTaxaCompra = document.getElementsByName('sim_taxacompra')[0];
    var campoTaxaCompraEfetiva = document.getElementsByName('sim_taxadecompraefetiva' + i)[0];

    if (campoValortotal && campoTaxaCompra && campoTaxaCompraEfetiva) {
      var valortotal = parseFloat(campoValortotal.value) || 0;
      var taxaCompra = parseFloat(campoTaxaCompra.value) || 0;
      var taxaCompraEfetiva = ((valortotal * (taxaCompra / 100)) / (valortotal - (valortotal * (taxaCompra / 100)))) * 100;
      campoTaxaCompraEfetiva.value = isNaN(taxaCompraEfetiva) ? 0 : taxaCompraEfetiva.toFixed(2);
    }
  }
}

// Funções para Calcular Operação
function calcularoperacao() {
  var dataOperacao = new Date(document.getElementsByName('ope_dataoperacao')[0].value);
  var myFloat = parseFloat(document.getElementsByName('ope_float')[0].value) || 0;

  for (var i = 1; i <= 6; i++) {
    var campoVencimento = document.getElementsByName('ope_vencimento' + i)[0];
    var campoPrazo = document.getElementsByName('ope_prazo' + i)[0];
    var campoTaxaPeriodo = document.getElementsByName('ope_taxaperiodo' + i)[0];
    var campoValorCompra = document.getElementsByName('ope_valorcompra' + i)[0];
    var campoValorIOF = document.getElementsByName('ope_valoriof' + i)[0];
    var campoValorIOFadicional = document.getElementsByName('ope_valoriofadicional' + i)[0];
    var campoValorLiquido = document.getElementsByName('ope_valorliquido' + i)[0];
    var campoDespesas = document.getElementsByName('ope_despesas')[0];
    var campoAcrescimos = document.getElementsByName('ope_acrescimos')[0];
    var campoRecompra = document.getElementsByName('ope_recompra')[0];
    var campoJuros = document.getElementsByName('ope_juros')[0];
    var campoNumTitulo = document.getElementsByName('ope_numtitulo' + i)[0];
    var campoRazaoSocial = document.getElementsByName('ope_razaosocial' + i)[0];
    var campoCnpj = document.getElementsByName('ope_cnpj' + i)[0];
    var campoEmail = document.getElementsByName('ope_email' + i)[0];
    var campoTelefone = document.getElementsByName('ope_telefone' + i)[0];
    var campoNomecontato = document.getElementsByName('ope_nomecontato' + i)[0];
    var campoEndereco = document.getElementsByName('ope_endereco' + i)[0];
    var campoComplementoEndereco = document.getElementsByName('ope_complementoendereco' + i)[0];
    var campoCep = document.getElementsByName('ope_cep' + i)[0];
    var campoBairro = document.getElementsByName('ope_bairro' + i)[0];
    var campoCidade = document.getElementsByName('ope_cidade' + i)[0];
    var campoEstado = document.getElementsByName('ope_estado' + i)[0];

    if (campoVencimento && campoPrazo && campoTaxaPeriodo && campoValorCompra && campoValorIOF && campoValorIOFadicional && campoValorLiquido && campoDespesas && campoAcrescimos && campoRecompra && campoJuros) {
      var vencimento = new Date(campoVencimento.value);
      var diferencaEmDias = Math.ceil((vencimento - dataOperacao) / (1000 * 60 * 60 * 24));
      var resultadoComFloat = diferencaEmDias + myFloat + 2;

      if (isNaN(resultadoComFloat)) {
        campoPrazo.value = 0;
        campoTaxaPeriodo.value = 0;
        campoValorCompra.value = 0;
        campoValorIOF.value = 0;
        campoValorIOFadicional.value = 0;
        campoValorLiquido.value = 0;
        campoNumTitulo.value = 0;
        campoRazaoSocial.value = "";
        campoCnpj.value = "";
        campoEmail.value = "";
        campoTelefone.value = "";
        campoNomecontato.value = "";
        campoEndereco.value = "";
        campoComplementoEndereco.value = "";
        campoCep.value = "";
        campoBairro.value = "";
        campoCidade.value = "";
        campoEstado.value = "";
      } else {
        campoPrazo.value = resultadoComFloat;

        var taxaCompra = parseFloat(document.getElementsByName('ope_taxacompra')[0].value) || 0;
        var taxaPeriodo = (taxaCompra / 30) * resultadoComFloat;
        campoTaxaPeriodo.value = taxaPeriodo.toFixed(2);

        var valortotal = parseFloat(document.getElementsByName('ope_valortotal' + i)[0].value) || 0;
        var valorCompra = (valortotal * taxaPeriodo) / 100;
        campoValorCompra.value = valorCompra.toFixed(2);

        var iof = parseFloat(document.getElementsByName('ope_iof')[0].value) || 0;
        var valoriof = (((iof / 365) * resultadoComFloat) * (valortotal - valorCompra)) / 100;
        campoValorIOF.value = valoriof.toFixed(2);

        var iofadicional = parseFloat(document.getElementsByName('ope_iofadicional')[0].value) || 0;
        var valoriofadicional = (iofadicional * (valortotal - valorCompra)) / 100;
        campoValorIOFadicional.value = valoriofadicional.toFixed(2);

        if (i === 1) {
          var despesas = parseFloat(campoDespesas.value) || 0;
          var acrescimos = parseFloat(campoAcrescimos.value) || 0;
          var recompra = parseFloat(campoRecompra.value) || 0;
          var juros = parseFloat(campoJuros.value) || 0;
          var valorLiquido1 = valortotal - valorCompra - valoriof - valoriofadicional - despesas + acrescimos - recompra - juros;
          campoValorLiquido.value = valorLiquido1.toFixed(2);
        } else {
          var valorLiquido = valortotal - valorCompra - valoriof - valoriofadicional;
          campoValorLiquido.value = valorLiquido.toFixed(2);
        }
      }
    } else {
      campoPrazo.value = 0;
      campoTaxaPeriodo.value = 0;
      campoValorCompra.value = 0;
      campoValorIOF.value = 0;
      campoValorIOFadicional.value = 0;
      campoValorLiquido.value = 0;
    }

    var campoValortotal = document.getElementsByName('ope_valortotal' + i)[0];
    var campoTaxaCompra = document.getElementsByName('ope_taxacompra')[0];
    var campoTaxaCompraEfetiva = document.getElementsByName('ope_taxadecompraefetiva' + i)[0];

    if (campoValortotal && campoTaxaCompra && campoTaxaCompraEfetiva) {
      var valortotal = parseFloat(campoValortotal.value) || 0;
      var taxaCompra = parseFloat(campoTaxaCompra.value) || 0;
      var taxaCompraEfetiva = ((valortotal * (taxaCompra / 100)) / (valortotal - (valortotal * (taxaCompra / 100)))) * 100;
      campoTaxaCompraEfetiva.value = isNaN(taxaCompraEfetiva) ? 0 : taxaCompraEfetiva.toFixed(2);
    }
  }
}

// Função para converter para caixa alta
function converterParaCaixaAlta(elemento) {
    elemento.value = elemento.value.toUpperCase();
}

// Função para redirecionar para a página principal
function irParaPaginaPrincipal() {
    window.location.href = "http://127.0.0.1:8000/Inicio";
}

$(document).ready(function () {
  $("#searchInput").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $("table tbody tr").filter(function () {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
  });
});

// Função para exportar os dados para Excel
function exportToExcel() {
  const table = document.getElementById('dataTable');
  const wb = XLSX.utils.table_to_book(table, {sheet: "Sheet1"});
  XLSX.writeFile(wb, 'DadosTela.xlsx');
}