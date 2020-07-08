#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


import sys
import time
import curses
import random
import os

# janela principal
screen = curses.initscr()

# tamanho da janela principal
screen_x, screen_y = screen.getmaxyx()

if screen_x < 24 or screen_y < 81:
	screen.clear()
	curses.endwin()
	print('Tamanho atual do terminal: {} x {}'.format(screen_x, screen_y))
	print('\nO seu terminal tem que ter no minimo 24 linhas por 81 colunas.\n')
	print('Reajuste o tamanho do seu terminal para poder jogar... \n')
	sys.exit(0)


screen.notimeout(False)
screen.keypad(True)
screen.clear()

# atualiza a tela automaticamente mais causa perda de performance
# pode ser usado no lugar das chamadas da funcao  screen.refresh()
#screen.immedok(True)

#screen.set_title('G E N I U S')

curses.mousemask(curses.ALL_MOUSE_EVENTS)

# iniciando cores
curses.start_color()
curses.use_default_colors()

# Define as cores dos 'botãozões'
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

# Define cor do box lateral
curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Define cor dos textos
curses.init_pair(12, curses.COLOR_BLUE, curses.COLOR_WHITE)

# Define cor da Barra de Status
curses.init_pair(13, curses.COLOR_WHITE, curses.COLOR_CYAN)

# Define cor da tela de abertura
curses.init_pair(14, curses.COLOR_GREEN, curses.COLOR_WHITE)

# Define cor da mensagem de error
curses.init_pair(15, curses.COLOR_RED, curses.COLOR_WHITE)

curses.cbreak()

# Não retorna caracteres na tela
curses.noecho()

# move o cursor para a posicao 0,0
#screen.move(0,0)

# esconde o cursor do mouse e do terminal
curses.curs_set(0)

# Define Constantes
K_CTRL_Q = 17
K_ESC    = 27
K_1      = 49
K_2      = 50
K_3      = 51
K_4      = 52

# Define Constantes usadas como caracteres especiais
# Single-line
# Chr( 218 ) + Chr( 196 ) + Chr( 191 ) ┌ ─ ┐
# Chr( 179 ) + Chr(  32 ) + Chr( 179 ) │   │
# Chr( 192 ) + Chr( 196 ) + Chr( 217 ) └ ─ ┘

c_032 = chr(  32) # espaço
c_177 = chr(9619) # bloco
c_179 = chr(9474)
c_191 = chr(9488)
c_192 = chr(9492)
c_196 = chr(9472)
c_217 = chr(9496)
c_218 = chr(9484)


class Box:

	def Fill(lt,ce,lb,cd, cor):
		#Desenha uma caixa sem bordas e sem sombras
		for x in range(lt,lb+1):
			screen.addstr(x, ce, c_032 * (cd-ce+1), curses.color_pair(cor))

	def Display(lt,ce,lb,cd,cor):
		#Desenha uma caixa com bordas e sem sombras
		
		__class__.Fill(lt,ce,lb,cd,cor)

		screen.addstr(lt, ce, c_196 * (cd-ce), curses.color_pair(cor))
		screen.addstr(lt, ce, c_218, curses.color_pair(cor))
		screen.addstr(lt, cd, c_191, curses.color_pair(cor))
		
		screen.addstr(lb, ce, c_196 * (cd-ce), curses.color_pair(cor))
		screen.addstr(lb, ce, c_192, curses.color_pair(cor))
		screen.addstr(lb, cd, c_217, curses.color_pair(cor))

		for x in range(lt+1,lb):
			screen.addstr(x, ce, c_179, curses.color_pair(cor))
			screen.addstr(x, cd, c_179, curses.color_pair(cor))

	def Shadow(lt,ce,lb,cd,cor):
		#Desenha uma caixa com bordas e com sombras
		
		__class__.Display(lt,ce,lb,cd,cor)

		#Desenha a Sombra da Caixa
		for x in range(lt+1,lb+1):
			screen.addstr(x, cd+1, c_032, curses.color_pair(0))
		
		screen.addstr(lb+1, ce+1, c_032 * (cd-ce+1), curses.color_pair(0))


def Beep(duration = .1, frequency = 3000):
	#curses.beep()

	#os.system('beep -f %s -l %s' % (frequency,duration))
	#os.system('beep -f 555 -l 460')

	# Observação:
	# O play é um utilitário de linha de comando (shell), para poder usa-lo
	# instale o Pacote sox atraves do apt-get no Debian
	# Para testar o play direto no bash copie e cole a linha abaixo:
	#play --no-show-progress --null -t alsa --channels 1 synth .5 sine 1000
	try:
		os.system('play --no-show-progress --null -t alsa --channels 1 synth %s sine %f' % (duration, frequency))
	except:
		pass


def pause(tempo):
	# Atualiza a tela
	screen.refresh()

	# Pausa por um tempo
	time.sleep(tempo)

	# Limpa qualquer outra coisa que o usuário tenha digitado
	curses.flushinp()


def autor():
	# Mostra a tela de abertura
	# Obs: As 'fontes' usadas foram criadas através do programa
	# figlet - http://www.figlet.org/
	# digite o cmd abaixo para ver as fontes disponiveis
	# showfigfonts
	# digite o cmd abaixo para criar o arquivo com o texto
	# figlet -f big "G e n i u s" >> genius.txt 
	# figlet -f small "Versao 1.0" >> genius.txt 

	Box.Shadow(1,10,20,68,12)

	screen.addstr( 4, 18, '  _____                  _                ', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr( 5, 18, ' / ____|                (_)               ', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr( 6, 18, '| |  __    ___   _ __    _   _   _   ___  ', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr( 7, 18, '| | |_ |  / _ \ | \'_ \  | | | | | | / __|', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr( 8, 18, '| |__| | |  __/ | | | | | | | |_| | \__ \\', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr( 9, 18, ' \_____|  \___| |_| |_| |_|  \__,_| |___/ ', curses.color_pair(14) | curses.A_BOLD)

	screen.addstr(11, 20, '__   __           __         _   __  ', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr(12, 20, '\ \ / /__ _ _ ___ __ _ ___  / | /  \ ', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr(13, 20, ' \ V / -_) \'_(_-</ _` / _ \ | || () |', curses.color_pair(14) | curses.A_BOLD)
	screen.addstr(14, 20, '  \_/\___|_| /__/\__,_\___/ |_(_)__/ ', curses.color_pair(14) | curses.A_BOLD)
                                     
	screen.addstr(17, 15, 'Autor: Víctor Donola Ferreira (vdonoladev)', curses.color_pair(12))
	screen.addstr(18, 15, 'Rua Antônio Marques, 64 - Triângulo', curses.color_pair(12))
	screen.addstr(19, 28, 'Carangola - Minas Gerais', curses.color_pair(12))


def inkey():

	while True:

		try:
			key = screen.getch()

			if key == curses.KEY_MOUSE:
				# botao esquerdo do mouse foi pressionado
				_, mx, my, _, _ = curses.getmouse()
				#screen.addstr (22, 1,"my = %i | mx = %i" % (my, mx))

				# Verifica em que posicao foi pressionado
				#        linhas            colunas 
				if   ( 4 <= my <= 10) and ( 4 <= mx <= 24):
					return 1

				elif ( 4 <= my <= 10) and (26 <= mx <= 46):
					return 2

				elif (12 <= my <= 18) and ( 4 <= mx <= 24):
					return 3

				elif (12 <= my <= 18) and (26 <= mx <= 46):
					return 4

		except curses.error:
			pass


		if key in (K_ESC, K_CTRL_Q, ord('q'), ord('Q')):
			# encerra o programa
			screen.addstr(23, 1, 'Jogo abortado...       ', curses.color_pair(13) | curses.A_BOLD)
			pause(3)
			ENCERRA()

		elif key in (curses.KEY_F1, ord('h'), ord('H')):
			# help acionado
			return 0

		elif key == K_1:
			return 1

		elif key == K_2:
			return 2

		elif key == K_3:
			return 3

		elif key == K_4:
			return 4


def showBotao(n, cor=0):
	#Desenha o botãozão
	botao = {1:(4,4,10,24), 2:(4,26,10,46), 3:(12,4,18,24), 4:(12,26,18,46)}
	label = {1:(7,13), 2:(7,35), 3:(15,13), 4:(15,35)}
	beep  = [500, 1100, 700, 900]

	Box.Display(*botao[n], cor=cor)

	screen.addstr(label[n][0], label[n][1], ' %s ' % n, curses.color_pair(12))

	if cor: Beep(.12, beep[n-1])


def display_tela():
	#Cria um quadro na tela com char azul e fundo branco
	Box.Display(0,0,23,79,12)

	Box.Display(1,50,22,77,11)
	screen.addstr( 3, 55, 'Genius versão 1.0', curses.color_pair(10))

	screen.addstr( 6, 54, 'by: Víctor Donola ', curses.color_pair(10))
	
	screen.addstr( 9, 52, 'My version of the Simon', curses.color_pair(10))
	screen.addstr(11, 53, 'electronic memory game', curses.color_pair(10))
	
	screen.addstr(14, 56, 'This program is', curses.color_pair(10))
	screen.addstr(16, 57, 'free software', curses.color_pair(10))

	screen.addstr(19, 52, 'Copyright (c) 2020-2021', curses.color_pair(10))

	#Escreve o titulo
	screen.addstr(2, 20, 'G E N I U S', curses.color_pair(12) | curses.A_BOLD)

	#Desenha os botões
	for n in (1,2,3,4):
		showBotao(n, n)

	#Limpa a Barra de Status
	screen.addstr(23, 0, c_032 * 80, curses.color_pair(13))
	pause(.01)

def ENCERRA():
	#Restaura a cor do terminal
	screen.refresh()
	screen.clear()
	screen.keypad(False)
	curses.nocbreak()
	curses.echo()
	curses.endwin()
	sys.exit(0)


def gerasequencia(size=10):
	return ''.join(random.choice('1234') for _ in range(size))

def main():
	msg   = {1:'Botão verde   ', 2:'Botão amarelo ', 3:'Botão vermelho', 4:'Botão azul    '}

	#Imprimi a tela de abertura
	display_tela()

	autor()

	for _ in range(5):
		# Fica piscando a tela (mudando de cor)
		curses.init_pair(14, random.randint(0, 7), curses.COLOR_WHITE)
		pause(.7)

	niveis      = 32
	seq_pc      = gerasequencia(niveis)
	seq_user    = ''
	dificuldade = 1

	display_tela()

	while True:

		# mostra a sequencia gerada pelo computador (só pra depuração)
		#screen.addstr(21, 1, 'sequencia -> %s    ' % seq_pc[:dificuldade], curses.color_pair(12))

		#Limpa a Barra de Status
		screen.addstr(23, 0, c_032 * 80, curses.color_pair(13))
		screen.addstr(23, 61, 'Dificuldade: %5i ' % dificuldade, curses.color_pair(13) | curses.A_BOLD)
		pause(1)

		for n in range(dificuldade):
			showBotao(int(seq_pc[n]), 0)
			pause(.2)
			showBotao(int(seq_pc[n]), int(seq_pc[n]))
			pause(.2)


		while True:

			botao = inkey()

			if   botao == 0:
				# help acionado
				autor()

				screen.addstr(23, 1, 'Tecle algo para sair...', curses.color_pair(13) | curses.A_BOLD)

				# O comando abaixo faz com que a chamada a getch() retorne depois
				# de um tempo simulando a função inkey(<tempo>) do CLIPPER
				curses.halfdelay(7)

				while True:
					key = screen.getch()
					if key != -1:break
					# Fica piscando a tela (mudando de cor)
					curses.init_pair(14, random.randint(0, 7), curses.COLOR_WHITE)
					screen.refresh()

				display_tela()
				#continue
				break

			elif 1 <= botao <= 4:
				#Aciona o botãozão
				screen.addstr(23, 1, msg[botao], curses.color_pair(13) | curses.A_BOLD)
				showBotao(botao, 0)
				pause(.01)
				showBotao(botao, botao)
				pause(.01)

				seq_user += str(botao)

				if seq_user == seq_pc:
					Box.Shadow(9,23,15,55,12)
					
					screen.addstr(11, 25, 'Parabéns!!! Você conseguiu...', curses.color_pair(12))
					screen.addstr(13, 25, 'Quer Jogar Novamente? (S/N) ', curses.color_pair(12))
					pause(.01)
					key = screen.getch()

					if key in (ord('S'), ord('s')):
						seq_pc      = gerasequencia(niveis)
						seq_user    = ''
						dificuldade = 1
						display_tela()
						break
					else:
						ENCERRA()

				elif seq_user == seq_pc[:len(seq_user)]:
					if len(seq_user) == dificuldade:
						screen.addstr(23, 16, 'OK  Próximo nivel...', curses.color_pair(13) | curses.A_BOLD)
						pause(2)
						seq_user     = ''
						dificuldade += 1
						break

					else:
						screen.addstr(23, 16, 'OK', curses.color_pair(13) | curses.A_BOLD)
						pause(.05)

				else:
					Beep(.2, 2000)
					Beep(.2, 1600)
					Beep(.2, 2200)
					screen.addstr(23, 16, 'NOK', curses.color_pair(13) | curses.A_BOLD)
					Box.Shadow(9,23,15,55,15)
					
					screen.addstr(11, 26, 'Você   E R R O U ...', curses.color_pair(15) | curses.A_BLINK)
					screen.addstr(13, 26, 'Quer Jogar Novamente? (S/N)', curses.color_pair(12))
					pause(.01)
					key = screen.getch()

					if key in (ord('S'), ord('s')):
						seq_pc      = gerasequencia(niveis)
						seq_user    = ''
						dificuldade = 1
						display_tela()
						break
					else:
						ENCERRA()


if __name__ == '__main__':
	try:
		curses.wrapper(main())
	except KeyboardInterrupt:
		ENCERRA()