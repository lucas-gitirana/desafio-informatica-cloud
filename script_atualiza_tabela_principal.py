"""
Descrição: Script para atualizar a tabela dim_pedido_cliente_endereco com dados completos de endereço
Autor: Lucas Emanoel Gitirana
Data de Criação: 2024-11-13
Última Modificação: 2024-11-13
Versão: 1.0
Contato: gitiranalucas5@gmail.com

"""

import pandas as pd

# Carrega o arquivo dim_pedido_cliente_endereco.csv
dados_principais = pd.read_csv("dim_pedido_cliente_endereco.csv")

# Carrega o arquivo de endereços atualizados
enderecos_atualizados = pd.read_csv("enderecos_atualizados.csv")

# Convertendo a coluna "CEP" para strings e removendo caracteres especiais
dados_principais["CEP"] = dados_principais["CEP"].astype(str).str.replace("-", "")
enderecos_atualizados["CEP"] = enderecos_atualizados["CEP"].astype(str).str.replace("-", "")

# Unindo os dados dos dois arquivos
dados_com_endereco = dados_principais.merge(
    enderecos_atualizados,
    left_on="CEP",
    right_on="CEP",
    how="left"
)

# Removendo a coluna de CEP duplicada
dados_com_endereco.drop(columns=["CEP"], inplace=True)

# Salvando o novo arquivo CSV
dados_com_endereco.to_csv("dim_pedido_cliente_endereco_atualizada.csv", index=False)

print("Arquivo 'dim_pedido_cliente_endereco_atualizada.csv' criado com sucesso!")