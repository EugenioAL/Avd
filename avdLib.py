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
#----------------------To do---------------------------------
#def mediaGeometrica
#def mediaHarmonica
#def mediaTaxas
#--exercicio slide 18Exercício
#def mediana
#def moda
#def amplitude
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

