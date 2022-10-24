### TPC5: Análise de dados: doença cardíaca
#Descarregue o ficheiro de dados: `myheart.csv`
#Crie um programa em Python, conjunto de funções, que responda às seguintes questões:
#* Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
#* Crie uma função que calcula a distribuição da doença por sexo;
#* Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ...
#* Crie uma função que calcula a distribuição da doença por níveis de colesterol. Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior;
#* Crie uma função que imprime na forma de uma tabela uma distribuição;
#* Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas.

global pop
global classes
global valoresClasse
pop = []
classes = []
valoresClasse = []


def lerFichero(ficheiro):
    global pop
    listatemporaria = []
    file = open(ficheiro, "r")
    file.readline()
    for line in file:
        pessoaList = line.split(",")
        listatemporaria.append(pessoaList)
    for pessoaList in listatemporaria:
        pessoaList[-1] = pessoaList[-1].replace("\n", "")
        pessoa = (pessoaList[0], pessoaList[1], pessoaList[2], pessoaList[3], pessoaList[4], pessoaList[5])
        pop.append(pessoa)
    file.close()

def sexoDoentes(lista):
    global classes
    global valoresClasse
    classes = []
    genero = ["Homem", "Mulher"]
    classes = genero
    masculino = 0
    feminino = 0
    for pessoa in lista:
        idade, sexo, tensão, colesterol, batimento, doença = pessoa
        if doença != "0":
            if sexo == "M":
                masculino = masculino + 1
            if sexo == "F":
                feminino = feminino + 1
    valoresClasse.append(masculino)
    valoresClasse.append(feminino)

def maior(lista):
    maiorIdade = 0
    maiorTen = 0
    maiorCol = 0
    maiorBat = 0
    for pessoa in lista:
        idade, sexo, tensão, colesterol, batimento, doença = pessoa
        if int(idade) > int(maiorIdade):
            maiorIdade = idade
        if int(tensão) > int(maiorTen):
            maiorTen = tensão
        if int(colesterol) > int(maiorCol):
            maiorCol = colesterol
        if  int(batimento) > int(maiorBat):
            maiorBat = batimento
    maiores = print("Lista de Maiores: " + "#" + " Maior idade = " + str(maiorIdade) +" #" + " Maior Tensão = " + str(maiorTen) + " #" +" Maior Colesterol: " + str(maiorCol) +" #" + " Maior Batimento: " + str(maiorBat))
    return maiores

def menor(lista):
    menorIdade = 77
    menorTen = 200
    menorCol = 603
    menorBat = 202
    for pessoa in lista:
        idade, sexo, tensão, colesterol, batimento, doença = pessoa
        if int(idade) < int(menorIdade):
            menorIdade = idade
        if int(tensão) < int(menorTen):
            menorTen = tensão
        if int(colesterol) < int(menorCol):
            menorCol = colesterol
        if  int(batimento) < int(menorBat):
            menorBat = batimento
    menores = print("Lista de Menores: " + "#" + " Menor idade = " + str(menorIdade) +" #" + " Menor Tensão = " + str(menorTen) + " #" +" Menor Colesterol: " + str(menorCol) +" #" + " Menor Batimento: " + str(menorBat))
    return menores

def distribIdades(lista):
    global classes
    global valoresClasse
    classes = []
    valoresClasse = []
    menor = 28
    Nclasse = 0
    while menor <= 73:
        for pessoa in lista:
            idade, sexo, tensão, colesterol, batimento, doença = pessoa
            if doença != "0":
                if int(idade) >= menor and int(idade) <= (menor + 4):
                    Nclasse = Nclasse + 1
        classeX = ("[" + str(menor) + ";" + str(menor+4) + "]")
        classes.append(classeX)
        valoresClasseX = Nclasse
        valoresClasse.append(valoresClasseX)
        Nclasse = 0
        menor = menor + 5


def distribCol(lista):
    global classes
    global valoresClasse
    classes = []
    valoresClasse = []
    menor = 0
    Nclasse = 0
    while menor <= 600:
        for pessoa in lista:
            idade, sexo, tensão, colesterol, batimento, doença = pessoa
            if doença != "0":
                if int(colesterol) >= menor and int(colesterol) <= (menor + 9):
                    Nclasse = Nclasse + 1
        classeX = ("[" + str(menor) + ";" + str(menor + 9) + "]")
        classes.append(classeX)
        valoresClasseX = Nclasse
        valoresClasse.append(valoresClasseX)
        Nclasse = 0
        menor = menor+10


def distribTen(lista):
    global classes
    global valoresClasse
    classes = []
    menor = 0
    Nclasse = 0
    while menor <= 200:
        for pessoa in lista:
            idade, sexo, tensão, colesterol, batimento, doença = pessoa
            if doença != "0":
                if int(tensão) >= menor and int(tensão) <= (menor + 9):
                    Nclasse = Nclasse + 1
        classeX = ("[" + str(menor) + ";" + str(menor + 9) + "]")
        classes.append(classeX)
        valoresClasseX = Nclasse
        valoresClasse.append(valoresClasseX)
        Nclasse = 0
        menor = menor+10


def distribBat(lista):
    global classes
    global valoresClasse
    classes = []
    valoresClasse = []
    menor = 60
    Nclasse = 0
    while menor <= 190:
        for pessoa in lista:
            idade, sexo, tensão, colesterol, batimento, doença = pessoa
            if doença != "0":
                if int(batimento) >= menor and int(batimento) <= (menor + 9):
                    Nclasse = Nclasse + 1
        classeX = ("[" + str(menor) + ";" + str(menor + 9) + "]")
        classes.append(classeX)
        valoresClasseX = Nclasse
        valoresClasse.append(valoresClasseX)
        Nclasse = 0
        menor = menor+10


def tabela(classesDist):
    global valoresClasse
    tituloX =("Classe de distribuição")
    tituloY =("Número de pessoas doentes")
    título = tituloX + " | " + tituloY
    print(título)
    print("--------------------------------------------------")
    indice = 0
    for classe in classesDist:
            print(str(classe) + " | " + str(valoresClasse[indice]))
            indice = indice + 1


####################################EXTRUTURA.PROG##################################################

lerFichero("ListaDados")
menu = 10
while menu != 0:
    menu = int(input('''
Com este programa podes ver a relação entre uma determinada doença estudada e a sua relação com os respetivos fatores:
1) Sexo
2) Idade
3) Tensão
4) Colesterol
5) Batimento
0) Encerrar o programa
Seleciona a opção da qual queres ver a relação com a distribuição da doença!
    '''))

    if menu == 1:
        print("__________________________________________________")
        sexoDoentes(pop)
        tabela(classes)
        print("__________________________________________________")
    if menu == 2:
        print("__________________________________________________")
        distribIdades(pop)
        tabela(classes)
        print("__________________________________________________")
    if menu == 3:
        print("__________________________________________________")
        distribTen(pop)
        tabela(classes)
        print("__________________________________________________")
    if menu == 4:
        print("__________________________________________________")
        distribCol(pop)
        tabela(classes)
        print("__________________________________________________")
    if menu == 5:
        print("__________________________________________________")
        distribBat(pop)
        tabela(classes)
        print("__________________________________________________")
    if menu == 0:
        print("Programa terminado!")

