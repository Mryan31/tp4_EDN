import numpy as np

def gaussiana(x, mu=0.5, sigma=0.1):
    return np.exp(-0.5 * ((x - mu) / sigma)**2)

def onda_quadrada(x, inicio=0.2, fim=0.4):
    return np.where(np.logical_and(x >= inicio, x <= fim), 1.0, 0.0)

def quina(x, centro=0.5, largura=0.2):
    return np.maximum(0, 1 - np.abs(x - centro) / largura)