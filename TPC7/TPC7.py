import csv
import matplotlib.pyplot as plt

def leFicheiro():
    file = open ("alunos.csv", "r", encoding = "UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter = ",")
    lista = []
    for linha in csv_file:
        lista.append(tuple(linha))
    file.close()
    return lista

def distribCursos(lista):
    cursos = {}
    if len(lista[1]) == 7:
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4 = aluno
            if curso in cursos.keys():
                cursos[curso] += 1
            else:
                cursos[curso] = 1

    if len(lista[1]) == 8:
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
            if curso in cursos.keys():
                cursos[curso] += 1
            else:
                cursos[curso] = 1
    
    if len(lista[1]) == 9:
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalão = aluno
            if curso in cursos.keys():
                cursos[curso] += 1
            else:
                cursos[curso] = 1
    
    return cursos

def media(lista):
    lista1 = []
    if len(lista[1]) >= 8:
        lista1 = lista
    else:
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4 = aluno
            media1 = (int(tpc1) + int(tpc2) + int(tpc3)+ int(tpc4))/4
            aluno = list(aluno)
            aluno.append(media1)
            aluno = tuple(aluno)
            lista1.append(aluno)
        file = open("alunos.csv", "w", encoding = "UTF8")
        file.write("id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4")
        for aluno in lista1:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
            media = str(media)
            soma = ""
            soma = id + "," + nome + "," + curso + "," + tpc1 + "," + tpc2 + "," + tpc3 + "," + tpc4 + "," + media + "\n"
            file.write(soma)
        file.close()
    return lista1

def escaloes(lista):
    if len(lista[1]) >= 9:
        lista1 = lista
    else:
        lista1=[]
        notas =[
            ["A",17,18,19,20],
            ["B",13,14,15,16],
            ["C",9,10,11,12],
            ["D",5,6,7,8],
            ["E",1,2,3,4],
        ]

        if len(lista[1]) == 7:
            print("faz primeiro a media")
            lista1 = lista
        else:
            listamedesc = []
            for aluno in lista:
                id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
                for escalao in notas:
                    if round(float(media)) in escalao:
                        escalao = escalao[0]
                        aluno = list(aluno)
                        aluno.append(escalao)
                        aluno = tuple(aluno)
                        lista1.append(aluno)

            file = open("alunos.csv", "w", encoding="UTF8")
            file.write("id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4")
            for aluno in lista1:
                id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
                media = str(media)
                soma = ""
                soma = id + "," + nome + "," + curso + "," + tpc1 + "," + tpc2 + "," + tpc3 + "," + tpc4 + "," + media + "," + escalao[0] + "\n"
                file.write(soma)
            file.close()
    return lista1

def distribEscalão(lista):
    if len(lista[1]) != 9:
        print("Faz primeiro a média")
    else:
        escaloes = {}
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
            if escalao in escaloes.keys():
                    escaloes[escalao] += 1
            else:
                escaloes[escalao] = 1
        return(escaloes)  

def grafico(distrib):
    x = distrib.keys()
    y = distrib.values()
    
    plt.plot(distrib.keys(), distrib.values(), marker = ".", markersize = 5)
    plt.title("Grafico de distribuições")
    plt.show()

def tabela(distrib):
    x = list(distrib.keys())
    y = list(distrib.values())

    for i in range(len(x)):
        print(f"| {x[i]:^10} - {y[i]:^10} |")










