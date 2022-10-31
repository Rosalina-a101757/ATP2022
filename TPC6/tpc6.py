# Modelo: [(nome, des, periodo,duracao,_id)]

import matplotlib.pyplot as plt
import csv

def lerObras():
    file = open("obras.csv", "r", encoding = "UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter = ";")
    lista = []
    for conjunto in csv_file:
        lista.append(tuple(conjunto))
    file.close()
    return (lista)

def contaObras(lista):
    return len(lista)

def imprimeObras(obras):
    print("-------------------------------------------------------------------------------")
    print(f"| {'Nome':<20} | {'Descição':<25} | {'Ano':<8} | {'Compositor':<15}")
    print("-------------------------------------------------------------------------------")
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        print(f"| {nome[:20]:<20} | {desc[:25]:<25} | {ano:^8} | {compositor[:15]:>15}")

def ordenaObrasTitAno(obras):
    return obras[0]

def obrasTitAno(obras):
    lista = []
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        lista.append((nome,ano))
    lista.sort(key=ordenaObrasTitAno)
    return lista

def ordenaObrasAnoTit(obras):
    return obras[1]

def obrasAnoTit(obras):
    lista = []
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        lista.append((ano, nome))
    lista.sort(key=ordenaObrasTitAno)
    return lista

def ordenaCompositores(obras):
    lista = []
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        lista.append(compositor)
    lista.sort()
    return lista

def distribPeriodos(obras):
    dict = {}
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        if periodo in dict.keys():
            dict[periodo] = dict[periodo] + 1
        else:
            dict[periodo] = 1
    return dict

def distribAnos(obras):
    dict = {} 
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        if ano in dict.keys():
            dict[ano] = dict[ano] + 1
        else:
            dict[ano] = 1

    listaTup  = list(dict.items())
    listaTup.sort(key=ordenaObrasTitAno)
    
    lista = []
    for par in listaTup:
        Ano, valor = par
        lista.append(int(Ano))
    
    listaClasses = []
    valoresClasse = []
    Nclasse = 0
    menor = lista[0]
    
    while menor <= lista[-50]:
        for Ano in lista:
            if Ano >= menor and Ano <= (menor + 49):
                    Nclasse = Nclasse + 1
        classeX = ("[" + str(menor) + ";" + str(menor + 49) + "]")
        listaClasses.append(classeX)
        valoresClasseX = Nclasse
        valoresClasse.append(valoresClasseX)
        Nclasse = 0
        menor = menor+50

    newDict = {}

    for classe in listaClasses:
        for n in valoresClasse:
            newDict[classe] = n
    return newDict


def distribCompositor(obras):
    dict = {}
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        if compositor in dict.keys():
            dict[compositor] = dict[compositor] + 1
        else:
            dict[compositor] = 1
    return dict

def criaGrafico(distrib):
    x = distrib.keys()
    y = distrib.values()

    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.show()
    plt.xlabel("Distribuição")
    plt.ylabel("Valores")
    plt.title("Grafico de distribuições")
    plt.gcf().set_size_inches(25,18)

def distribCompObras(obras):
    listaComp = []
    listaObras = []
    for nome, desc, ano, periodo, compositor, duracao, id in obras:
        listaComp.append(compositor)
        listaObras.append((compositor,obras))
    for compositor in listaComp:
        print ("Compositor:" + str(compositor))
        for tuplo in listaObras:
            comp, obra = tuplo
            if comp == compositor:
                print("Obras:" + str(obra))
    print()
    
