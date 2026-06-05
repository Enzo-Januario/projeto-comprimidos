import os

# Descobre o caminho absoluto do diretório raiz do projeto (onde este config.py reside)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Aponta para a pasta ogyeiv2 localizada na raiz do projeto
DATASET_ROOT = os.path.join(BASE_DIR, "ogyeiv2")

# Apenas para depuração local caso queira testar se o caminho está correto
if __name__ == "__main__":
    print("Diretório Base do Projeto:", BASE_DIR)
    print("Caminho do Dataset Configurado:", DATASET_ROOT)
    print("A pasta existe?", os.path.exists(DATASET_ROOT))