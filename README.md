# Projeto Prático 1: Análise de Dados e Comportamento no E-commerce 📊

## 📝 Sobre o Projeto

Este projeto prático de Ciência de Dados tem como objetivo analisar um conjunto de dados de comércio eletrônico para extrair *insights* valiosos sobre o comportamento do consumidor, logística, faturamento e desempenho de vendedores. 

Através do processamento, filtragem e agregação de dados, buscamos entender os principais fatores que influenciam a satisfação dos clientes e o sucesso das vendas.

## 🎯 Objetivos de Negócio

O projeto foi estruturado para responder a 10 perguntas de negócios fundamentais utilizando análise exploratória de dados (EDA):

1. **Logística e Satisfação:** Como o atraso na entrega influencia a satisfação dos clientes?
2. **Impacto do Frete:** Como o valor do frete influencia o valor final da compra e a satisfação dos clientes?
3. **Desempenho de Produtos:** Quais categorias de produtos geram maior faturamento e quais apresentam melhores avaliações dos clientes?
4. **Geografia das Vendas:** Quais estados brasileiros apresentam maior volume de vendas e faturamento, e como a satisfação dos clientes varia entre eles?
5. **Comportamento de Pagamento (Parcelas):** Existe relação entre o número de parcelas e o valor médio das compras?
6. **Sazonalidade:** Como o volume de vendas varia ao longo do tempo e quais períodos apresentam maior demanda?
7. **Métodos de Pagamento:** Quais formas de pagamento estão associadas a compras de maior valor?
8. **Gargalos Logísticos:** Quais categorias de produtos apresentam maior frequência de atrasos nas entregas?
9. **Impacto Visual:** Produtos com maior número de fotos apresentam melhores avaliações ou maior volume de vendas?
10. **Top Sellers:** Quais vendedores conseguem combinar alto volume de vendas com boas avaliações dos clientes?

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido em **Python**, utilizando as seguintes bibliotecas para manipulação e visualização de dados:

* **[Pandas](https://pandas.pydata.org/):** Limpeza, filtragem, agregação e manipulação dos *dataframes*.
* **[NumPy](https://numpy.org/):** Operações matemáticas e computação numérica de alta performance.
* **[Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/):** Criação de gráficos e visualização de dados para facilitar a interpretação dos resultados.
* **Jupyter Notebook:** Ambiente interativo de desenvolvimento.

## 📂 Estrutura do Repositório

```text
├── data/                   # Diretório contendo os arquivos de dados brutos e processados (se aplicável)
├── notebooks/              # Jupyter Notebooks com a análise exploratória passo a passo
├── src/                    # Scripts Python auxiliares para processamento de dados
├── README.md               # Documentação do projeto
└── requirements.txt        # Lista de dependências e bibliotecas do projeto