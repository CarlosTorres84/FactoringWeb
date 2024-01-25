from django.urls import path
from .views import *
from .models import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns= [
    # Página Principal
    path('Inicio', pagina_principal, name='pagina_principal'),  

    #Clientes
    path('inserir_cliente', inserir_clientes, name='inserir_clientes'),  
    path('listar_cliente', listar_clientes, name='listar_clientes'),  
    path('editar_cliente/<str:id>', editar_clientes, name='editar_clientes'),  
    path('remover_cliente/<str:id>', remover_clientes, name='remover_clientes'),  
    

    #Factorings
    path('inserir_factoring', inserir_factorings, name='inserir_factorings'),
    path('listar_factoring', listar_factorings, name='listar_factorings'),
    path('editar_factoring/<str:id>', editar_factorings, name='editar_factorings'),
    path('remover_factoring/<str:id>', remover_factorings, name='remover_factorings'),

    #Pessoas
    path('inserir_pessoa', inserir_pessoas, name='inserir_pessoas'),
    path('listar_pessoa', listar_pessoas, name='listar_pessoas'),
    path('editar_pessoa/<str:id>', editar_pessoas, name='editar_pessoas'),
    path('remover_pessoa/<str:id>', remover_pessoas, name='remover_pessoas'),    

    #Contrato Mãe
    path('inserir_contratomae', inserir_contratomae, name='inserir_contratomae'),
    path('listar_contratomae', listar_contratomae, name='listar_contratomae'),
    path('gerar_contrato_word/<int:cma_id>/', gerar_contrato_word, name='gerar_contrato_word'),
    path('editar_contratomae/<str:id>', editar_contratomae, name='editar_contratomae'),

    #Simulação
    path('inserir_simulacao', inserir_simulacao, name='inserir_simulacao'),    
    path('listar_simulacaoid/<str:id>', listar_simulacaoid, name='listar_simulacaoid'),
    path('gerar_simulacao_word/<int:sim_id>/', gerar_simulacao_word, name='gerar_simulacao_word'),
    path('listar_simulacao', listar_simulacao, name='listar_simulacao'),
    path('listar_simulacaocopy', listar_simulacaocopy, name='listar_simulacaocopy'),
    path('editar_simulacao2/<str:id>', editar_simulacao2, name='editar_simulacao2'),
    
    #Operação
    path('inserir_operacao/<int:sim_id>/', inserir_operacao, name='inserir_operacao'),
    path('listar_operacao', listar_operacao, name='listar_operacao'),
    path('gerar_operacao_word/<int:ope_id>/', gerar_operacao_word, name='gerar_operacao_word'),
    path('gerar_promissoria_word/<int:ope_id>/', gerar_promissoria_word, name='gerar_promissoria_word'),
    path('listar_operacaoid/<str:id>', listar_operacaoid, name='listar_operacaoid'),
    path('editar_operacao/<str:id>', editar_operacao, name='editar_operacao'),

    #Carteira
    path('listar_carteira', listar_carteira , name='listar_carteira'),
    path('incluir_pagamento/<int:ope_id>/<int:titulonumero>/', incluir_pagamento, name='incluir_pagamento'),

   # Configurando a servir a folha de estilo com o tipo MIME correto
    path('style0.css', serve, {'document_root': settings.STATIC_ROOT, 'path': 'style0.css', 'content_type': 'text/css'}),
]

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)