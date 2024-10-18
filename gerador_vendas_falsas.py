from faker import Faker
import pandas as pd

fake = Faker()
data = [{'Data da Venda': fake.date_this_year(), 'Produto': fake.word(),
         'Quantidade': fake.random_int(min=1, max=100), 
         'Preço': fake.random_int(min=10, max=500), 
         'Região': fake.city(), 'Vendedor': fake.name()} 
        for _ in range(1000)]

df = pd.DataFrame(data)
df.to_csv('vendas.csv', index=False)
