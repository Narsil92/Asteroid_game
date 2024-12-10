# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame  
from constants import *

#var to keep infitnie while loop to make game screen black




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True: # infitnie loop that make game running 
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # press escape on keyboard to exit game
                    return 
        screen.fill((0, 0, 0))
        pygame.display.flip()
    



if __name__ == "__main__":
    main()