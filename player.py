from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self,x,y,shots):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shots=shots
        self.shot_delay= 0

        
    def triangle(self):
       forward = pygame.Vector2(0, 1).rotate(self.rotation)
       right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
       a = self.position + forward * self.radius
       b = self.position - forward * self.radius - right
       c = self.position - forward * self.radius + right
       return [a, b, c]    

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt) # value need to be negative to rotate left

        if keys[pygame.K_RIGHT]:
            self.rotate(dt)   
       
        if keys[pygame.K_UP]:    
           self.move(dt)

        if keys[pygame.K_DOWN]: # actually this was supposed to make ship move backwards but make it accelerate which is cooler ;) 
            self.move(dt)  

        if keys[pygame.K_SPACE]: # actually this was supposed to make ship move backwards but make it accelerate which is cooler ;) 
            self.shoot()

        if self.shot_delay > 0:  # logic that will count time from shot cd (0,3) until next shot
            self.shot_delay -= dt
            self.shot_delay= max(0,self.shot_delay)            

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_delay == 0:

           shot = Shot(self.position.x, self.position.y)
           velocity = pygame.Vector2(0, 1)
           velocity = velocity.rotate(self.rotation)
           velocity = velocity * PLAYER_SHOOT_SPEED
           shot.velocity= velocity
           for container in Shot.containers:
            if isinstance(container, pygame.sprite.Group):
                container.add(shot)
           self.shot_delay = PLAYER_SHOOT_COOLDOWN # starting 0,3 cd between each shot

            
        

                 