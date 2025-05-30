# Projeto Aplicado 1 - Análise de Dados Walmart

Este repositório contém a análise de dados das vendas do Walmart, desenvolvida como parte do Projeto Aplicado 1. O projeto explora diversos fatores que influenciam as vendas, como temperatura, desemprego e feriados.

A apresentação do projeto se encontra no Youtube, pode ser vista aqui: https://www.youtube.com/watch?v=BCe41GIgLXI

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

### 📊 Notebooks Principais de Análise

A pasta **`Notebooks/`** contém os notebooks principais utilizados para a análise de dados, organizados por tipo de análise:

- **Análise Exploratória Geral**:
  - `analise_exploratoria.ipynb` - Análise exploratória inicial dos dados
  - `Exp_inicial.ipynb` - Exploração inicial dos dados

- **Análise de Temperatura**:
  - `Walmart_AE_Temperature.ipynb` - Análise do impacto da temperatura nas vendas

- **Análise de Desemprego**:
  - `Walmart_AE_Unemployment.ipynb` - Análise do impacto da taxa de desemprego nas vendas

- **Análise de Feriados**:
  - `Walmart_AE_Holiday.ipynb` - Análise do impacto dos feriados nas vendas
  - `Wallmart_Revisao_Feriados_B.ipynb` - Revisão da análise de feriados
  - `Walmart_Otimizacao_Feriados.ipynb` - Otimização da análise de feriados

### 📁 Notebooks Auxiliares

A pasta **`src/`** contém notebooks auxiliares e arquivos de suporte organizados por contribuidor:

- `g_duarte/` - Notebooks auxiliares focados na análise de temperatura
- `r_amaral/` - Notebooks auxiliares para diversas análises (temperatura, desemprego, feriados, CPI, combustível)
- `g_guimaraes/`, `g_leal/`, `g_oliveira/` - Outros arquivos auxiliares
- `Outros/` - Notebooks auxiliares adicionais

### 🗃️ Conjuntos de Dados

A pasta **`dados/`** contém os conjuntos de dados utilizados no projeto:

- `Walmart_Sales.csv` - Conjunto de dados original
- `Walmart_Sales_Updated.csv` - Conjunto de dados atualizado
- `boom_bust_by_store.csv` e `boom_bust_by_store_with_total.csv` - Conjuntos de dados derivados

### 📑 Documentação

A pasta **`DOCS/`** contém a documentação do projeto:

- Arquivos Word com os relatórios das entregas
- Cronogramas do projeto
- A subpasta `entregas/` contém as versões em PDF dos documentos

## Conjunto de Dados

O conjunto de dados utilizado neste projeto contém informações sobre as vendas semanais do Walmart e inclui as seguintes colunas:

- **Store**: Número da loja
- **Date**: Data de início da semana de vendas
- **Weekly_Sales**: Vendas semanais
- **Holiday_Flag**: Indicador de presença ou ausência de feriado
- **Temperature**: Temperatura do ar na região
- **Fuel_Price**: Custo do combustível na região
- **CPI**: Índice de preços ao consumidor
- **Unemployment**: Taxa de desemprego

## Como Navegar pelo Repositório

Para encontrar análises específicas:

1. **Análises Principais**: Consulte a pasta `Notebooks/` para os notebooks principais organizados por tipo de análise.
2. **Análises Detalhadas por Contribuidor**: Consulte as subpastas dentro de `src/` para notebooks auxiliares e análises específicas desenvolvidas por cada contribuidor.
3. **Documentação e Relatórios**: Consulte a pasta `DOCS/` para relatórios completos e documentação do projeto.
4. **Dados**: Consulte a pasta `dados/` para acessar os conjuntos de dados utilizados.

## Fonte dos Dados

Os dados utilizados neste projeto foram obtidos do Kaggle:
[Walmart Sales Dataset](https://www.kaggle.com/datasets/mikhail1681/walmart-sales/data)
