# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame  
from constants import *
from circleshape import *

#var to keep infitnie while loop to make game screen black




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock # using to setup FPS limit at 60
    clock_timer = pygame.time.Clock() # instance of pygame.time.Clock to be used inside loop
    dt = 0


    while True: # infitnie loop that make game running 
        clock_timer.tick(60)
        dt = clock_timer.tick(60)/1000      
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # press escape on keyboard to exit game
                    return        
            if event.type == pygame.QUIT: # click close ikon at window level to exit game
                return        
        screen.fill((0, 0, 0))
        pygame.display.flip()
    



if __name__ == "__main__":
    main()