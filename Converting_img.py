import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert_img(image_array, n_colors=5):
    image=cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    pixel=image.reshape(-1, 3)
    pixels=pixel/255

    from sklearn.cluster import KMeans
    kmeans=KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)
    
    new_colors=kmeans.cluster_centers_[kmeans.predict(pixels)]
    new_colors=new_colors*255
    new_colors=new_colors.astype(int)
    new_image=new_colors.reshape(image.shape).astype(np.uint8)

    new_image_bgr=cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)

    return new_image_bgr


