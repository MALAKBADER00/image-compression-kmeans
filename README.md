# Image Compression using K-Means Clustering

This repository contains code for compressing images using the K-Means clustering algorithm. Image compression is achieved by reducing the number of unique colors in the image while preserving its visual quality to some extent.

## How it Works

1. **Data Representation**: Images are represented as a collection of pixels, where each pixel contains color information (RGB values). Before applying K-means clustering, the image is reshaped into a 2D array where each row represents a pixel and each column represents a color channel (R, G, or B).

2. **Clustering Similar Colors**: The K-Means algorithm partitions the color space into clusters based on similarity. Each cluster centroid represents a color prototype, and similar colors are grouped together.

3. **Assigning Pixels to Clusters**: Each pixel in the image is assigned to the nearest cluster centroid based on color similarity. This assignment is done by calculating the Euclidean distance between the pixel's color and each cluster centroid.

4. **Compression**: After assigning pixels to clusters, each pixel's color is replaced with the color of its assigned cluster centroid. This significantly reduces the amount of information needed to represent the image since we only need to store the indices of the cluster centroids rather than the full color information of each pixel.

5. **Reconstruction**: Finally, the compressed image is reconstructed by replacing each pixel's color with the color of its assigned cluster centroid, resulting in an image with reduced color depth.

## Usage


1. Install the required dependencies:
   pip install -r requirements.txt
2. Run the Python script to compress your images:
   ## Example
![Original and Compressed Images](example.png)





