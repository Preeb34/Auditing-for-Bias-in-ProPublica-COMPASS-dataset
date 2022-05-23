# -*- coding: utf-8 -*-
"""HW5_Bhattacharya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17pmaicM86Q9yRQRHSForfDoLQQ1O2Ole
"""

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist 
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

input_iris_data = pd.read_table("1649181792_01407_1604554690_4994035_1601384279_9602122_iris_new_data.txt", header=None, skip_blank_lines=False, delim_whitespace=True)

input_iris_data.values

def kmeans(a,k, iterations):
    index = np.random.choice(len(a), k, replace=False)
    centroids = a[index, :]
    distances = cdist(a, centroids ,'cosine')
    points = np.array([np.argmin(i) for i in distances])
    for _ in range(iterations):
      centroids = []
      for index in range(k):
        temp = a[points==index].mean(axis=0)
        centroids.append(temp)
      centroids = np.vstack(centroids)
      distances = cdist(a, centroids ,'cosine')
      points = np.array([np.argmin(i) for i in distances])
    return points

output_iris = kmeans(input_iris_data.values,3,1000)

print(output_iris)

np.savetxt("Output_iris_data.txt",output_iris,fmt="%s")

pca = PCA(2)
dx = pca.fit_transform(input_iris_data)
u_labels = np.unique(output_iris)
for j in u_labels:
    plt.scatter(dx[output_iris == j , 0] , dx[output_iris == j , 1] , label = j)
plt.legend()
plt.show()
len(dx[output_iris == 0])

part2 = pd.read_table("/content/1649182019_5350096_1604556007_243332_1601384482_8387134_image_new_test.txt", delimiter =",",header=None)

def kmeans(a,k, iterations):
    index = np.random.choice(len(a), k, replace=False)
   
    centroids = a[index, :] 
     
    dist = cdist(a, centroids ,'cosine')

    points = np.array([np.argmin(i) for i in dist])
    
    for _ in range(iterations): 
        centroids = []
        for index in range(k):
            temp = a[points==index].mean(axis=0) 
            centroids.append(temp)
 
        centroids = np.vstack(centroids) 
        dist = cdist(a, centroids ,'cosine')
        points = np.array([np.argmin(i) for i in dist])
         
    return [points,centroids];

test = kmeans(part2.values,10,50)

fig, ax = plt.subplots(2, 5, figsize=(8, 3))
center =test[1].reshape(10,28,28)
for axi, center in zip(ax.flat, center):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

def sum_squ_err(y,y1):
  summation = 0 
  l = len(y)

  for i in range (1,l):
    diff = y[i] - y1[i] 
    squ_diff = diff**2  
    summation = summation + squ_diff 
  return summation/l  

distortions = []

K = [2,4,6,8,10,12,14,16,18,20]
y = kmeans(part2.values,10,50)   
 
for k in K:

    kmeanModel2 = kmeans(part2.values,k,50)    
    m=kmeanModel2[0]

    distortions.append(sum_squ_err(y[0],m))

plt.figure()
plt.plot(K, distortions, 'bx-')
plt.title('Optimal K by using Elbow Method')
plt.xlabel('k')
plt.ylabel('Distortion')

plt.show()

pca = PCA(n_components=72)
res_pca = pca.fit_transform(part2)
print('Variation/principal: {}'.format(pca.explained_variance_ratio_))
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2,perplexity=8,verbose=1,n_iter=250)
res_tsne_pca = tsne.fit_transform(res_pca)

tag = kmeans(res_tsne_pca,10,50)
print((tag[0]))

u_tag = np.unique(tag[0])
for i in u_tag:
    plt.scatter(res_tsne_pca[tag[0] == i , 0] , res_tsne_pca[tag[0] == i , 1] , label = i)

plt.legend(loc='center right')
plt.figure(figsize=(20,20))
plt.show()

np.savetxt("output_image_data.txt",tag[0],fmt="%s")