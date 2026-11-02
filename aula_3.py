frutas = ["maçã", "banana", "laranja", "uva", "pera", "melancia", "abacaxi", "kiwi", "manga", "morango"]
comidas=list()

for fruta in frutas:
    print(fruta)

print()
print()
print(frutas[6])


#Adicionando Valores a lista
for i in range(5):
    print("Digite o nome de uma comida:")
    comidas.append(input(""))

#excluindo valores da lista
for i in frutas:
    print(i)
    frutas.pop()

for i in range(len(frutas)):
    frutas.pop()

print(frutas)