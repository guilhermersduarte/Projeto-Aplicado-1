import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# definir caminho do arquivo
data_path = 'C:\\Users\\lealg\\OneDrive\\Mackenzie Ciencia de Dados\\2 Semestre\\Projeto Aplicado I\\Walmart_Sales.csv'

# carregar o arquivo
df = pd.read_csv(data_path)

# Preparar dados:
# Converter a coluna 'Date' para o tipo 'datetime'
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# converter Coluna de Temperatura para ° Celcius
df['Temperature'] = (df['Temperature'] - 32) * 5/9

# Analise exploratória
# primeiras linhas
print(df.head())
# infosGerais
print(df.info())
# descrição
print(df.describe())
# médias
print(df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI',
      'Unemployment']].mean().apply(lambda x: "{:,.2f}".format(x)))
# medianas
print(df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI',
      'Unemployment']].median().apply(lambda x: "{:,.2f}".format(x)))
# maximos
print(df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI',
      'Unemployment']].max().apply(lambda x: "{:,.2f}".format(x)))
# minimos
print(df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI',
      'Unemployment']].min().apply(lambda x: "{:,.2f}".format(x)))


# matriz de Correlação
# Configurar o estilo dos gráficos
sns.set(style="whitegrid")

# Criar uma matriz de correlação ignorando as colunas 'Store' e 'Date'
correlation_matrix = df.drop(['Store', 'Date'], axis=1).corr()

# Gerar um mapa de calor da matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()
