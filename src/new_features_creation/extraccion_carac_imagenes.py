import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog

# Cargar imagen de ejemplo (reemplaza con tu propia ruta)
# Si no tienes una imagen, podemos generar una aleatoria
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# 1. Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Detección de bordes (Canny)
edges = cv2.Canny(gray, 100, 200)

# 3. Histograma de gradientes orientados (HOG)
fd, hog_image = hog(gray, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True)

# 4. Extraer histograma de color
hist_color = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist_color = hist_color.flatten()

# Mostrar resultados
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(gray, cmap="gray")
plt.title("Escala de Grises")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(edges, cmap="gray")
plt.title("Bordes (Canny)")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(hog_image, cmap="gray")
plt.title("HOG")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"Características HOG: {len(fd)} dimensiones")
print(f"Histograma de color: {len(hist_color)} dimensiones")