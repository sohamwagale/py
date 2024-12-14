import pygame as pyg
from os.path import join
import random
import math

pyg.init()

#intitalisation
win_height, win_width = 720,1280
display_surface = pyg.display.set_mode(( win_width,win_height))
running = True
pyg.display.set_caption("Aah..Shit!!!") 
clock = pyg.time.Clock()

#plain surface
surf = pyg.Surface((50,50))
surf.fill("lightgreen")

#plain rectnagle
plain_rect = pyg.FRect()

#imports

player_surf = pyg.image.load(join('images','player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (win_width/2,4*win_height/5))

star = pyg.image.load(join("images","star.png")).convert_alpha()
star_pos =[(random.randint(0,win_width),random.randint(0,win_height)) for i in range(20)]

meteor_surf = pyg.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (win_width/2,win_height/2))

laser_surf = pyg.image.load(join('images','laser.png'))
laser_rect = laser_surf.get_frect()


player_direction = pyg.math.Vector2(1,1)
player_speed = 200


while running:
    dt = clock.tick() /1000
    #print(clock.get_fps())
    #print(dt)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        if event.type == pyg.KEYDOWN and event.key == pyg.K_LEFT:
            print('left')
        if event.type == pyg.MOUSEMOTION:
            print('Mouse moving')


#movements implementation
    if player_rect.right > win_width or player_rect.left < 0:
        player_direction.x *=-1
    if player_rect.top < 0 or player_rect.bottom > win_height:
        player_direction.y *=-1
    player_rect.center += player_direction*player_speed*dt

    laser_rect.midbottom  = (player_rect.midtop[0] , player_rect.midtop[1] -10)   # x, y, width, height 
    


#displaying
    display_surface.fill('lightsalmon')
    for pos in star_pos:
        display_surface.blit(star, pos )
    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf,laser_rect)
    display_surface.blit(player_surf, player_rect)


    pyg.display.update()


pyg.quit()