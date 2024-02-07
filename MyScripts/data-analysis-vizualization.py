try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    print(f"Erro ao importar biblioteca: {e}")
    print("Certifique-se de que as bibliotecas necessárias estão instaladas.")
    exit(1)  # Encerrar o script com código de erro
    
# Create a DataFrame
data = {
    'Ano': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Receita (milhões de dólares)': [120, 135, 155, 180, 200, 210, 225, 240, 260, 280],
}

df = pd.DataFrame(data)

# Perform simple data analysis
stats = df['Receita (milhões de dólares)'].describe()

mean_revenue = stats['mean']
max_revenue = stats['max']
min_revenue = stats['min']

print(f"Média de Receita: ${mean_revenue:.2f} milhões")
print(f"Maior Receita: ${max_revenue:.2f} milhões (em {df.loc[df['Receita (milhões de dólares)'].idxmax()]['Ano']})")
print(f"Menor Receita: ${min_revenue:.2f} milhões (em {df.loc[df['Receita (milhões de dólares)'].idxmin()]['Ano']})")

# Create visualizations
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Ano', y='Receita (milhões de dólares)', marker='o')
plt.title('Receita ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Receita (milhões de dólares)')
plt.grid(True)
plt.show()