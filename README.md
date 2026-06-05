# Inspeção Visual de Comprimidos — Pipeline Clássico (OGYEIv2)

Projeto Final de Visão Computacional — Cenário C (classificação de comprimidos).
Classifica 4 tipos de comprimido do OGYEIv2 usando segmentação + features manuais + classificadores clássicos.

**Classes usadas:** algoflex_forte_dolo_400_mg (rosa), apranax_550_mg (azul),
donalgin_250_mg (amarelo/vermelho), jutavit_c_vitamin (laranja).

## Estrutura
```
notebooks/
  01_segmentacao.ipynb   # 2 métodos de segmentação (Otsu vs HSV)
  02_features.ipynb      # 4 famílias de features -> X.csv, y.csv
  03_classificacao.ipynb # (a fazer) >=2 classificadores + avaliação
outputs/                 # figuras, matrizes, métricas
config.exemplo.py        # modelo de configuração (copie para config.py)
X.csv  y.csv             # gerados pelo notebook 02
requirements.txt
.gitignore
```

## Setup (cada integrante, uma vez)

1. Clonar o repositório e entrar na pasta:
   ```bash
   git clone <url-do-repo>
   cd projeto-comprimidos
   ```
2. Criar e ativar o ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1     # Windows
   # source venv/bin/activate      # Linux/Mac
   ```
3. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. **Baixar o OGYEIv2 do Kaggle** (só quem for mexer nos notebooks 01 e 02).
   Quem for fazer só a classificação (notebook 03) NÃO precisa do dataset —
   usa o X.csv e y.csv que já estão no repositório.
5. Configurar o caminho do dataset:
   ```bash
   copy config.exemplo.py config.py     # Windows  (cp no Linux/Mac)
   ```
   Abra `config.py` e ajuste `DATASET_ROOT` para o caminho na SUA máquina
   (a pasta que contém train/ valid/ test/). O config.py é individual e não
   vai para o GitHub.

## Executar
```bash
jupyter notebook
```
Abra e rode, em ordem:
1. `notebooks/01_segmentacao.ipynb` — compara os dois métodos de segmentação.
2. `notebooks/02_features.ipynb` — gera `X.csv` e `y.csv`.

## Observações
- O OGYEIv2 tem ~40 imagens por classe; discutir essa limitação no relatório.
- O dataset já vem dividido em train/valid/test; a coluna `split` em X.csv preserva essa divisão.
