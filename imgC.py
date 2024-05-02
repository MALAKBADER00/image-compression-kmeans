import numpy as np 
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# read image 
img = imread('butterfly.jpeg')
img_size = img.shape

# re-shape the img to be 2D
x = img.reshape(img_size[0] * img_size[1] , img_size[2])

# Number of clusters for compression
num_clusters = [10, 6, 2]

num_rows = len(num_clusters) // 2 + len(num_clusters) % 2 
fig, ax = plt.subplots(num_rows, 2, figsize=(10, 5*num_rows))

# Plot original image
ax[0, 0].imshow(img)
ax[0, 0].set_title('Original Image')
ax[0, 0].axis('off')

row , col = 0 , 1
for i, n_clusters in enumerate(num_clusters, 1):
    # Run KMeans with specified number of clusters
    km = KMeans(n_clusters=n_clusters)
    km.fit(x)

    # Compress the image
    x_compressed = km.cluster_centers_[km.labels_]
    x_compressed = np.clip(x_compressed.astype('uint8'), 0, 255)
    x_compressed = x_compressed.reshape(img_size[0], img_size[1], img_size[2])

    # Plot compressed image
    ax[row, col].imshow(x_compressed)
    ax[row, col].set_title(f'Compressed Image with {n_clusters} Colors')
    ax[row, col].axis('off')
    
    if col == 0: col+=1 
    else: 
      row+=1
      col = 0    

plt.tight_layout()
plt.show()
