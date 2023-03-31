import random
import time


def busca_binaria1(valor):
    vetor = sorted(random.sample(range(100), 50))
    esquerda = 0
    direita = len(vetor) - 1

    inicio = time.time()
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == valor:
            resultado = meio
            fim = time.time()
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            print("Tempo de execução: ", fim - inicio, "segundos")
            return meio
        elif vetor[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    fim = time.time()
    print(f"O valor {valor} não foi encontrado no vetor.")
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_binaria2(valor):
    vetor = sorted(random.sample(range(10000), 5000))
    esquerda = 0
    direita = len(vetor) - 1

    inicio = time.time()
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == valor:
            resultado = meio
            fim = time.time()
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            print("Tempo de execução: ", fim - inicio, "segundos")
            return meio
        elif vetor[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    fim = time.time()
    print(f"O valor {valor} não foi encontrado no vetor.")
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_binaria3(valor):
    vetor = sorted(random.sample(range(1000000), 500000))
    esquerda = 0
    direita = len(vetor) - 1

    inicio = time.time()
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == valor:
            resultado = meio
            fim = time.time()
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            print("Tempo de execução: ", fim - inicio, "segundos")
            return meio
        elif vetor[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    fim = time.time()
    print(f"O valor {valor} não foi encontrado no vetor.")
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1


def busca_binaria4(valor):
    vetor = sorted(random.sample(range(10000000), 5000000))
    esquerda = 0
    direita = len(vetor) - 1

    inicio = time.time()
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == valor:
            resultado = meio
            fim = time.time()
            print(f"O valor {valor} está no índice {resultado} do vetor.")
            print("Tempo de execução: ", fim - inicio, "segundos")
            return meio
        elif vetor[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    fim = time.time()
    print(f"O valor {valor} não foi encontrado no vetor.")
    print("Tempo de execução: ", fim - inicio, "segundos")
    return -1