import os
import shutil
import random

# Caminhos
train_dir = 'dataset/images/train'
label_train_dir = 'dataset/labels/train'
valid_dir = 'dataset/images/valid'
label_valid_dir = 'dataset/labels/valid'

os.makedirs(valid_dir, exist_ok=True)
os.makedirs(label_valid_dir, exist_ok=True)

# Porcentagem para validação
val_percent = 0.1

# Lista de imagens
images = [f for f in os.listdir(train_dir) if f.endswith('.jpg') or f.endswith('.png')]
random.shuffle(images)
val_count = int(len(images) * val_percent)
val_images = images[:val_count]

for img in val_images:
    # Move imagem
    shutil.move(os.path.join(train_dir, img), os.path.join(valid_dir, img))
    # Move label correspondente
    label_file = os.path.splitext(img)[0] + '.txt'
    if os.path.exists(os.path.join(label_train_dir, label_file)):
        shutil.move(os.path.join(label_train_dir, label_file), os.path.join(label_valid_dir, label_file))

print(f'{len(val_images)} imagens movidas para validação.')