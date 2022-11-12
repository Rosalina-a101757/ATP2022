############################################# EXERCICIO 1 #######################################################

def inicDiferente(s1, s2):
    lista = []
    for letra in s1:
        if letra not in s2:
            lista.append(letra)
    return len(lista)
inicDiferente("Está um bom dia...", "Hoje é um dia alegre.")


def acimaMedia(n):
    num = n
    lista = []
    while n > 0:      
        numero = input("escolhe um numero")
        lista.append(int(numero))
        n = n -1
    res = 0
    for num in lista:
        res = res + num 
    med = res/num
    nAcima = []
    for i in lista:
        if i > med:
            nAcima.append(i)
    return(nAcima)
acimaMedia(5)


def merge(l1, l2):
    lista = l1
    for i in l2:
        if i not in lista:
            lista.append(i)
    elem = 1
    while elem <len (lista):
        indice = 1
        while indice < len (lista):
            if lista[indice] < lista [indice -1]:
                lista [indice -1] , lista[indice] = lista[indice], lista[indice - 1]
            indice = indice +1
        elem = elem +1

    return lista
    
merge([1,2,6,9], [3,4,7,12])


def figuais(f1, f2):
    lista1 = []
    lista2 = []
    file1 = open(f1)
    for line in file1:
        lista1.append(line)
    file2 = open(f2)
    for line in file2:
        lista2.append(line)
    if lista1 == lista2:
        veredito = True
    else: 
        veredito = False
    file1.close
    file2.close
    return(veredito)
print(figuais("texto1.txt", "texto1.txt"))
print(figuais("texto1.txt", "texto2.txt"))



############################################# EXERCICIO 2 #######################################################

# Cinemateca = [Filme]
# Pub = (Título, Ano, Elenco, Géneros)
# Título = String
# Ano = Int
# Elenco = [Ator]
# Ator = String
# Géneros = [Género]
# Género = String
Filme1 = ("Meet the Parents", 2000, ["Ben Stiller","Robert De Niro",
      "Blythe Danner","Teri Polo","Owen Wilson"], ["Comedy", "Drama"])
Filme2 = ("Men of Honor", 2000, ["Robert De Niro","Cuba Gooding, Jr.",
      "Charlize Theron"], ["Biography", "Drama", "Thriller"])
Filme3 = ("Analyze That", 2002, ["Robert De Niro","Billy Crystal",
      "Lisa Kudrow"], ["Comedy"])
CineUM = [Filme1, Filme2, Filme3]



def atores(cinemateca):
    listaAtores = []
    for filme in cinemateca:
        Título, Ano, Elenco, Géneros = filme
        for ator in Elenco:
            if ator not in listaAtores:
                listaAtores.append(ator)
    listaAtores.sort()
    return listaAtores
print(atores(CineUM))


def listarPorGenero(cinemateca, genero):
    listaTit = []
    for filme in cinemateca:
        Título, Ano, Elenco, Géneros = filme
        for gen in Géneros:
            if gen == genero:
                listaTit.append(Título)
    listaTit.sort()
    return listaTit
print(listarPorGenero(CineUM, "Comedy"))


def maiorElenco( cinemateca ):
    maior = 0
    titMaiorElenco = []
    for filme in cinemateca:
        Título, Ano, Elenco, Géneros = filme
        if len(Elenco)> maior:
            titMaiorElenco = Título
            maior = len(Elenco)
    return titMaiorElenco
print(maiorElenco(CineUM))


def filmePorGenero( cinemateca ):
    dictCin = {}
    for filme in cinemateca:
        Título, Ano, Elenco, Géneros = filme
        for gen in Géneros:
            if gen in dictCin.keys():
                dictCin[gen] += 1
            else:
                dictCin[gen] = 1
    return dictCin
filmePorGenero( CineUM )


import matplotlib.pyplot as plt
x = filmePorGenero(CineUM).keys()
y = filmePorGenero(CineUM).values()
plt.bar(x,y)
plt.yscale
plt.xlabel("Género")
plt.ylabel("Número de Filmes")
plt.title("Grafico de distribuições")
plt.show()
