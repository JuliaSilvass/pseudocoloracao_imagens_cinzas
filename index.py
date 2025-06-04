import cv2
import matplotlib.pyplot as plt

# Carregar a imagem em tons de cinza
imagem_gray = cv2.imread('imagem_tons_de_cinza.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar pseudo-colorização usando diferentes colormaps
colormaps = {
    'JET': cv2.COLORMAP_JET,
    'HOT': cv2.COLORMAP_HOT,
    'COOL': cv2.COLORMAP_COOL,
    'VIRIDIS': cv2.COLORMAP_VIRIDIS
}

# Criar uma figura para mostrar os resultados
plt.figure(figsize=(10, 8))

# Mostrar a imagem original
plt.subplot(1, len(colormaps) + 1, 1)
plt.imshow(imagem_gray, cmap='gray')
plt.title('Original')
plt.axis('off')

# Aplicar e mostrar cada colormap
for i, (nome, mapa) in enumerate(colormaps.items(), start=2):
    imagem_colorida = cv2.applyColorMap(imagem_gray, mapa)
    imagem_colorida = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)  # Converter para RGB para o matplotlib
    plt.subplot(1, len(colormaps) + 1, i)
    plt.imshow(imagem_colorida)
    plt.title(nome)
    plt.axis('off')

plt.tight_layout()
plt.show()
