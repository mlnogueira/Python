# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |Letra: %s
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.tam = len(word)
		self.composicao = ''
		print("Construindo o Objeto.")
	# Método para adivinhar a letra
	def guess(self, letter):
		for i in range(0, len(self.word)):
			self.composicao = self.composicao + '_'
		for indice, valor in enumerate(self.word):
			if (valor == letter):
				self.composicao = self.composicao[:indice] + valor + self.composicao[indice + 1:]
		print(self.composicao.count('_'))
		print(self.composicao)
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		print()
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		print("")
	# Método para não mostrar a letra no board
	def hide_word(self):
		print("")
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print("")

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
		return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():
	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	game.guess(input("Digite uma letra: "))

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

