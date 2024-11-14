# Desafio - Informatica Cloud
Participante: Lucas Emanoel Gitirana

Sumário:
- [Configuração de conexão das sources](#configuração-de-conexão-das-sources)
- [Configuração de conexão dos targets](#configuração-de-conexão-dos-targets)
- [Estrutura do Mapeamento](#estrutura-do-mapeamento)
  - [join_pedido_cliente](#join_pedido_cliente)
  - [join_pedido_cliente_endereco](#join_pedido_cliente_endereco)
  - [exp_calcula_idade](#exp_calcula_idade)
  - [filtro_idade_18_65 e tabela clientes_18_a_65](#filtro_idade_18_65-e-tabela-clientes_18_a_65)
  - [filtro_idade_acima_65 e tabela clientes_acima_65](#filtro_idade_acima_65-e-tabela-clientes_acima_65)
  - [tabela dim_pedido_cliente_endereco](#tabela-dim_pedido_cliente_endereco)
- [Busca de Endereços](#busca-de-endereços)
  - [script_busca_dados_enderecos](#script_busca_dados_enderecos)
  - [script_atualiza_tabela_principal](#script_atualiza_tabela_principal)

## Configuração de conexão das sources
Os arquivos clientes.csv, pedidos.csv e enderecos.csv foram alocados em uma instância da AWS S3 e seus dados foram carregados para o mapeamento conforme figuras abaixo.

Arquivos na AWS S3:  
![image](https://github.com/user-attachments/assets/9424f0fe-5a54-420e-b955-0af983a43ddd)

Conexão com AWS:  
![image](https://github.com/user-attachments/assets/bab52da9-5e5a-47f6-b0d5-e7174db98268)

O conteúdo dos arquivos de fonte de dados foram preenchidos com informações aleatórias. Abaixo seguem os exemplos:

clientes.csv:  
id_cliente,nome,email,telefone,data_nascimento,sexo,data_cadastro  
1,Ana Silva,ana.silva@email.com,(11)98765-4321,1985-06-12,F,2020-01-15  
2,João Pereira,joao.pereira@email.com,(21)99876-5432,1970-04-22,M,2021-03-10  
3,Marcos Oliveira,marcos.oliveira@email.com,(31)91234-5678,1995-11-30,M,2022-07-18  
4,Clara Souza,clara.souza@email.com,(19)92345-6789,2002-01-25,F,2019-09-01  
5,Carlos Mendes,carlos.mendes@email.com,(41)94567-8910,1955-10-05,M,2020-06-08  

pedidos.csv  
id_pedido,id_cliente,data_pedido,valor,status_pedido,forma_pagamento,data_envio,data_entrega  
101,1,2023-01-10,150.00,Entregue,Cartão de Crédito,2023-01-12,2023-01-15  
102,2,2023-02-18,250.00,Cancelado,Boleto Bancário,2023-02-19,NULL  
103,3,2023-03-25,320.50,Em trânsito,Pix,2023-03-26,NULL  
104,4,2023-04-05,85.75,Entregue,Cartão de Crédito,2023-04-07,2023-04-10  
105,5,2023-05-12,600.00,Entregue,Boleto Bancário,2023-05-14,2023-05-18  

enderecos.csv  
id_cliente,CEP,Tipo  
1,01001-000,Entrega  
1,01001-000,Cobrança  
2,20020-040,Entrega  
3,30130-000,Entrega  
4,13040-050,Entrega  
5,80420-060,Cobrança 

## Configuração de conexão dos targets
Os arquivos dim_pedido_cliente_endereco.csv, clientes_acima_65.csv e clientes_18_a_65.csv, por sua vez, foram armazenados localmente utilizando o Secure Agent. A conexão criada pode ser visualizada abaixo.

Conexão com arquivo local:  
![image](https://github.com/user-attachments/assets/6f32dd90-2c1b-4e34-aa6d-9dce5a3af547)

Após a execução do mapeamento utilizando os arquivos mencionados acima, o resultado obtido foi:

dim_pedido_cliente_endereco.csv  
"id_pedido","id_cliente","nome","email","telefone","data_nascimento","sexo","data_cadastro","idade","data_pedido","valor","status_pedido","forma_pagamento","data_envio","data_entrega","CEP","tipo_endereco"  
"101","1","Ana Silva","ana.silva@email.com","(11)98765-4321","1985-06-12","F","2020-01-15","39","2023-01-10","150.00","Entregue","Cartão de Crédito","2023-01-12","2023-01-15","01001-000","Entrega"  
"101","1","Ana Silva","ana.silva@email.com","(11)98765-4321","1985-06-12","F","2020-01-15","39","2023-01-10","150.00","Entregue","Cartão de Crédito","2023-01-12","2023-01-15","01001-000","Cobrança"  
"102","2","João Pereira","joao.pereira@email.com","(21)99876-5432","1970-04-22","M","2021-03-10","55","2023-02-18","250.00","Cancelado","Boleto Bancário","2023-02-19","NULL","20020-040","Entrega"  
"103","3","Marcos Oliveira","marcos.oliveira@email.com","(31)91234-5678","1995-11-30","M","2022-07-18","29","2023-03-25","320.50","Em trânsito","Pix","2023-03-26","NULL","30130-000","Entrega"  
"104","4","Clara Souza","clara.souza@email.com","(19)92345-6789","2002-01-25","F","2019-09-01","23","2023-04-05","85.75","Entregue","Cartão de Crédito","2023-04-07","2023-04-10","13040-050","Entrega"  
"105","5","Carlos Mendes","carlos.mendes@email.com","(41)94567-8910","1955-10-05","M","2020-06-08","69","2023-05-12","600.00","Entregue","Boleto Bancário","2023-05-14","2023-05-18","80420-060","Cobrança" 

clientes_acima_65.csv  
"id_cliente","nome","email","telefone","data_nascimento","idade","sexo","data_cadastro"  
"5","Carlos Mendes","carlos.mendes@email.com","(41)94567-8910","1955-10-05","69","M","2020-06-08"  

clientes_18_a_65.csv  
"id_cliente","nome","email","telefone","data_nascimento","idade","sexo","data_cadastro"  
"1","Ana Silva","ana.silva@email.com","(11)98765-4321","1985-06-12","39","F","2020-01-15"  
"1","Ana Silva","ana.silva@email.com","(11)98765-4321","1985-06-12","39","F","2020-01-15"  
"2","João Pereira","joao.pereira@email.com","(21)99876-5432","1970-04-22","55","M","2021-03-10"  
"3","Marcos Oliveira","marcos.oliveira@email.com","(31)91234-5678","1995-11-30","29","M","2022-07-18"  
"4","Clara Souza","clara.souza@email.com","(19)92345-6789","2002-01-25","23","F","2019-09-01"  

## Estrutura do Mapeamento
A fim de obter os dados para as três tabelas finais, foram adicionados dois joins, uma expressão e dois filtros. Abaixo, seguem os detalhes dos elementos utilizados.

### join_pedido_cliente  
Realiza a junção dos dados das tabelas pedido e cliente pelo id do cliente.  
![image](https://github.com/user-attachments/assets/3e6998b7-3f5f-4efc-a51a-d97a87519fd0)  

### join_pedido_cliente_endereco
Realiza a junção dos dados resultantes do join_pedido_cliente com os dados da tabela de enderecos pelo id do cliente.  
![image](https://github.com/user-attachments/assets/ae911f8f-eb9d-47d3-a050-b7127f806950)

Visualização dos joins no mapa:  
![image](https://github.com/user-attachments/assets/6874bd72-a75b-4bb4-b7d7-41642d6ef17a)

## exp_calcula_idade
Expressão criada para gerar a coluna que servirá como filtro para as tabelas auxiliares. Por meio dela, os dados de data de nascimento dos clientes são transformados em idade e adicionados aos dados obtidos a partir dos joins anteriores.

Campos recebidos pela expressão:  
![image](https://github.com/user-attachments/assets/3edf4ae3-f169-4391-a4c6-c09ea01b7ebd)

Expressão:  
![image](https://github.com/user-attachments/assets/c989fe55-ad0a-4b19-9dc3-530d3d0ec933)

## filtro_idade_18_65 e tabela clientes_18_a_65
Filtra os registros cujos clientes possuem idade entre 18 e 65 anos e popula a tabela clientes_18_a_65.

Filtro:  
![image](https://github.com/user-attachments/assets/0b1a1a53-9b7f-403b-905a-0b9e951326eb)

Tabela resultante:  
![image](https://github.com/user-attachments/assets/2b4b8b3a-b99e-40a4-b978-056be6bc9e80)

## filtro_idade_acima_65 e tabela clientes_acima_65
Filtra os registros cujos clientes possuem idade acima de 65 anos e popula a tabela clientes_acima_65.

Filtro:  
![image](https://github.com/user-attachments/assets/2377d3b5-f199-40cc-94fe-786bcfe3e34c)

Tabela resultante:  
![image](https://github.com/user-attachments/assets/066e3350-9114-4c3d-9675-8a82c0544740)

## tabela dim_pedido_cliente_endereco
Esta é a tabela principal da integração, pois reúne todos os registros, independentemente da idade. Os dados obtidos a partir dos joins e da expression não são filtrados.

Tabela:  
![image](https://github.com/user-attachments/assets/2ad4f69c-6207-416a-b9f9-99862233cb1f)

Visualização dos filtros e tabelas finais no mapa:  
![image](https://github.com/user-attachments/assets/59db5075-22a2-4f0b-bad7-d6af117c1765)

## Busca de Endereços
A fim de complementar os endereços dos clientes com dados de logradouro, bairro, cidade e estado, foram desenvolvidos dois scripts em Python, responsáveis por carregar os dados completos de endereço da BrasilAPI com base no CEP e atualizar a tabela dim_pedido_cliente_endereco com as novas informações obtidas. A seguir, segue uma breve explicação sobre cada algoritmo.

## script_busca_dados_enderecos
Carrega os dados adicionais dos endereços a partir dos seguintes passos:
1. Cria um dataframe com base nas colunas do arquivo "endereco.csv" somadas às colunas de logradouro, bairro, cidade e estado  
2. Percorre cada linha do arquivo "enderecos.csv"  
3. Carrega os dados do endereço da BrasilAPI utilizando o CEP
4. Ao final, cria um novo arquivo com os endereços completos

Resultado:  
id_cliente,CEP,Tipo,logradouro,bairro,cidade,estado  
1,01001-000,Entrega,Praça da Sé,Sé,São Paulo,SP  
1,01001-000,Cobrança,Praça da Sé,Sé,São Paulo,SP  
2,20020-040,Entrega,Praça Ana Amélia,Centro,Rio de Janeiro,RJ  
3,30130-000,Entrega,Avenida Afonso Pena,Centro,Belo Horizonte,MG  
4,13040-050,Entrega,Não disponível,Não disponível,Não disponível,Não disponível  
5,80420-060,Cobrança,Alameda Dom Pedro II,Batel,Curitiba,PR  

## script_atualiza_tabela_principal
Atualiza os dados da tabela dim_pedido_cliente_endereco com os endereços completos a partir dos seguintes passos:
1. Carrega os arquivos dim_pedido_cliente_endereco.csv e enderecos_atualizados.csv
2. Trata os valores e une os dados dos dois arquivos utilizando o CEP
3. Cria um novo arquivo "clone" com os dados atualizados

Resultado:  
id_pedido,id_cliente_x,nome,email,telefone,data_nascimento,sexo,data_cadastro,idade,data_pedido,valor,status_pedido,forma_pagamento,data_envio,data_entrega,tipo_endereco,id_cliente_y,Tipo,logradouro,bairro,cidade,estado
101,1,Ana Silva,ana.silva@email.com,(11)98765-4321,1985-06-12,F,2020-01-15,39,2023-01-10,150.0,Entregue,Cartão de Crédito,2023-01-12,2023-01-15,Entrega,1,Entrega,Praça da Sé,Sé,São Paulo,SP  
101,1,Ana Silva,ana.silva@email.com,(11)98765-4321,1985-06-12,F,2020-01-15,39,2023-01-10,150.0,Entregue,Cartão de Crédito,2023-01-12,2023-01-15,Entrega,1,Cobrança,Praça da Sé,Sé,São Paulo,SP  
101,1,Ana Silva,ana.silva@email.com,(11)98765-4321,1985-06-12,F,2020-01-15,39,2023-01-10,150.0,Entregue,Cartão de Crédito,2023-01-12,2023-01-15,Cobrança,1,Entrega,Praça da Sé,Sé,São Paulo,SP  
101,1,Ana Silva,ana.silva@email.com,(11)98765-4321,1985-06-12,F,2020-01-15,39,2023-01-10,150.0,Entregue,Cartão de Crédito,2023-01-12,2023-01-15,Cobrança,1,Cobrança,Praça da Sé,Sé,São Paulo,SP  
102,2,João Pereira,joao.pereira@email.com,(21)99876-5432,1970-04-22,M,2021-03-10,55,2023-02-18,250.0,Cancelado,Boleto Bancário,2023-02-19,,Entrega,2,Entrega,Praça Ana Amélia,Centro,Rio de Janeiro,RJ  
103,3,Marcos Oliveira,marcos.oliveira@email.com,(31)91234-5678,1995-11-30,M,2022-07-18,29,2023-03-25,320.5,Em trânsito,Pix,2023-03-26,,Entrega,3,Entrega,Avenida Afonso Pena,Centro,Belo Horizonte,MG  
104,4,Clara Souza,clara.souza@email.com,(19)92345-6789,2002-01-25,F,2019-09-01,23,2023-04-05,85.75,Entregue,Cartão de Crédito,2023-04-07,2023-04-10,Entrega,4,Entrega,Não disponível,Não disponível,Não disponível,Não disponível  
105,5,Carlos Mendes,carlos.mendes@email.com,(41)94567-8910,1955-10-05,M,2020-06-08,69,2023-05-12,600.0,Entregue,Boleto Bancário,2023-05-14,2023-05-18,Cobrança,5,Cobrança,Alameda Dom Pedro II,Batel,Curitiba,PR  

