for i in range(10):
    if i%2 == 0:
        print(i)
    elif i%2 !=0:
       pass

"""num = int(input("Digite um número: "))
mult =num"""

"""for i in range(1, 11):
    mult = num * i
    print(mult)"""





pswd = input("Digite a senha: ")
pswddb = "123456"
senha = { "usuario": "admin",
          "usuario2": pswddb}
contador = 0


while pswddb == "123456":
    
    if pswd == pswddb:
        print("Acesso permitido.")
    else:
        print("Senha incorreta.", end=" ")
        pswd = input("Digite a senha: ")
        contador += 1
        if contador == 3:
            print("Acesso negado.")
            pswd = None
    print(f"Tentativa  restantes {3-contador}")

print("sai do loop")