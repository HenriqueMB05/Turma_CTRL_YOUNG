def add_lista_usando_for():
    lista = []
    for i in range(1,11):
        lista.append(int(input(f"Digite o número {i}: ")))
    return lista

def add_lista_usando_while():
    lista = []
    i = 1
    while i <= 10:
        lista.append(int(input(f"Digite o número {i}: ")))
        if len(lista) == 10:
            break
    return lista

def verificar_qual_maior(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
        else:
            continue
    return maior


a = add_lista_usando_for()
b = verificar_qual_maior(a)

print(b)