import pygame
import os
from sys import exit
from random import randint

def display_current_score():
    current_ticks =pygame.time.get_ticks()- start_game
    current_time = int(current_ticks/1000)
    score_surface = my_font.render(f"{current_time}", False, "pink")
    score_rect = score_surface.get_rect(center = (720,50))
    pygame.draw.ellipse(screen,"blue",score_rect.scale_by(1.3,1.3))
    screen.blit(score_surface,score_rect)
    return current_ticks

def display_score():
    current_ticks =pygame.time.get_ticks()- start_game
    current_time = int(current_ticks/1000)
    score_surface = my_font.render(f"{score}", False, "pink")
    score_rect = score_surface.get_rect(center = (400,120))
    pygame.draw.ellipse(screen,"blue",score_rect.scale_by(1.3,1.3))
    screen.blit(score_surface,score_rect)
    return current_ticks

def obstacle_movement(obstacle_list,direccion):
    if obstacle_list:
        obstacle_in_center= False
        obstacle_in_left= False
        obstacle_in_right = False
        for obstacle_rect in obstacle_list:
            if (obstacle_rect.x==400):
                obstacle_in_center = True 
            obstacle_rect.x -= direccion
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface_reversed,obstacle_rect)
                    
            if obstacle_rect.bottom == 301:
            
                screen.blit(snail_surface,obstacle_rect)

            if obstacle_rect.bottom == 200:
                screen.blit(fly_surface,obstacle_rect)
            if obstacle_rect.bottom == 201:
                screen.blit(fly_surface_reversed,obstacle_rect)



            if (obstacle_rect.x < -100 and obstacle_in_center ==True) or(obstacle_rect.x > 900 and obstacle_in_center == True):
                del obstacle_rect
            

            
        return obstacle_list
        
    else: return[]
def collision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

             



#basicos

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Juego de Quique")
clock = pygame.time.Clock()
my_font_small =pygame.font.Font("font/pixel.ttf", 50)
my_font = pygame.font.Font("font/pixel.ttf", 80)
my_font_big = pygame.font.Font("font/pixel.ttf", 120)
game_active = False
start_game = 0
score = 0
game_start = 0
tiki = False
user_text = ""
meter_datos_finalizado = True
check_highscore = True
obstacle_in_center= False
loop = 0
#highscore



names = []
scores = []
highscore_document = open("highscores.txt", "r+")
names_scores = highscore_document.read()
names_scores = names_scores.split("..") 
names = names_scores[0].split("-")
scorestxt = (names_scores[1].split(", "))

for score_ in scorestxt:
        score_ = int(score_)
        scores.append(score_)
highscore_document.close()
 
higscore = False

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1200)
    




#fondo
background_surface = pygame.image.load("graphics/background.png").convert_alpha()

mountain_surface = pygame.image.load("graphics/mountain.png").convert_alpha()

floor_surface = pygame.image.load("graphics/floor.png").convert()

cloud_surface = pygame.image.load("graphics/cloud.png").convert_alpha()
cloud_rect = cloud_surface.get_rect(center = (000,100))
cloud_speed= 1

#textos

text_surface = my_font.render("Quique vs Snails", False, "Blue")
text_rect = text_surface.get_rect(center = (400,50))

game_over_surface = my_font.render("GAME OVER",False,"pink")
game_over_rect = game_over_surface.get_rect(center = (400,200))

strt_surface = my_font.render("START",False,"pink")
strt_rect = strt_surface.get_rect(center = (170,200))

strt_ag_surface = my_font_big.render("START AGAIN?",False,"pink")
strt_ag_rect = strt_ag_surface.get_rect(center = (400,350))

higscore_surface = my_font.render("HIGHSCORE",False,"pink")
highscore_rect = higscore_surface.get_rect(center = (630,200))

higscore_from_game_over_surface = my_font_small.render("HIGHSCORE",False,"pink")
highscore_from_game_over_rect = higscore_from_game_over_surface.get_rect(topleft = (20,15))

back_surface = my_font.render(" BACK ",False,"pink")
back_rect = back_surface.get_rect(center = (90,50))

back_menu_surface = my_font.render(" MENU ",False,"pink")
back_menu_rect = back_menu_surface.get_rect(center = (90,50))

higscore_title_surface = my_font.render("HIGHSCORE",False,"pink")
highscore_title_rect = higscore_title_surface.get_rect(center = (400,50))

#DATOSHIGHSCORE
higscore_onename_surface = my_font.render("1. " + names[0],False,"pink")
highscore_onename_rect = higscore_onename_surface.get_rect(midleft = (150,100))
higscore_onescore_surface = my_font.render(str(scores[0]),False,"pink")
highscore_onescore_rect = higscore_onescore_surface.get_rect(midright = (700,100))

higscore_twoname_surface = my_font.render("2. " + names[1],False,"pink")
highscore_twoname_rect = higscore_twoname_surface.get_rect(midleft = (150,150))
higscore_twoscore_surface = my_font.render(str(scores[1]),False,"pink")
highscore_twoscore_rect = higscore_twoscore_surface.get_rect(midright = (700,150))

higscore_threename_surface = my_font.render("3. " + names[2],False,"pink")
highscore_threename_rect = higscore_threename_surface.get_rect(midleft = (150,200))
higscore_threescore_surface = my_font.render(str(scores[2]),False,"pink")
highscore_threescore_rect = higscore_threescore_surface.get_rect(midright = (700,200))

higscore_fourname_surface = my_font.render("4. " + names[3],False,"pink")
highscore_fourname_rect = higscore_fourname_surface.get_rect(midleft = (150,250))
higscore_fourscore_surface = my_font.render(str(scores[3]),False,"pink")
highscore_fourscore_rect = higscore_fourscore_surface.get_rect(midright = (700,250))

higscore_fivename_surface = my_font.render("5. " + names[4],False,"pink")
highscore_fivename_rect = higscore_fivename_surface.get_rect(midleft = (150,300))
higscore_fivescore_surface = my_font.render(str(scores[4]),False,"pink")
highscore_fivescore_rect = higscore_fivescore_surface.get_rect(midright = (700,300))

new_highscore_surface = my_font.render("New Highscore! Enter Name:",False,"pink")
new_highscore_rect = new_highscore_surface.get_rect(midtop = (400,200))
new_highscore_rect_two = new_highscore_surface.get_rect(midtop = (400,250))


user_text_surface = my_font.render(user_text,False,"pink")
user_text_rect = user_text_surface.get_rect(center = (300,275))

#enemigos
    #snail
snail_surface = pygame.image.load("graphics/snail1.png").convert_alpha()
snail_surface_reversed = pygame.image.load("graphics/snail1_reversed.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


snail_rect_list_derecha = []
snail_rect_list_izquierda = []
print(type(snail_rect_list_derecha))
    #fly
fly_surface = pygame.image.load("graphics/fly1.png").convert_alpha()
fly_surface_reversed= pygame.image.load("graphics/fly1_reversed.png").convert_alpha()
fly_rect_list =[]
fly_rect_list_reversed= []
print(type(fly_rect_list_reversed))



#snail_rect_list_derecha = obstacle_movement(snail_rect_list_derecha,5)
#snail_rect_list_izquierda = obstacle_movement(snail_rect_list_izquierda,-5)

#player

player_walk_one_surface = pygame.image.load("graphics/player_walk_1.png").convert_alpha()
player_walk_one_reversed_surface = pygame.image.load("graphics/player_walk_1_left.png").convert_alpha()
player_walk_two_surface = pygame.image.load("graphics/player_walk_2.png").convert_alpha()
player_walk_two_reversed_surface =pygame.image.load("graphics/player_walk_2_left.png").convert_alpha()

player_jump_surface = pygame.image.load("graphics/player_jump.png").convert_alpha()
player_jump_left_surface = pygame.image.load("graphics/player_jump_left.png").convert_alpha()

player_walk_list =[player_walk_one_surface,player_walk_two_surface]
player_walk_list_reversed =[player_walk_one_reversed_surface,player_walk_two_reversed_surface]

player_full_list =[player_walk_one_surface,player_walk_two_surface, player_walk_one_reversed_surface , player_walk_two_reversed_surface , player_jump_surface, player_jump_left_surface]

player_index = 0
player_rect = player_full_list[player_index].get_rect(midbottom=(400,300))
player_gravity = 0
player_movement = 0
player_left= True
player_right= False

#pantalla inicio

player_surface_scaled = pygame.transform.scale2x(player_walk_one_surface)
player_rect_start = player_walk_one_surface.get_rect(midbottom =(360,220))

#abrir y cerrar programa

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #salto jugador
        if event.type == pygame.KEYDOWN and player_rect.bottom >= 300 and game_active is True:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
                
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_movement = 6
                player_index = 0
                player_index += 0.1
                if player_index >= 2: player_index = 0 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_movement = 0
                player_index = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_index=2
                player_index+= 0.1
                if player_index >=4 :player_index = 2
                player_movement = -6 
                player_right=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_movement = 0  
                player_right =False
                player_index = 2    
        #volver a jugar
        if event.type == pygame.KEYDOWN and game_active == False and tiki == True:
            if event.key == pygame.K_SPACE:
                start_game = pygame.time.get_ticks()                    
                game_active = True
                game_start += 1
        if event.type== pygame.MOUSEBUTTONDOWN and game_active == False:
            if strt_ag_rect.collidepoint(event.pos) or strt_rect.collidepoint(event.pos):
                start_game = pygame.time.get_ticks()
                game_active = True
                game_start += 1
                check_highscore = True
            if highscore_rect.collidepoint(event.pos):
                higscore = True
            if back_rect.collidepoint(event.pos):
                game_start = 0
                higscore = False
            if back_menu_rect.collidepoint(event.pos):
                higscore = False
            if highscore_from_game_over_rect.collidepoint(event.pos):
                higscore = True
        if event.type == obstacle_timer and game_active:
            decision_direction =(randint(0,5))
            print(type(snail_rect_list_derecha))
            print(type(fly_rect_list))
            if decision_direction == 0 or decision_direction ==1:
                snail_derecha =0
                snail_rect_list_derecha.append(snail_surface_reversed.get_rect(midbottom = (randint(900,1200),301)))
                
                snail_derecha +=1
            elif decision_direction ==2 or decision_direction == 3:
                snail_rect_list_izquierda.append(snail_surface.get_rect(midbottom = (randint(-400,-100),300)))
                  
                snail_izq = 0
                snail_izq+= 1
            elif decision_direction== 4:
                fly_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1200),200)))
                fly_der = 0
                fly_der+= 1
            elif decision_direction== 5: 
                fly_izq = 0
                fly_izq+= 1
                fly_rect_list_reversed.append(fly_surface_reversed.get_rect(midbottom = (randint(-400,-100),201)))
            #print("derecha",snail_rect_list_derecha)
            #print("izquierda", snail_rect_list_izquierda)
            print(fly_rect_list)
            print(fly_rect_list_reversed)

        #input texto
        if event.type == pygame.KEYDOWN and game_active == False and meter_datos_finalizado == False:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_SPACE:
                nothing = 1
            elif event.key == pygame.K_RETURN:
                nothing = 1
            
            else: 
                user_text += event.unicode
                print(event)
    
                
                
                
           
#pantalla inicio

    if game_start == 0 and higscore == False : 
        screen.fill("#003366")
        screen.blit(background_surface,(0,0))
        screen.blit(cloud_surface,cloud_rect)
        screen.blit(mountain_surface,(0,0))
        screen.blit(floor_surface,(0,300))
        screen.blit(player_surface_scaled,player_rect_start)
        pygame.draw.ellipse(screen,"pink",text_rect.scale_by(1.2,1.2))
        screen.blit(text_surface,text_rect)
        pygame.draw.rect(screen,"black",strt_rect.scale_by(1.22,1.37))
        pygame.draw.rect(screen,"blue",strt_rect.scale_by(1.2,1.2))
        screen.blit(strt_surface,strt_rect)
        pygame.draw.rect(screen,"black",highscore_rect.scale_by(1.22,1.37))
        pygame.draw.rect(screen,"blue",highscore_rect.scale_by(1.2,1.2))
        screen.blit(higscore_surface,highscore_rect)
        
        cloud_rect.x += cloud_speed
        if cloud_rect.x >= 900:
            cloud_rect.x = -200
        if event.type== pygame.MOUSEMOTION:
            if strt_rect.collidepoint(event.pos):
                pygame.draw.rect(screen,"#281879",strt_rect.scale_by(1.2,1.2))
                
            else:
                pygame.draw.rect(screen,"blue",strt_rect.scale_by(1.2,1.2))
            screen.blit(strt_surface,strt_rect)  
        if event.type== pygame.MOUSEMOTION:
            if highscore_rect.collidepoint(event.pos):
                pygame.draw.rect(screen,"#281879",highscore_rect.scale_by(1.2,1.2))
                
            else:
                pygame.draw.rect(screen,"blue",highscore_rect.scale_by(1.2,1.2))
            screen.blit(higscore_surface,highscore_rect)
        if check_highscore == True:
            higscore_onename_surface = my_font.render("1. " + names[0],False,"pink")
            higscore_twoname_surface = my_font.render("2. " + names[1],False,"pink")
            higscore_threename_surface = my_font.render("3. " + names[2],False,"pink")
            higscore_fourname_surface = my_font.render("4. " + names[3],False,"pink")
            higscore_fivename_surface = my_font.render("5. " + names[4],False,"pink")
            higscore_onescore_surface = my_font.render(str(scores[0]),False,"pink")
            higscore_twoscore_surface = my_font.render(str(scores[1]),False,"pink")
            higscore_threescore_surface = my_font.render(str(scores[2]),False,"pink")
            higscore_fourscore_surface = my_font.render(str(scores[3]),False,"pink")
            higscore_fivescore_surface = my_font.render(str(scores[4]),False,"pink")
            names = []
            scores = []
            highscore_document = open("highscores.txt", "r+")
            names_scores = highscore_document.read()
            names_scores = names_scores.split("..") 
            names = names_scores[0].split("-")
            scorestxt = (names_scores[1].split(", "))

            for score_ in scorestxt:
                score_ = int(score_)
                scores.append(score_)
            highscore_document.close()
            check_highscore = False
    
    #pantalla highscores

    elif higscore == True:
        screen.fill("#003366")
        screen.blit(background_surface,(0,0))
        screen.blit(cloud_surface,cloud_rect)
        screen.blit(mountain_surface,(0,0))
        screen.blit(floor_surface,(0,300))
        pygame.draw.ellipse(screen,"black",highscore_title_rect.scale_by(1.22,1.37))
        pygame.draw.ellipse(screen,"blue",highscore_title_rect.scale_by(1.2,1.2))
        pygame.draw.rect(screen,"black",back_rect.scale_by(1.25,1.37))
        pygame.draw.rect(screen,"blue",back_rect.scale_by(1.2,1.2))
        screen.blit(back_surface,back_rect)
        screen.blit(higscore_title_surface,highscore_title_rect)
        screen.blit(higscore_onename_surface,highscore_onename_rect)
        screen.blit(higscore_onescore_surface,highscore_onescore_rect)
        screen.blit(higscore_twoname_surface,highscore_twoname_rect)
        screen.blit(higscore_twoscore_surface,highscore_twoscore_rect)
        screen.blit(higscore_threename_surface,highscore_threename_rect)
        screen.blit(higscore_threescore_surface,highscore_threescore_rect)
        screen.blit(higscore_fourname_surface,highscore_fourname_rect)
        screen.blit(higscore_fourscore_surface,highscore_fourscore_rect)
        screen.blit(higscore_fivename_surface,highscore_fivename_rect)
        screen.blit(higscore_fivescore_surface,highscore_fivescore_rect)

        if event.type== pygame.MOUSEMOTION:
            if back_rect.collidepoint(event.pos):
                pygame.draw.rect(screen,"#281879",back_rect.scale_by(1.2,1.2))
                
            else:
                pygame.draw.rect(screen,"blue",back_rect.scale_by(1.2,1.2))
            screen.blit(back_surface,back_rect)

#pantalla juego
            
    elif game_active:
        #score = int(display_current_score())
        
        screen.fill("#003366")
        screen.blit(background_surface,(0,0))
        screen.blit(cloud_surface,cloud_rect)
        screen.blit(mountain_surface,(0,0))
        screen.blit(floor_surface,(0,300))
        if score <10:
            fly_rect_list=obstacle_movement(fly_rect_list,5)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-5)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 5)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-5) 
        if score >= 10 and score <25:
            fly_rect_list=obstacle_movement(fly_rect_list,7)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-7)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 6)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-6)
        if score >= 25 and score <40:
            fly_rect_list=obstacle_movement(fly_rect_list,8)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-8)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 7)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-7)
        if score >= 40 and score <55:
            fly_rect_list=obstacle_movement(fly_rect_list,8)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-8)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 7)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-7)
        if score >= 55 and score <70:
            fly_rect_list=obstacle_movement(fly_rect_list,10)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-10)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 8)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-8)
        if score >= 70 and score < 85:
            fly_rect_list=obstacle_movement(fly_rect_list,11)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-11)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 9)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-9)
        if score >= 85:
            fly_rect_list=obstacle_movement(fly_rect_list,12)
            fly_rect_list_reversed=obstacle_movement(fly_rect_list_reversed,-12)
            snail_rect_list_derecha= obstacle_movement(snail_rect_list_derecha, 9)
            snail_rect_list_izquierda= obstacle_movement(snail_rect_list_izquierda,-9)
        
        
        

        screen.blit(player_full_list[int(player_index)],player_rect)
        score = int(display_current_score()/1000)
        print(int(player_index))
    
        player_gravity += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                player_index += 0.1
                if player_index >= 2: player_index = 0 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                     
                player_index += 0.1
                if player_index >= 4: player_index = 2 
                
        player_rect.y += player_gravity
        if player_rect.x <= 0:
            player_rect.x= 0
        if player_rect.x >= 735:
            player_rect.x= 735
        
        player_rect.x += player_movement
        if player_rect.bottom > 300: player_rect.bottom =300
        
        cloud_rect.x += cloud_speed
        if cloud_rect.x >= 900:
            cloud_rect.x = -200

        loop = 1

        #movimiento snail
        
        #snail_rect.x -= snail_speed
        if collision(player_rect,snail_rect_list_derecha)== False or collision(player_rect,snail_rect_list_izquierda)== False or collision(player_rect,fly_rect_list)== False or collision(player_rect,fly_rect_list_reversed)== False:
            game_active= False
            print("collision")
        
        
        
        

 #pantalla game over       
    
    else:
        print(fly_rect_list)
        print(fly_rect_list_reversed)
        screen.fill("#003366")
        screen.blit(background_surface,(0,0))
        screen.blit(cloud_surface,cloud_rect)
        screen.blit(mountain_surface,(0,0))
        screen.blit(floor_surface,(0,300))
        #pygame.draw.rect(screen,"blue",snail_rect)
        #pygame.draw.rect(screen,"orange",player_rect)
        
        screen.blit(player_walk_one_surface,player_rect)
        display_score()
        snail_rect_list_derecha.clear()
        snail_rect_list_izquierda.clear()
        fly_rect_list.clear()
        fly_rect_list_reversed.clear()
        player_rect.x =400

        pygame.draw.ellipse(screen,"pink",text_rect.scale_by(1.2,1.2))
        screen.blit(text_surface,text_rect)
        screen.blit(game_over_surface,game_over_rect)
        pygame.draw.rect(screen,"black",strt_ag_rect.scale_by(1.22,1.37))
        pygame.draw.rect(screen,"blue",strt_ag_rect.scale_by(1.2,1.2))
        screen.blit(strt_ag_surface,strt_ag_rect)
        pygame.draw.rect(screen,"black",back_menu_rect.scale_by(1.3,1.37))
        pygame.draw.rect(screen,"blue",back_menu_rect.scale_by(1.2,1.2))
        screen.blit(back_menu_surface,back_menu_rect)
        cloud_rect.x += cloud_speed
        if cloud_rect.x >= 900:
            cloud_rect.x = -200
        new_score = int(score)
       
        
        if new_score > (scores[4]):

            if loop == 1:
                meter_datos_finalizado= False
                loop += 1

            
            if meter_datos_finalizado == False and tiki == False:
                
                print(user_text)
                pygame.draw.rect(screen,"black",new_highscore_rect.scale_by(1,1))
                pygame.draw.rect(screen,"black",new_highscore_rect_two.scale_by(1,1))
                screen.blit(new_highscore_surface,new_highscore_rect)
                user_text_surface = my_font.render(user_text,True,"pink")
                screen.blit(user_text_surface,user_text_rect)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        name_to_save = user_text
                        user_text = ""
                        meter_datos_finalizado = True
            elif tiki == False and meter_datos_finalizado == True:
                print('3')
                scores.append(new_score)
                scores.sort(reverse = True)
                scores.pop()
                index_new_score = scores.index(new_score)
                names.insert(index_new_score,name_to_save)
                names.pop()
                names_final = []
                        
                for eachname in names:
                    name = (eachname + "-")
                    names_final.append(name)    
                names_final.pop()
                names_final = ''.join(names_final)
                scoresstring = ''.join(str(scores))
                scoresstring =scoresstring.replace("[", "")
                scoresstring =scoresstring.replace("]", "")
                highscore_document = open("highscores.txt", "w")
                highscore_document.write(names_final + ".." + scoresstring)
                highscore_document.close()
                tiki = True
                
                
            
                        

                        
            
            new_score = 0
             
            
            
    
        
        if event.type== pygame.MOUSEMOTION:
            if strt_ag_rect.collidepoint(event.pos):
                pygame.draw.rect(screen,"#281879",strt_ag_rect.scale_by(1.2,1.2))
                
            else:
                pygame.draw.rect(screen,"blue",strt_ag_rect.scale_by(1.2,1.2))
            screen.blit(strt_ag_surface,strt_ag_rect)
            if back_menu_rect.collidepoint(event.pos):
                pygame.draw.rect(screen,"#281879",back_menu_rect.scale_by(1.2,1.2))
                
            else:
                pygame.draw.rect(screen,"blue",back_menu_rect.scale_by(1.2,1.2))
            screen.blit(back_menu_surface,back_menu_rect)

        
                
            


        
                                    
    
    pygame.display.update()
    clock.tick(60)