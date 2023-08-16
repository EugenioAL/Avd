from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import functools as ft
from math import *


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

def mediaGeometrica(vetor):
    acumulador = 1
    for i in range(len(vetor)):
        acumulador*=vetor[i]
    return acumulador**(1/len(vetor))
    
def amplitude(vetor):
    min = min(vetor)
    max = max(vetor)
    return max-min

def mediaTaxas(vetorA, vetorB):
    media(vetorA/vetorB)

def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)

    if tamanho % 2 == 0:
        mediana = (vetor_ordenado[tamanho // 2-1] + vetor_ordenado[tamanho //2])/2
    else:
        mediana = vetor_ordenado[tamanho // 2]
    return mediana
    
#----------------------To do---------------------------------


#def mediaHarmonica
#def mediaTaxas
#--exercicio slide 18Exercício
#def mediana
#def moda
#--exercicio slide 29
#--exercicio slide 30
#--exercicio slide 31
#def desvioPadrao
#--exercicio slide 33
#def coefVariacao
##--exercicio slide 35
#def quartis
##--exercicio slide 42
#def intevaloConfiancaMedia
#--exercicio slide 51
#--exercicio slide 54
#def testeMediazero
#--exercicio slide 58
#--exercicio slide 59
#--exercicio slide 62
#def tamanhoAmostra
#--exercicio slide 67
#--exercicio slide 69
#def testeHipotese
#def testeShapWilk
#--exercicio slide 86
#
#
#

