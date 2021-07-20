# Calculadora em Python
# Autor - Marcelo de Lima Nogueira
# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.

som = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b

def ask():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            return val
            

print("\n******************* Python Calculator *******************")
print('\nSelecione o número da operação desejada: ')
print('\n1 - SOMA \n2 - SUBTRAÇÃO \n3 - MULTIPLICAÇÃO \n4 - DIVISÃO')

continuar = 'y'
while(continuar == 'y'):
    try:
        opcao = int(input('\nInforme sua opção (1/2/3/4): '))
    except ValueError:
        print('\nOpção inválida!')
        continuar = input('\nDeseja continuar na calculadora (y/n): ')
    else:
        if(int(opcao) == 1):
            try:
                a = ask()
                b = ask()
            except ValueError:
                print("\nVocê não digitou um número!")
            else:
                print('\nA soma de %d + %d = %d' % (a,b,som(a,b)))
            finally:
                continuar = input('\nDeseja continuar na calculadora (y/n): ')
        elif(int(opcao) == 2):
            try:
                a = ask()
                b = ask()
            except ValueError:
                print("\nVocê não digitou um número!")
            else:
                print('\nA subtração de %d - %d = %d' % (a,b,sub(a,b)))
            finally:
                continuar = input('\nDeseja continuar na calculadora (y/n): ')
        elif(int(opcao) == 3):
            try:
                a = ask()
                b = ask()
            except ValueError:
                print("\nVocê não digitou um número!")
            else:
                print('\nA multiplicação de %d * %d = %d' % (a,b,mul(a,b)))
            finally:
                continuar = input('\nDeseja continuar na calculadora (y/n): ')
        elif(int(opcao) == 4):
            try:
                a = ask()
                b = ask()
                print('\nA divisão de %d / %d = %d' % (a,b,div(a,b)))
            except ValueError:
                print("\nVocê não digitou um número!")
            except ZeroDivisionError:
                print('\nDivisão por zero invalida!')
            finally:
                continuar = input('\nDeseja continuar na calculadora (y/n): ')   
        else:
            print('\nOpção inválida!')
            continuar = input('\nDeseja continuar na calculadora (y/n): ')
