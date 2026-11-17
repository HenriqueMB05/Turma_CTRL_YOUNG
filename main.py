import calculadora as calc

while True:
    var = int(input("0 para sair: "))

    match var:
        case 1:
            print(calc.soma(2,3))
        case 2:
            print(calc.subtracao(5,2))
        case 3:
            print(calc.multiplicacao(2,3))
        case 4:
            print(calc.divisao(10,2))
        case 5:
            print(calc.pontencia(2,3))
        case 6:
            print(calc.raiz_quadrada(6))
        case 0:
            break