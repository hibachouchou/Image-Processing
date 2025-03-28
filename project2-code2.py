import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Lire l'image
image = io.imread("rgb_image.jpg")


# Séparer les composantes R, G et B
red = image[:, :, 0]   # Canal Rouge
green = image[:, :, 1] # Canal Vert
blue = image[:, :, 2]  # Canal Bleu

# Afficher les images
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

axes[0].imshow(image)
axes[0].set_title("Image originale")
axes[0].axis("off")

axes[1].imshow(red, cmap="Reds")
axes[1].set_title("Canal Rouge")
axes[1].axis("off")

axes[2].imshow(green, cmap="Greens")
axes[2].set_title("Canal Vert")
axes[2].axis("off")

axes[3].imshow(blue, cmap="Blues")
axes[3].set_title("Canal Bleu")
axes[3].axis("off")

plt.show()
