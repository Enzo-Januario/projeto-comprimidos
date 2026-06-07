# Inspeção Visual de Comprimidos — Pipeline Clássico (OGYEIv2)

Projeto Final de Visão Computacional — Cenário C (classificação de comprimidos).
Classifica 4 tipos de comprimidos do dataset OGYEIv2 usando segmentação, extração de features manuais e classificadores clássicos.

**Classes usadas:** algoflex_forte_dolo_400_mg (rosa), apranax_550_mg (azul), donalgin_250_mg (amarelo/vermelho), jutavit_c_vitamin (laranja).

## Estrutura do Projeto

```

├── notebooks/
│   ├── 01_segmentacao.ipynb   # 2 métodos de segmentação (Otsu vs HSV)
│   ├── 02_features.ipynb      # 4 famílias de features -> gera X.csv, y.csv
│   └── 03_classificacao.ipynb # >=2 classificadores clássicos + avaliação
├── ogyeiv2/                   # [IGNORADO NO GIT] Pasta do dataset extraído do Kaggle
├── outputs/                   # Figuras geradas, matrizes de confusão e métricas
├── config.exemplo.py          # Modelo de configuração automatizada
├── config.py                  # Gerado localmente (ignorado no Git)
├── X.csv                      # Matriz de características (gerada pelo notebook 02)
├── y.csv                      # Vetor de alvos/classes (gerado pelo notebook 02)
├── requirements.txt           # Bibliotecas necessárias do projeto
└── .gitignore                 # Filtro de arquivos para o repositório

```

## Setup (Cada integrante faz uma vez)

1. **Clonar o repositório e entrar na pasta:**
   ```bash
   git clone <url-do-repo>
   cd projeto-comprimidos

2. **Criar e ativar o ambiente virtual (venv):**
* **Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```


*(Nota: Se o Windows bloquear por política de execução, rode `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` antes de ativar).*
* **Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate

```




3. **Instalar as dependências:**
```bash
pip install -r requirements.txt

```


4. **Configurar o dataset local (Apenas para os Notebooks 01 e 02):**
Quem for trabalhar apenas no desenvolvimento dos modelos de machine learning (**Notebook 03**) NÃO precisa baixar as imagens pesadas, pois os arquivos `X.csv` e `y.csv` já estão versionados no repositório.
Se você for rodar os passos 01 e 02, siga o padrão:
* Baixe o dataset OGYEIv2 do Kaggle.
* Extraia e mova **apenas** a pasta interna chamada `ogyeiv2` (com letras minúsculas, contendo as subpastas `train/`, `valid/` e `test/`) para a **raiz deste projeto**. *(O arquivo .gitignore já está configurado para não subir essas imagens para o GitHub).*


5. **Ativar o arquivo de configuração:**
Gere o arquivo local rodando o comando:
* **Windows:** `copy config.exemplo.py config.py`
* **Linux/Mac:** `cp config.exemplo.py config.py`


*O arquivo config.py detecta automaticamente a raiz do projeto no sistema de qualquer integrante, eliminando a necessidade de editar caminhos de pastas manualmente.*

## Como Executar

Você pode rodar o projeto de duas formas:

### Opção A: Pelo VS Code (Recomendado)

1. Instale a extensão oficial **Jupyter** da Microsoft no seu VS Code.
2. Abra qualquer notebook na pasta `notebooks/`.
3. No canto superior direito, clique em **Select Kernel** -> **Python Environments** e escolha o interpretador do seu ambiente virtual (`./venv/Scripts/python.exe`).
4. Execute as células normalmente pela interface gráfica.

### Opção B: Pelo Navegador

Ative o ambiente virtual no terminal e execute:

```bash
jupyter notebook

```

Abra os arquivos na ordem do pipeline:

1. `notebooks/01_segmentacao.ipynb` — Compara e valida os métodos de segmentação.
2. `notebooks/02_features.ipynb` — Extrai as características estruturais e gera as matrizes `X.csv` e `y.csv`.
3. `notebooks/03_classificacao.ipynb` — Treina os modelos clássicos e avalia as métricas.
