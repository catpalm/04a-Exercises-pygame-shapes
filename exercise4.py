#!/usr/bin/env python
'''

For this exercise, draw a circle wherever the user clicks the mouse

'''
import sys, pygame
from datetime import datetime
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("arial",64)
	clock = pygame.time.Clock()

	(x, y, radius) = (100, 100, 20)
	screen.fill(black)
	while True:
		clock.tick(FPS)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				pygame.draw.circle(screen, white, pos, radius)
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				pygame.draw.circle(screen, white, pos, radius)

		pygame.draw.circle(screen, white, (x,y), radius)
		
		pygame.display.flip()

if __name__ == '__main__':
	main()