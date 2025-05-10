import pygame
import sys
from math import sin, cos, pi, atan2
pygame.init()
healht = 100
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World!")
MOUSE_POS = (0, 0)
def show_text(text, x, y, color, size):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def rad_to_deg(rad):
    return rad*180/pi

def deg_to_rad(deg):
    return deg*pi/180

def distance(x2, y2, x1, y1):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_facing(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y1 - y2
    return atan2(dy, dx)

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(1)

class Actor:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def move (self, dx, dy):
        self.x += dx
        self.y += dy
    
    def move_facing(self, facing, step):
        dx = cos(facing)*step
        dy = -sin(facing)*step
        self.move(dx,dy)

    def go_to(self, x, y):
        self.x = x
        self.y = y

    def refresh(self):
        self.pos = (self.x, self.y)
        self.draw(screen)

    '''
    def colliderent(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        else:
            return False
        
    def collidepoint(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        else:
            return False
    '''

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x - width/2
        self.y = y - height/2
        self.width = width
        self.height = height
        self.color = color
        self.pos = (self.x, self.y)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move (self, dx, dy):
        self.x += dx
        self.y += dy
    
    def move_facing(self, facing, step):
        dx = cos(facing)*step
        dy = -sin(facing)*step
        self.move(dx,dy)
    
    def go_to(self, x, y):
        self.x = x
        self.y = y

    def refresh(self):
        self.pos = (self.x, self.y)
        self.draw(screen)

    def colliderent(self, other):
        return bool(self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y)
        
    def collidepoint(self, pos):
        return bool(self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height)
    
    

player = Entity(400, 300, 50, 50, (0, 255, 0))
helper = Entity(25, 25, 50, 50, (0, 0, 255))
enemy = Entity(25, 25, 50, 50, (255, 0, 0))
enemy_rotate = 0
entity_speed = 5
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEMOTION:
            MOUSE_POS = event.pos
        '''
        elif event.type == pygame.KEYDOWN:
            #print("Key pressed: ", event.key)
            if event.key == pygame.K_SPACE:
                print("Space bar pressed")  
            if event.key == pygame.K_UP:
                player.move_facing(deg_to_rad(90), 10)
                #print("Up arrow pressed")
            if event.key == pygame.K_DOWN:
                player.move_facing(deg_to_rad(270), 10)
                #print("Down arrow pressed")
            if event.key == pygame.K_LEFT:
                player.move_facing(deg_to_rad(180), 10)
                #print("Left arrow pressed")
            if event.key == pygame.K_RIGHT:
                player.move_facing(0, 10)
                #print("Right arrow pressed")
        '''
    if player.colliderent(enemy):
        #show_text("Player collided with enemy", 400, 300, (255, 0, 0), 30)
        healht -= 10
        play_music("music/Pop.wav")
        enemy.go_to(25, 25)
        if healht <= 0:
            running = False
    enemy_rotate = get_facing(enemy.x, enemy.y, player.x, player.y)
    enemy.move_facing(enemy_rotate, entity_speed)
    if enemy.x < 0:
        enemy.x = 0
    if enemy.x > 800:
        enemy.x = 800
    if enemy.y < 0:
        enemy.y = 0
    if enemy.y > 600:
        enemy.y = 600
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player.y > 0:
            player.move_facing(deg_to_rad(90), entity_speed*1.5)
    if keys[pygame.K_DOWN]:
        if player.y < 550:
            player.move_facing(deg_to_rad(270), entity_speed*1.5)
    if keys[pygame.K_LEFT]:
        if player.x > 0:
            player.move_facing(deg_to_rad(180), entity_speed*1.5)
    if keys[pygame.K_RIGHT]:
        if player.x < 750:
            player.move_facing(0, entity_speed*1.5)
    if enemy.y > 0:
        enemy.move_facing(deg_to_rad(90), entity_speed)
    if enemy.y < 550:
        enemy.move_facing(deg_to_rad(270), entity_speed)
    if enemy.x > 0:
        enemy.move_facing(deg_to_rad(180), entity_speed)
    if enemy.x < 750:
        enemy.move_facing(0, entity_speed)
    screen.fill((255, 255, 255))
    player.refresh()
    enemy.refresh()
    helper.refresh()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()