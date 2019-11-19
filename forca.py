def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_",]

    enforcou = False
    acertou = False

    print("A palavra secreta contém {} letra(s). {}".format(len(palavra_secreta), letras_acertadas))

    while (not enforcou and not acertou):
        chute = input("Qual a primeira letra ?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index]= letra
            index = index + 1

        palavra_completa = ""
        for l in letras_acertadas:
            palavra_completa = palavra_completa + l

        if(palavra_completa == palavra_secreta):
            acertou = True
            print("Parabens! Voce acertou a palavra secreta {}.", palavra_completa)

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()
