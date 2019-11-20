# -*- coding: UTF-8 -*-
import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavra.txt","r")
    lista = [fruta.upper() for fruta in arquivo]
    palavra_secreta = lista[random.randrange(len(lista)+1)].strip()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erro = 0

    print("A palavra secreta contém {} letra(s). {}".format(len(palavra_secreta), letras_acertadas))

    while not enforcou and not acertou:
        chute = input("Qual a primeira letra ?")
        chute = chute.strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index = index + 1

        palavra_completa = ""
        for l in letras_acertadas:
            palavra_completa += l

        if palavra_completa == palavra_secreta:
            acertou = True
            print("Parabens! Voce acertou a palavra secreta -> {}.".format(palavra_completa))
        else:
            erro += 1

        enforcou = erro == len(palavra_secreta)

        if enforcou:
            print("Perdeu e você foi enforcado! Fim do Jogo!")
        else:
            print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()
