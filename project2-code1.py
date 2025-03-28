import matplotlib.pyplot as plt
from skimage import io, color

# Lire l'image ((l'originale en couleur )
original_image = io.imread("rgb_image.jpg")

# Convertir en niveaux de gris
gray_image = color.rgb2gray(original_image)

# Afficher les deux images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(original_image)
axes[0].set_title("Image originale")
axes[0].axis("off") #enlève les axes pour une meilleure visualisation.

axes[1].imshow(gray_image, cmap="gray")
axes[1].set_title("Image en niveaux de gris")
axes[1].axis("off") #enlève les axes pour une meilleure visualisation.

plt.show()
