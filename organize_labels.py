import os
import shutil

# Caminhos dos arquivos
train_txt = 'train.txt'
test_txt = 'test.txt'

# Pasta base de destino
base_dir = 'dataset'
os.makedirs(base_dir, exist_ok=True)

def copiar_arquivos(txt_file, split):
    with open(txt_file, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    for linha in linhas:
        img_path = linha.strip()
        if not img_path:
            continue
        # Nome do arquivo
        img_name = os.path.basename(img_path)
        # Pasta destino para imagens
        dest_img_dir = os.path.join(base_dir, 'images', split)
        os.makedirs(dest_img_dir, exist_ok=True)
        # Copia a imagem
        try:
            shutil.copy2(img_path, os.path.join(dest_img_dir, img_name))
        except Exception as e:
            print(f'Erro ao copiar imagem {img_path}: {e}')
        # Copia o label (troca .jpg por .txt)
        label_path = os.path.splitext(img_path)[0] + '.txt'
        label_name = os.path.splitext(img_name)[0] + '.txt'
        dest_label_dir = os.path.join(base_dir, 'labels', split)
        os.makedirs(dest_label_dir, exist_ok=True)
        if os.path.exists(label_path):
            try:
                shutil.copy2(label_path, os.path.join(dest_label_dir, label_name))
            except Exception as e:
                print(f'Erro ao copiar label {label_path}: {e}')
        else:
            print(f'Label não encontrado para {img_path}')

# Organiza treino e teste
copiar_arquivos(train_txt, 'train')
copiar_arquivos(test_txt, 'test')

print('Imagens e labels organizados!')