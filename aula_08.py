#w (write)
#r (read)
#r+ (read and write)
#a (append)


nome = "henrique"

with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
   arquivo.write(f"Olá, boa noite meu nome é: {nome}")


with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    #conteudo = arquivo.read()
    #print(conteudo)
    #conteudo = arquivo.readline()
   # for linha in arquivo:
   #     if linha.strip() == "chave":
    #        print("Jogo original")
    #        break
    #conteudo = arquivo.readlines()
    #print(conteudo)
    pass


with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nAdicionando mais uma linha")

