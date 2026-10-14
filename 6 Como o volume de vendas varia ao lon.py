#6) Como o volume de vendas varia ao longo do tempo e quais períodos apresentam maior demanda?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#impotando a base de dados
orders = pd.read_csv('datasets\\olist_orders_dataset.csv', delimiter=',')

# Convertendo a coluna de data para o tipo datetime
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Inclui tudo o que for considerado uma venda efetiva
orders_validos = orders[orders['order_status'].isin(['delivered', 'invoiced', 'shipped', 'processing', 'approved'])].copy()

# Filtra os dados para manter apenas as compras feitas antes de 1º de Setembro de 2018
orders_validos = orders_validos[orders_validos['order_purchase_timestamp'] < '2018-09-01']

# separando o ano e o mês da data de compra
orders_validos['ano'] = orders_validos['order_purchase_timestamp'].dt.year
orders_validos['mes'] = orders_validos['order_purchase_timestamp'].dt.month

# Removendo o ano de 2016, pois os dados desse ano são incompletos e podem distorcer a análise
orders_validos = orders_validos[orders_validos['ano'] != 2016]

# Agrupar os dados por ano e por mês
vendas_ano_mes = orders_validos.groupby(['ano', 'mes']).size().reset_index(name='volume')

# Transformar os dados para facilitar o gráfico (linhas = meses, colunas = anos)
vendas_pivot = vendas_ano_mes.pivot(index='mes', columns='ano', values='volume')

#mostrar o volume de vendas separado por ano e mês
print("Volume de vendas separado por Ano e Mês:")
print(vendas_pivot)

# Loop para desenhar uma linha para cada ano encontrado na base de dados
for ano in vendas_pivot.columns:
    plt.plot(vendas_pivot.index, vendas_pivot[ano], marker='o', linewidth=2, label=str(ano))

plt.title('Comparativo de Volume de Vendas por Ano')
plt.xlabel('Mês do Ano')
plt.ylabel('Quantidade de Pedidos')

# Substituir os números de 1 a 12 pelos nomes dos meses no eixo X
meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
plt.xticks(range(1, 13), meses_nomes)

# Adicionar legenda, grade e mostrar o gráfico
plt.legend(title='Ano')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()