#9) Produtos com maior número de fotos apresentam melhores avaliações ou maior volume de vendas?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#carregando os datasets
products = pd.read_csv('datasets\\olist_products_dataset.csv', delimiter=',')
order_items = pd.read_csv('datasets\\olist_order_items_dataset.csv', delimiter=',')
order_reviews = pd.read_csv('datasets\\olist_order_reviews_dataset.csv', delimiter=',')

# Juntar os datasets de reviews e orders com as avaliações dos produtos
item_reviews = pd.merge(order_items,order_reviews[['order_id', 'review_score']], on='order_id', how='inner')

# Juntando com a tabela dde produtos
df_complete = pd.merge(item_reviews, products[['product_id', 'product_photos_qty']], on='product_id', how='inner')

# Agrupar calculando a MÉDIA de notas e a CONTAGEM de vendas (volume)
grouped_reviews = df_complete.groupby('product_photos_qty').agg(
    media_avaliacoes=('review_score', 'mean'),
    volume_vendas=('order_id', 'count')
).reset_index()

# Filtrar para remover os "pontos fora da curva" (produtos com mais de 10 fotos)
grouped_reviews = grouped_reviews[grouped_reviews['product_photos_qty'] <= 10]

print(grouped_reviews)


#criando a tabela
plt.bar(grouped_reviews['product_photos_qty'], grouped_reviews['media_avaliacoes'])
plt.xlabel('Quantidade de Fotos')
plt.ylabel('Média das Avaliações')
plt.title('Relação entre Quantidade de Fotos e Avaliação dos Produtos')
plt.show()