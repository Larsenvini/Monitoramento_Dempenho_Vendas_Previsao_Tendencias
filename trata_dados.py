import pandas as pd

def clean_data():
    # Load and clean data
    df = pd.read_csv('vendas.csv')
    df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])  # Convert dates
    df['Total de Vendas'] = df['Quantidade'] * df['Preço']  # Calculate total sales
    df.dropna(inplace=True)  # Remove null values

    # Save cleaned data to a new CSV
    df.to_csv('vendas_clean.csv', index=False)
    print("Data cleaned and saved as vendas_clean.csv!")


