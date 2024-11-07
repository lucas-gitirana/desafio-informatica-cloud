# Desafio - Informatica Cloud
Participante: Lucas Emanoel Gitirana

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
