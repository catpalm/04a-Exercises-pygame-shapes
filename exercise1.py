#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2
#imports system version info
screen_size = (800,600)
#sets the screen size to 800 by 600 pixels"
FPS = 60
#sets the frame rate to 60 frames"
def main():
#defines main
	pygame.init()
	#initiates pygame"
	screen = pygame.display.set_mode(screen_size)
	#sets the pygames window to the screen size that was earlier"
	clock = pygame.time.Clock()
	#sets the internal time of the program"

	while True:
		#while true statement for if main is true
		clock.tick(FPS)
		#sets the clock to tick to be synced with the FPS"
		screen.fill((0,0,0))
		#fills the screen with a color"

		for event in pygame.event.get():
			#sets up a "for" statement that happens if a certain thing happens
			if event.type == pygame.QUIT:
				#quits pygame if the event.type happens
				pygame.quit()
				#quits pygame
				sys.exit(0)
				#exits python

		pygame.display.flip()
	#flips the display
if __name__ == '__main__':
	#sets if the name is equal to main
	main()
	#this is just main.