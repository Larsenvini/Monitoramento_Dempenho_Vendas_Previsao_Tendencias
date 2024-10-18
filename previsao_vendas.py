import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression

def load_clean_data():
    df = pd.read_csv('vendas_clean.csv')
    df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
    return df

df = load_clean_data()

def prever_vendas_arima(df):
    # Agrupar os dados por data e somar as vendas
    df_grouped = df.groupby('Data da Venda').agg({'Total de Vendas': 'sum'}).reset_index()

    # Definir o modelo ARIMA
    model = ARIMA(df_grouped['Total de Vendas'], order=(5, 1, 0))  # (p, d, q)
    model_fit = model.fit()

    # Fazer previsões para os próximos 10 dias
    forecast = model_fit.forecast(steps=10)
    
    # Plotar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(df_grouped['Data da Venda'], df_grouped['Total de Vendas'], label='Vendas Reais')
    forecast_index = pd.date_range(start=df_grouped['Data da Venda'].max() + pd.Timedelta(days=1), periods=10)
    plt.plot(forecast_index, forecast, color='red', label='Previsão ARIMA')
    plt.title('Previsão de Vendas com ARIMA (10 dias)')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.legend()
    plt.show()

def prever_vendas_linear(df):
    # Agrupar os dados por data e somar as vendas
    df_grouped = df.groupby('Data da Venda').agg({'Total de Vendas': 'sum'}).reset_index()

    # Criar coluna de dias desde a primeira venda
    df_grouped['Dias'] = (df_grouped['Data da Venda'] - df_grouped['Data da Venda'].min()).dt.days

    # Dividir os dados em conjuntos de treino e teste
    X = df_grouped[['Dias']]
    y = df_grouped['Total de Vendas']
    
    # Criar e treinar o modelo
    model = LinearRegression()
    model.fit(X, y)

    # Fazer previsões
    predictions = model.predict(X)

    # Plotar resultados
    plt.figure(figsize=(12, 6))
    plt.scatter(df_grouped['Data da Venda'], y, color='blue', label='Dados Reais')
    plt.plot(df_grouped['Data da Venda'], predictions, color='red', label='Previsões Linear')
    plt.title('Previsão de Vendas com Regressão Linear')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.legend()
    plt.show()

# Nova função para previsões de longo prazo
def prever_vendas_arima_longo_prazo(df):
    # Agrupar os dados por data e somar as vendas
    df_grouped = df.groupby('Data da Venda').agg({'Total de Vendas': 'sum'}).reset_index()

    # Definir o modelo ARIMA
    model = ARIMA(df_grouped['Total de Vendas'], order=(5, 1, 0))  # (p, d, q)
    model_fit = model.fit()

    # Fazer previsões para os próximos 30 dias (ou mais)
    forecast_steps = 30
    forecast = model_fit.forecast(steps=forecast_steps)

    # Plotar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(df_grouped['Data da Venda'], df_grouped['Total de Vendas'], label='Vendas Reais')
    forecast_index = pd.date_range(start=df_grouped['Data da Venda'].max() + pd.Timedelta(days=1), periods=forecast_steps)
    plt.plot(forecast_index, forecast, color='green', label=f'Previsão ARIMA ({forecast_steps} dias)')
    plt.title(f'Previsão de Vendas com ARIMA ({forecast_steps} dias)')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    df = load_clean_data()
    
    # Chamar a função de previsão ARIMA (curto prazo)
    prever_vendas_arima(df)
    
    # Chamar a função de previsão Linear
    prever_vendas_linear(df)
    
    # Chamar a função de previsão ARIMA (longo prazo)
    prever_vendas_arima_longo_prazo(df)
