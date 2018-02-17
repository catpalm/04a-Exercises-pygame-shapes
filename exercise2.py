#!/usr/bin/env python
'''

For this exercise, draw randomly-sized, randomly-colored, rectangles in random locations on the screen
It might be helpful to define a list of colors you want to use
hint: where you place the screen.fill(black) will affect whether or not the squares persist on the screen

'''
import sys, pygame, random
#random is not importing due to an error
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	(x,y,width,height) = (100,100,50,50)
    #I wanted to change each of the numbers listed into random integers, with randint(1,100) for the x and y with randint(1,50) for height and width.

	while True:
		clock.tick(FPS)

		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
		color = red
		pygame.draw.rect(screen, color, (x,y,width,height))
#I wished to copy this above code block a total of fouor times, for four squares in different places, but since random is not importing, I am unable to do so.
        #it should also be noted that anything I post in that code block becomes unreachable, no matter where I place it. Unless I delete a part of the code and replace it

#
#most likely, I am doing something wrong outside of python to get this error, but I am unsure of what it is. The import error with random seems to be the most detrimental, since without it
#I cannot perform what I am wanting to. The unreachable code error is also another one.

if __name__ == '__main__':
	main()