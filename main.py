# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame  
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock # using to setup FPS limit at 60
    clock_timer = pygame.time.Clock() # instance of pygame.time.Clock to be used inside loop
    dt = 0

    updatable=pygame.sprite.Group() # player
    drawable=pygame.sprite.Group()  ## groups 

    asteroids = pygame.sprite.Group() #groups for asteroids object


    #Tell the Player class which groups to join
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create the Player instance at the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
     # Create the asteroid field
    asteroid_field = AsteroidField()
    print("Updatable group size:", len(updatable))
    print("Drawable group size:", len(drawable))
    print("Asteroids group size:", len(asteroids))


    while True: # infitnie loop that make game running 
        
        dt = clock_timer.tick(60)/1000      
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # press escape on keyboard to exit game
                    return        
            if event.type == pygame.QUIT: # click close ikon at window level to exit game
                return
         
        for sprite in updatable:
            sprite.update(dt)

        for a in asteroids:
            if player.collision_check(a):
                print("Game Over")
                sys.exit()                
        
        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)

               
        pygame.display.flip()
    



if __name__ == "__main__":
    main()