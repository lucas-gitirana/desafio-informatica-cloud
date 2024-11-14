"""
Descrição: Script para obter dados completos de endereço da BrasilAPI com base nos CEPs dos clientes
Autor: Lucas Emanoel Gitirana
Data de Criação: 2024-11-13
Última Modificação: 2024-11-13
Versão: 1.0
Contato: gitiranalucas5@gmail.com

"""

import pandas as pd
import requests
import time

# Função para buscar informações de endereços
def consultar_cep(cep):
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                return {
                    "logradouro": data.get("street", "Não disponível"),
                    "bairro": data.get("neighborhood", "Não disponível"),
                    "cidade": data.get("city", "Não disponível"),
                    "estado": data.get("state", "Não disponível")
                }
    except Exception as e:
        print(f"Erro ao consultar CEP {cep}: {e}")
    return {"logradouro": "Não disponível", "bairro": "Não disponível", "cidade": "Não disponível", "estado": "Não disponível"}

# Carregar o arquivo CSV
enderecos_df = pd.read_csv("enderecos.csv")

# Adicionando as novas colunas para armazenar os dados do endereço
enderecos_df["logradouro"] = "Não disponível"
enderecos_df["bairro"] = "Não disponível"
enderecos_df["cidade"] = "Não disponível"
enderecos_df["estado"] = "Não disponível"

# Iterando sobre cada linha do DataFrame para complementar os dados
for index, row in enderecos_df.iterrows():
    cep = str(row["CEP"]).zfill(8)  # Garantindo que o CEP tenha 8 dígitos
    print(f"Consultando CEP {cep}...")
    endereco_info = consultar_cep(cep)
    enderecos_df.loc[index, "logradouro"] = endereco_info["logradouro"]
    enderecos_df.loc[index, "bairro"] = endereco_info["bairro"]
    enderecos_df.loc[index, "cidade"] = endereco_info["cidade"]
    enderecos_df.loc[index, "estado"] = endereco_info["estado"]
    time.sleep(1)

# Salvando o novo arquivo CSV
enderecos_df.to_csv("enderecos_atualizados.csv", index=False)
print("Arquivo 'enderecos_atualizados.csv' salvo com sucesso!")