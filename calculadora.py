import math as m

def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def pontencia(a: float, b: float) -> float:
    return m.pow(a, b) 

def raiz_quadrada(a: float) -> float:
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return m.sqrt(a)