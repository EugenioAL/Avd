from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import functools as ft


def arrayFfile(nome):
    with open(nome) as file:
        data = file.read()
    vetor = data.split()
    for i in range(len(vetor)):
        vetor[i] = int(vetor[i])
    return vetor

def plotHist(vetor):
    plt.hist(vetor, rwidth=0.5)


def media(vetor):
    return sum(vetor)/len(vetor)

def mediaPond(matriz):
    pesoTotal = sum(matriz[1])
    valorTotal = 0
    for i in range(len(matriz[1])):
        valorTotal += matriz[0][i]*matriz[1][i]
    return valorTotal/pesoTotal

def mediaHarmo
