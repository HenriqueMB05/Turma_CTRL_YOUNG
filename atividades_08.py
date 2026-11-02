def escrever_txt(parametro):
    with open("atividade.txt", "w", encoding="utf-8") as file:
            file.write(parametro)

escrever_txt("sim")