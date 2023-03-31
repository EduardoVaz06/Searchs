import time

from binaria import busca_binaria
from linear import busca_linear
from linear_ord import busca_linear_ord

if __name__ == '__main__':

    busca_linear.busca_linear1(int(input("Vetor 50 - Digite um valor inteiro: ")))
    busca_linear.busca_linear2(int(input("Vetor 5.000 - Digite um valor inteiro: ")))
    busca_linear.busca_linear3(int(input("Vetor 500.000 - Digite um valor inteiro: ")))
    busca_linear.busca_linear4(int(input("Vetor 5.000.000 - Digite um valor inteiro: ")))

    busca_linear_ord.busca_linear_ordenada1(int(input("Vetor Ordenado 50 - Digite um valor inteiro: ")))
    busca_linear_ord.busca_linear_ordenada2(int(input("Vetor Ordenado 5.000 - Digite um valor inteiro: ")))
    busca_linear_ord.busca_linear_ordenada3(int(input("Vetor Ordenado 500.000 - Digite um valor inteiro: ")))
    busca_linear_ord.busca_linear_ordenada4(int(input("Vetor Ordenado 5.000.000 - Digite um valor inteiro: ")))

    busca_binaria.busca_binaria1(int(input("Busca Binária 50 - Digite um valor inteiro: ")))
    busca_binaria.busca_binaria2(int(input("Busca Binária 5.000 - Digite um valor inteiro: ")))
    busca_binaria.busca_binaria3(int(input("Busca Binária 500.000 - Digite um valor inteiro: ")))
    busca_binaria.busca_binaria4(int(input("Busca Binária 5.000.000 - Digite um valor inteiro: ")))

