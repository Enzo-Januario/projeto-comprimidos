import pandas as pd
import numpy as np

# Carregamento dos arquivos originais
X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv')

# Identificação das colunas numéricas para aplicação de ruído
colunas_numericas = X.select_dtypes(include=[np.number]).columns
classes_unicas = y['classe'].unique()

X_adicionais = []
y_adicionais = []

np.random.seed(42)

for classe in classes_unicas:
    # Isolamento dos índices pertencentes à classe atual
    indices_classe = y[y['classe'] == classe].index
    
    # Seleção aleatória de 10 amostras da classe para replicação com variação
    indices_selecionados = np.random.choice(indices_classe, size=10, replace=False)
    
    X_sub = X.loc[indices_selecionados].copy()
    y_sub = y.loc[indices_selecionados].copy()
    
    # Aplicação de ruído gaussiano controlado (0.1% do desvio padrão da coluna)
    for col in colunas_numericas:
        std_ruido = X[col].std() * 0.001
        ruido = np.random.normal(0, std_ruido, size=len(X_sub))
        X_sub[col] = X_sub[col] + ruido
        
    X_adicionais.append(X_sub)
    y_adicionais.append(y_sub)

# Concatenação das novas amostras artificiais às originais
X_final = pd.concat([X, *X_adicionais], ignore_index=True)
y_final = pd.concat([y, *y_adicionais], ignore_index=True)

# Exportação e sobrescrita segura dos arquivos CSV
X_final.to_csv('X.csv', index=False)
y_final.to_csv('y.csv', index=False)

print("STATUS: Expansão concluída com sucesso.")
print(f"Nova volumetria total do dataset: {X_final.shape[0]} amostras (50 por classe).")