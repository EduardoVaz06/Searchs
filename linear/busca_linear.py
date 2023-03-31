import random
import time


def busca_linear1(valor):
    vetor = random.sample(range(100), 50)
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
    print("Valor não encontrado")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_linear2(valor):
    vetor = random.sample(range(10000), 5000)
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
    print("Valor não encontrado")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1

def busca_linear3(valor):
    vetor = random.sample(range(1000000), 500000)
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
    print("Valor não encontrado")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_linear4(valor):
    vetor = random.sample(range(10000000), 5000000)
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
    print("Valor não encontrado")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1