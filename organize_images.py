import os
import shutil

# Caminhos dos arquivos
train_txt = 'train.txt'
test_txt = 'test.txt'

# Pasta base de destino
base_dir = 'dataset'
os.makedirs(base_dir, exist_ok=True)

# Função para copiar imagens
def organizar_imagens(txt_file, split):
    with open(txt_file, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    for linha in linhas:
        img_path = linha.strip()
        if not img_path:
            continue
        # Nome do arquivo
        img_name = os.path.basename(img_path)
        # Pasta destino (ex: dataset/train/)
        dest_dir = os.path.join(base_dir, split)
        os.makedirs(dest_dir, exist_ok=True)
        # Copia a imagem
        try:
            shutil.copy2(img_path, os.path.join(dest_dir, img_name))
        except Exception as e:
            print(f'Erro ao copiar {img_path}: {e}')

# Organiza treino e teste
organizar_imagens(train_txt, 'train')
organizar_imagens(test_txt, 'test')

print('Imagens organizadas!')