#criando uma lista
frutas = ["Maçã","Manga", "Melancia", "Goiaba", "Laranja"]
comidas = list()

#mostrando os valores da lista
print(frutas) # toda a lista
print(frutas[0]) #mostrando um valor pelo indice

for f in frutas: #toda a lista
    print(f)

# Adicionando valores na lista
for i in range(5):
    comidas.append(str(input("Digite o nome da comida: ")))

# Remover valores da lista
for i in range(len(frutas)):
    frutas.pop()

print(frutas)
