import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

# Carregar os dados
df = pd.read_csv('Walmart_sales.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Função para categorizar semanas em relação aos feriados
def categorize_week(date, holiday_dates):
    for holiday in holiday_dates:
        if holiday - timedelta(weeks=3) <= date < holiday:
            return 'Boom'
        elif holiday < date <= holiday + timedelta(weeks=3):
            return 'Bust'
    return 'Neutral'

# Gráfico de Barras - Impacto dos Feriados (Item 10.1)
holiday_dates = df[df['Holiday_Flag'] == 1]['Date'].unique()
df['Category'] = df['Date'].apply(lambda x: categorize_week(x, holiday_dates))
df['Holiday_Status'] = df['Holiday_Flag'].map({0: 'Sem Feriado', 1: 'Com Feriado'})

holiday_means = df.groupby('Holiday_Status')['Weekly_Sales'].mean()
category_means = df.groupby('Category')['Weekly_Sales'].mean()
means_df = pd.concat([holiday_means, category_means]).reset_index()
means_df.columns = ['Categoria', 'Média de Vendas']

plt.figure(figsize=(10, 6))
sns.barplot(x='Categoria', y='Média de Vendas', data=means_df, palette='viridis')
plt.title('Média de Vendas Semanais por Categoria de Feriado')
plt.xlabel('Categoria')
plt.ylabel('Média de Vendas (US$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('impacto_feriados.png')

# Gráfico de Dispersão - Impacto do Desemprego (Item 10.2)
plt.figure(figsize=(10, 6))
sns.regplot(x='Unemployment', y='Weekly_Sales', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relação entre Taxa de Desemprego e Vendas Semanais')
plt.xlabel('Taxa de Desemprego (%)')
plt.ylabel('Vendas Semanais (US$)')
plt.tight_layout()
plt.savefig('impacto_desemprego.png')

# Gráfico de Dispersão - Impacto da Temperatura (Item 10.3)
df['Temp_Below_32'] = df['Temperature'] < 32

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Weekly_Sales', data=df, hue='Temp_Below_32', palette={True: 'red', False: 'blue'}, legend=False)
sns.regplot(x='Temperature', y='Weekly_Sales', data=df, scatter=False, color='green')
plt.title('Relação entre Temperatura e Vendas Semanais')
plt.xlabel('Temperatura (°F)')
plt.ylabel('Vendas Semanais (US$)')
plt.tight_layout()
plt.savefig('impacto_temperatura.png')