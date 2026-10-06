#Logística e Satisfação:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv('datasets\\olist_customers_dataset.csv', delimiter=',')
geolocation = pd.read_csv('datasets\\olist_geolocation_dataset.csv', delimiter=',')
order_items = pd.read_csv('datasets\\olist_order_items_dataset.csv', delimiter=',')
order_payments = pd.read_csv('datasets\\olist_order_payments_dataset.csv', delimiter=',')
order_reviews = pd.read_csv('datasets\\olist_order_reviews_dataset.csv', delimiter=',')
orders = pd.read_csv('datasets\\olist_orders_dataset.csv', delimiter=',')
products = pd.read_csv('datasets\\olist_products_dataset.csv', delimiter=',')
sellers = pd.read_csv('datasets\\olist_sellers_dataset.csv', delimiter=',')
category_translation = pd.read_csv('datasets\\product_category_name_translation.csv', delimiter=',')

