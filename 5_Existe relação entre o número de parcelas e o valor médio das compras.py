#5) Existe relação entre o número de parcelas e o valor médio das compras?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset de pagamentos
order_payments = pd.read_csv('datasets\\olist_order_payments_dataset.csv', delimiter=',')

#Agruopando o valor médio das compras por número de parcelas
media_por_parcela = order_payments.groupby('payment_installments')['payment_value'].mean().reset_index()

print(media_por_parcela)

# Criando a regra de cores com numpy (mais rápido e prático)
cores = np.where(media_por_parcela['payment_value'] > 400, 'green',  # Verde para > 500
        np.where(media_por_parcela['payment_value'] < 200, 'red',   # Vermelho para < 200
                 'blue'))                                            # Azul para os valores do meio (200 a 500)

# 3. Criando o gráfico
plt.figure(figsize=(10, 6))

plt.bar(0, 0, color='green', label='Acima de R\$ 400')
plt.bar(0, 0, color='blue', label='Entre R\$ 200 e R\$ 400')
plt.bar(0, 0, color='red', label='Abaixo de R\$ 200')

# Adicionando a legenda ao gráfico
plt.legend(title="Categorias de Valor")

# Usamos a lista 'cores' no parâmetro color
plt.bar(media_por_parcela['payment_installments'], media_por_parcela['payment_value'], color=cores)

# Adicionando título e rótulos aos eixos
plt.title('Valor médio das compras por número de parcelas')
plt.xlabel('Número de Parcelas')
plt.ylabel('Valor Médio')

plt.show()