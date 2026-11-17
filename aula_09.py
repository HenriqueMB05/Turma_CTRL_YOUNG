import math 


def calcular_hipotenusa(a: float,b:float,c:float):
    if a+b>c and a+c>b and b+c>a:
        if c == math.sqrt(math.pow(a,2) + math.pow(b,2)):
            return "É um triângulo retângulo"
        pass
    else:
        return "Não é um triângulo"

