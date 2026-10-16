import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregando o dataset
order_payments = pd.read_csv('datasets\\olist_order_payments_dataset.csv', delimiter=',')

# 2. APLICANDO O FILTRO (Remove as parcelas 0)
order_payments = order_payments[order_payments['payment_installments'] >= 1]

# 3. Agrupando os dados
media_por_parcela = order_payments.groupby('payment_installments')['payment_value'].mean().reset_index()

# 4. Definindo as cores
cores = np.where(media_por_parcela['payment_value'] > 400, 'green',  
        np.where(media_por_parcela['payment_value'] < 200, 'red',   
                 'blue'))                                            

# 5. Criando o gráfico
plt.figure(figsize=(10, 6))

# Truque para a legenda aparecer corretamente
plt.bar(0, 0, color='green', label='Acima de R$ 400')
plt.bar(0, 0, color='blue', label='Entre R$ 200 e R$ 400')
plt.bar(0, 0, color='red', label='Abaixo de R$ 200')
plt.legend(title="Categorias de Valor")

# Plotando as barras principais
plt.bar(media_por_parcela['payment_installments'], media_por_parcela['payment_value'], color=cores)

# Isso força o gráfico a mostrar as barras lado a lado, usando apenas os números da sua tabela
plt.xticks(media_por_parcela['payment_installments'])

# Adicionando título e rótulos
plt.title('Valor médio das compras por número de parcelas')
plt.xlabel('Número de Parcelas')
plt.ylabel('Valor Médio')

plt.show()
