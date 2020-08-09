#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


import sys
import time
import curses
import random
import os

# main window
screen = curses.initscr()

# main window size
screen_x, screen_y = screen.getmaxyx()

if screen_x < 24 or screen_y < 81:
	screen.clear()
	curses.endwin()
	print('Current terminal size: {} x {}'.format(screen_x, screen_y))
	print('\nYour terminal must have at least 24 lines per 81 columns.\n')
	print('Readjust the size of your terminal to be able to play ... \n')
	sys.exit(0)


screen.notimeout(False)
screen.keypad(True)
screen.clear()

# updates the screen automatically but causes loss of performance
# can be used in place of screen.refresh() function calls
# screen.immedok(True)

# screen.set_title('G E N I U S')

curses.mousemask(curses.ALL_MOUSE_EVENTS)

# starting colors
curses.start_color()
curses.use_default_colors()

# Defines 'buttonhole' colors
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

# Defines side box color
curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Sets text color
curses.init_pair(12, curses.COLOR_BLUE, curses.COLOR_WHITE)

# Sets color of the Status Bar
curses.init_pair(13, curses.COLOR_WHITE, curses.COLOR_CYAN)

# Sets the color of the splash screen
curses.init_pair(14, curses.COLOR_GREEN, curses.COLOR_WHITE)

# Defines error message color
curses.init_pair(15, curses.COLOR_RED, curses.COLOR_WHITE)

curses.cbreak()

# Does not return characters on the screen
curses.noecho()

# moves the cursor to the 0,0 position
# screen.move(0,0)

# hides the mouse and terminal cursor
curses.curs_set(0)

# Defines Constants
K_CTRL_Q = 17
K_ESC    = 27
K_1      = 49
K_2      = 50
K_3      = 51
K_4      = 52

# Defines Constants used as special characters
# Single-line
# Chr( 218 ) + Chr( 196 ) + Chr( 191 ) ┌ ─ ┐
# Chr( 179 ) + Chr(  32 ) + Chr( 179 ) │   │
# Chr( 192 ) + Chr( 196 ) + Chr( 217 ) └ ─ ┘

c_032 = chr(  32) # space
c_177 = chr(9619) # block
c_179 = chr(9474)
c_191 = chr(9488)
c_192 = chr(9492)
c_196 = chr(9472)
c_217 = chr(9496)
c_218 = chr(9484)


class Box:

	def Fill(lt,ce,lb,cd, cor):
		#Draws a borderless and shadowless box
		for x in range(lt,lb+1):
			screen.addstr(x, ce, c_032 * (cd-ce+1), curses.color_pair(cor))

	def Display(lt,ce,lb,cd,cor):
		#Draws a box with borders and no shadows
		
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
		#Draws a box with borders and shadows
		
		__class__.Display(lt,ce,lb,cd,cor)

		#Draw the Shadow of the Box
		for x in range(lt+1,lb+1):
			screen.addstr(x, cd+1, c_032, curses.color_pair(0))
		
		screen.addstr(lb+1, ce+1, c_032 * (cd-ce+1), curses.color_pair(0))


def Beep(duration = .1, frequency = 3000):
	#curses.beep()

	#os.system('beep -f %s -l %s' % (frequency,duration))
	#os.system('beep -f 555 -l 460')

	# Note:
    # Play is a command line utility (shell), so you can use it
    # install the sox package via apt-get on Debian
    # To test play directly in bash copy and paste the line below:
	#play --no-show-progress --null -t alsa --channels 1 synth .5 sine 1000
	try:
		os.system('play --no-show-progress --null -t alsa --channels 1 synth %s sine %f' % (duration, frequency))
	except:
		pass


def pause(time):
	# Updates the screen
	screen.refresh()

	# Pause for a while
	time.sleep(time)

	# Clears anything else the user has typed
	curses.flushinp()


def author():
	# Shows the opening screen
    # Obs: The 'fonts' used were created through the program
    # figlet - http://www.figlet.org/
    # type the cmd below to see the available fonts
    # showfigfonts
    # type the cmd below to create the file with the text
    # figlet -f big "G e n i u s" >> genius.txt
    # figlet -f small "Version 1.0" >> genius.txt

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
                                     
	screen.addstr(17, 15, 'author: Víctor Donola Ferreira (vdonoladev)', curses.color_pair(12))
	screen.addstr(18, 15, 'Rua Divino, 64 - Centro', curses.color_pair(12))
	screen.addstr(19, 28, 'Carangola - Minas Gerais', curses.color_pair(12))


def inkey():

	while True:

		try:
			key = screen.getch()

			if key == curses.KEY_MOUSE:
				# left mouse button was pressed
				_, mx, my, _, _ = curses.getmouse()
				#screen.addstr (22, 1,"my = %i | mx = %i" % (my, mx))

				# Check which position was pressed
				#        lines            columns 
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
			# closes the program
			screen.addstr(23, 1, 'Game aborted ...       ', curses.color_pair(13) | curses.A_BOLD)
			pause(3)
			CLOSE()

		elif key in (curses.KEY_F1, ord('h'), ord('H')):
			# help triggered
			return 0

		elif key == K_1:
			return 1

		elif key == K_2:
			return 2

		elif key == K_3:
			return 3

		elif key == K_4:
			return 4


def showButton(n, cor=0):
	#Draw the button
	button = {1:(4,4,10,24), 2:(4,26,10,46), 3:(12,4,18,24), 4:(12,26,18,46)}
	label = {1:(7,13), 2:(7,35), 3:(15,13), 4:(15,35)}
	beep  = [500, 1100, 700, 900]

	Box.Display(*button[n], cor=cor)

	screen.addstr(label[n][0], label[n][1], ' %s ' % n, curses.color_pair(12))

	if cor: Beep(.12, beep[n-1])


def screen_display():
	#Creates a frame on the screen with blue char and white background
	Box.Display(0,0,23,79,12)

	Box.Display(1,50,22,77,11)
	screen.addstr( 3, 55, 'Genius versão 1.0', curses.color_pair(10))

	screen.addstr( 6, 54, 'by: Víctor Donola ', curses.color_pair(10))
	
	screen.addstr( 9, 52, 'My version of the Simon', curses.color_pair(10))
	screen.addstr(11, 53, 'electronic memory game', curses.color_pair(10))
	
	screen.addstr(14, 56, 'This program is', curses.color_pair(10))
	screen.addstr(16, 57, 'free software', curses.color_pair(10))

	screen.addstr(19, 52, 'Copyright (c) 2020-2021', curses.color_pair(10))

	#Write the title
	screen.addstr(2, 20, 'G E N I U S', curses.color_pair(12) | curses.A_BOLD)

	#Draw the buttons
	for n in (1,2,3,4):
		showButton(n, n)

	#Clear the Status Bar
	screen.addstr(23, 0, c_032 * 80, curses.color_pair(13))
	pause(.01)

def CLOSE():
	#Restores the color of the terminal
	screen.refresh()
	screen.clear()
	screen.keypad(False)
	curses.nocbreak()
	curses.echo()
	curses.endwin()
	sys.exit(0)


def generatesequence(size=10):
	return ''.join(random.choice('1234') for _ in range(size))

def main():
	msg   = {1:'Green button   ', 2:'Yellow button ', 3:'Red button', 4:'Blue button    '}

	#Print the splash screen
	screen_display()

	author()

	for _ in range(5):
		# The screen is flashing (changing color)
		curses.init_pair(14, random.randint(0, 7), curses.COLOR_WHITE)
		pause(.7)

	niveis      = 32
	seq_pc      = generatesequence(niveis)
	seq_user    = ''
	dificuldade = 1

	screen_display()

	while True:

		# shows the sequence generated by the computer (for debugging only)
		#screen.addstr(21, 1, 'sequencia -> %s    ' % seq_pc[:dificuldade], curses.color_pair(12))

		#Clear the Status Bar
		screen.addstr(23, 0, c_032 * 80, curses.color_pair(13))
		screen.addstr(23, 61, 'Dificuldade: %5i ' % dificuldade, curses.color_pair(13) | curses.A_BOLD)
		pause(1)

		for n in range(dificuldade):
			showButton(int(seq_pc[n]), 0)
			pause(.2)
			showButton(int(seq_pc[n]), int(seq_pc[n]))
			pause(.2)


		while True:

			button = inkey()

			if   button == 0:
				# help triggered
				author()

				screen.addstr(23, 1, 'Hit something to leave ...', curses.color_pair(13) | curses.A_BOLD)

				# The command below causes the call to getch () to be returned later
                # of a time simulating the CLIPPER inkey function (<time>)
				curses.halfdelay(7)

				while True:
					key = screen.getch()
					if key != -1:break
					# The screen is flashing (changing color)
					curses.init_pair(14, random.randint(0, 7), curses.COLOR_WHITE)
					screen.refresh()

				screen_display()
				#continue
				break

			elif 1 <= button <= 4:
				#Click the button
				screen.addstr(23, 1, msg[button], curses.color_pair(13) | curses.A_BOLD)
				showButton(button, 0)
				pause(.01)
				showButton(button, button)
				pause(.01)

				seq_user += str(button)

				if seq_user == seq_pc:
					Box.Shadow(9,23,15,55,12)
					
					screen.addstr(11, 25, 'Congratulations!!! You got it...', curses.color_pair(12))
					screen.addstr(13, 25, 'Want to Play Again? (Y / N)', curses.color_pair(12))
					pause(.01)
					key = screen.getch()

					if key in (ord('Y'), ord('y')):
						seq_pc      = generatesequence(niveis)
						seq_user    = ''
						dificuldade = 1
						screen_display()
						break
					else:
						CLOSE()

				elif seq_user == seq_pc[:len(seq_user)]:
					if len(seq_user) == dificuldade:
						screen.addstr(23, 16, 'OK  Next level...', curses.color_pair(13) | curses.A_BOLD)
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
					
					screen.addstr(11, 26, 'You missed ...', curses.color_pair(15) | curses.A_BLINK)
					screen.addstr(13, 26, 'Want to Play Again? (Y / N)', curses.color_pair(12))
					pause(.01)
					key = screen.getch()

					if key in (ord('Y'), ord('y')):
						seq_pc      = generatesequence(niveis)
						seq_user    = ''
						dificuldade = 1
						screen_display()
						break
					else:
						CLOSE()


if __name__ == '__main__':
	try:
		curses.wrapper(main())
	except KeyboardInterrupt:
		CLOSE()