import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

# Charger l'image
image = io.imread("noir_blanc.jpg")


# Appliquer la transformation de Fourier
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)  # Centrer les basses fréquences

# Calculer le spectre (valeurs absolues et échelle logarithmique)
magnitude_spectrum = np.log1p(np.abs(f_transform_shifted))

# Afficher l'image originale et son spectre
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(image, cmap="gray")
axes[0].set_title("Image originale")
axes[0].axis("off")

axes[1].imshow(magnitude_spectrum, cmap="gray")
axes[1].set_title("Spectre de Fourier")
axes[1].axis("off")

plt.show()
