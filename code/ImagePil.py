from PIL import Image
import glob

# Caminho para a pasta de carros
path = r'C:\Users\Felipe\PycharmProjects\FormulaRacing\assets\cars'

# Lista de arquivos de imagem dentro da pasta "cars"
files = glob.glob(path + r'\*.png')

print(f"Arquivos encontrados: {files}")

for file in files:
    # Abrindo a imagem
    img = Image.open(file)

    # Obtendo as dimensões da imagem
    width, height = img.size

    # Calculando as novas dimensões (reduzindo por 4)
    new_width = round(width / 4)
    new_height = round(height / 4)

    # Redimensionando a imagem
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Salvando a imagem redimensionada
    img.save(file, format='PNG')

    print(f"Imagem {file} redimensionada para {new_width}x{new_height}")
