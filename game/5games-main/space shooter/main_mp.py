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
#plain_rect = pyg.FRect()

#imports

player_surf = pyg.image.load(join('images','player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (win_width/2,4*win_height/5))

star = pyg.image.load(join("images","star.png")).convert_alpha()
star_pos =[(random.randint(0,win_width),random.randint(0,win_height)) for i in range(20)]

meteor_surf = pyg.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (win_width/2,win_height/2))

laser_surf = pyg.image.load(join('images','laser.png'))
laser_rect = laser_surf.get_frect()


player_direction = pyg.math.Vector2()
player_speed = 350


while running:
    dt = clock.tick() /1000
    #print(clock.get_fps())
    #print(dt)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        #if event.type == pyg.KEYDOWN and event.key == pyg.K_LEFT:
        #    print('left')
        if event.type == pyg.MOUSEMOTION:                                      #checks if key had been pressed
            player_rect.center = event.pos


    #print(pyg.mouse.get_pos(), pyg.mouse.get_pressed(),pyg.mouse.get_rel())
    #player_rect.center =pyg.mouse.get_pos()
    #keys = pyg.key.get_pressed()                                               #checks in key is kept pressed 
    #if keys[pyg.K_1]:
    #    print(1)

    keys = pyg.key.get_pressed()
    keys_jp = pyg.key.get_just_pressed()
    player_direction.x = int(keys[pyg.K_RIGHT] or keys[pyg.K_d])-int(keys[pyg.K_LEFT] or keys[pyg.K_a])
    player_direction.y = int(keys[pyg.K_DOWN] or keys[pyg.K_s])-int(keys[pyg.K_UP] or keys[pyg.K_w])
    player_direction = player_direction.normalize() if player_direction else player_direction 
    #print(player_direction,(player_direction*player_speed).magnitude())
    if keys_jp[pyg.K_SPACE] or pyg.mouse.get_just_pressed()[0]:
        print('Fire laser')

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