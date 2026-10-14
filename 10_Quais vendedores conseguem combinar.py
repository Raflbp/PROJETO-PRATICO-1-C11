#10) Quais vendedores conseguem combinar alto volume de vendas com boas avaliações dos clientes?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os datasets
order_items = pd.read_csv('datasets\\olist_order_items_dataset.csv', delimiter=',')
order_reviews = pd.read_csv('datasets\\olist_order_reviews_dataset.csv', delimiter=',')
sellers = pd.read_csv('datasets\\olist_sellers_dataset.csv', delimiter=',')

# Mesclando os datasets de itens de pedidos e avaliações de pedidos com base no 'order_id'
items_review = pd.merge(order_items, order_reviews[['order_id', 'review_score']], on='order_id', how='inner')

# Agrupando por 'seller_id' para calcular o volume de vendas e a média das avaliações
desempenho_vendedores = items_review.groupby('seller_id').agg(volume_vendas=('order_id', 'count'),media_avaliacoes=('review_score', 'mean')).reset_index()

#filtrar relevancia 
vendedores_relevantes = desempenho_vendedores[desempenho_vendedores['volume_vendas'] >= 100]

vendedores_estrela = vendedores_relevantes[(vendedores_relevantes['volume_vendas'] >= 500) & (vendedores_relevantes['media_avaliacoes'] >= 4.0)]

# 2. Juntar os Vendedores Estrela com os dados de localização
estrelas_com_local = pd.merge(vendedores_estrela, sellers, on='seller_id', how='inner')

# 3. Mostrar apenas as colunas que interessam
resultado_final = estrelas_com_local[['seller_id', 'volume_vendas', 'media_avaliacoes', 'seller_city', 'seller_state']]

# Ordenar do que mais vendeu para o que menos vendeu
resultado_final = resultado_final.sort_values(by='volume_vendas', ascending=False)

print("Localização dos Vendedores de Maior Sucesso:")
print(resultado_final.head(10)) # Mostra o Top 10

print(vendedores_estrela)

plt.pie(x=[len(vendedores_estrela), len(vendedores_relevantes) - len(vendedores_estrela), len(desempenho_vendedores) - len(vendedores_relevantes)],
        labels=['Vendedores Estrela', 'Vendedores Relevantes', 'Demais Vendedores'], autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Distribuição de Vendedores por Desempenho')
