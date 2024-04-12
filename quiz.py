import numpy as np 
import pandas as pd
import scipy.io as sio



dim1=10
dim2=20
dim3=30
dim4=200

matriz4d= np.random.randint(10, size=(dim1,dim2,dim3,dim4))

print("PUNTO 1:")
print(matriz4d.shape)
print(matriz4d)

matriz3d= matriz4d.copy()
matriz3d.shape=(dim1, dim2, -1)

print("PUNTO 2:")
print(matriz3d.shape)
print(matriz3d)

#punto 3
print(" PUNTO 3 \n")
print(f"Numero de dimensiones: {matriz3d.ndim}")
print(f"Forma: {matriz3d.shape}")
print(f"Tamaño: {matriz3d.size}")
print(f"Tipo: {matriz3d.dtype}")
print(f"Tamaño de bytes: {matriz3d.itemsize}")
print(f"Tamaño total: {matriz3d.nbytes}")


