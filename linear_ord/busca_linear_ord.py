import random
import time


def busca_linear_ordenada1(valor):
    vetor = sorted(random.sample(range(100), 50))
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
        elif vetor[i] > valor:
            print(f"O valor {valor} não está no vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return -1
    print(f"O valor {valor} não está no vetor.")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_linear_ordenada2(valor):
    vetor = sorted(random.sample(range(10000), 5000))
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
        elif vetor[i] > valor:
            print(f"O valor {valor} não está no vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return -1
    print(f"O valor {valor} não está no vetor.")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1

def busca_linear_ordenada3(valor):
    vetor = sorted(random.sample(range(1000000), 500000))
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
        elif vetor[i] > valor:
            print(f"O valor {valor} não está no vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return -1
    print(f"O valor {valor} não está no vetor.")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_linear_ordenada4(valor):
    vetor = sorted(random.sample(range(10000000), 5000000))
    inicio = time.time()
    for i in range(len(vetor)):
        if vetor[i] == valor:
            resultado = i
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return i
        elif vetor[i] > valor:
            print(f"O valor {valor} não está no vetor.")
            fim = time.time()
            print("Tempo de execução: ", fim - inicio, "segundos")
            return -1
    print(f"O valor {valor} não está no vetor.")
    fim = time.time()
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1