import pygame
import random
import math
from pygame import mixer


pygame.init()

BG_COLOR = (55, 17, 49)
WHITE_COLOR = (255 , 255 ,  255)
RED_COLOR = (125, 170, 150)
SCREEN = pygame.display.set_mode((800 , 800))

X_CHANGE = 0
Y_CHANGE = 0
left_change = -0.5
right_change = +0.5
up_change = -0.5
down_change = +0.5
score = 0

x_val = []
y_val = []
prev_x_val = []
prev_y_val = []

number_of_blocks = 1

def draw_top_label():
    pygame.draw.rect(SCREEN ,(55, 29, 69), (0 , 0 , 800 , 80))
    

for i in range(number_of_blocks):
    x_val.append(300)
    y_val.append(300)
    prev_x_val.append(0)
    prev_y_val.append(0)
    







width = 30
height = 30
food_x = random.randint(0 , 700 )
food_y = random.randint(300 , 700 )



def show_score():
    font = pygame.font.Font('freesansbold.ttf' , 64)
    score_text = font.render("SCORE : "  + str(score) , True , WHITE_COLOR)
    SCREEN.blit(score_text , (220 , 10))
# def show_score():
#     font = pygame.font.Font('freesansbold.ttf' , 32)
#     score_text = font.render("Score : " + str(SCORE) , True , RED_COLOR)
#     screen.blit(score_text , (10 , 10))


def print_food():
    pygame.draw.rect(SCREEN , (0, 170, 69) , (food_x , food_y , 10 , 10 ) )


def print_snake_block():


    prev_x_val[i] = x_val[i]
    prev_y_val[i] = y_val[i]
    
        
    if i == 0:

 

        if x_entry:
            x_val[i] += X_CHANGE
            
        else:
        
            y_val[i] += Y_CHANGE
        
        
    else:

 
        x_val[i] = prev_x_val[i - 1]
        y_val[i] = prev_y_val[i - 1]


    pygame.draw.rect(SCREEN , RED_COLOR , (x_val[i] , y_val[i] , width , height))






    





    

def CHECK_COLLISION():
    distance = math.sqrt( (x_val[i] - food_x)**2 + (y_val[i] - food_y)**2 )
    if distance <= 30:
        return True
    else:
        return False

def CHECK_BLOCK_COLLISION():
    distance = math.sqrt( (x_val[i] - x_val[0])**2 + (y_val[i] - y_val[0])**2 )
    if distance == 0.1:
        return True
    else:
        return False
def game_over_screen():
    SCREEN.fill((47, 66, 114))
   
    font = pygame.font.SysFont('comicsansms' , 50)
    over_font = pygame.font.SysFont("comicsansms", 100)
    # over_font = pygame.font.Font('freesansbold.ttf' , 80 )
    over_text_1 = over_font.render("GAME OVER" , True , (0 , 0 , 0))
    over_text_2 = font.render("DEVELOPED BY : MALIK" , True  , (0 , 0 , 0))
    SCREEN.blit(over_text_1 , (110 , 200))
    SCREEN.blit(over_text_2 , (120 , 600))

RUNNING = True
x_entry = False
y_entry = False
i = 0
speed_incrementer = 0


# BACKGROUND SOUND
mixer.music.load('BACKGROUND_SOUND.wav')
mixer.music.play(-1)

game_over_entry = False

while RUNNING:
    if game_over_entry:
        game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
    
    else:
        SCREEN.fill(BG_COLOR)
        draw_top_label()
        show_score()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and X_CHANGE != right_change:
                    Y_CHANGE = 0
                    X_CHANGE = left_change
                    x_entry = True
                    y_entry = False
                elif event.key == pygame.K_RIGHT and X_CHANGE != left_change:
                    Y_CHANGE = 0
                    X_CHANGE = right_change
                    x_entry = True
                    y_entry = False
                elif event.key == pygame.K_UP and Y_CHANGE != down_change:
                    X_CHANGE = 0
                    Y_CHANGE = up_change
                    x_entry = False
                    y_entry = True
                elif event.key == pygame.K_DOWN and Y_CHANGE != up_change:
                    X_CHANGE = 0
                    Y_CHANGE = down_change
                    x_entry = False
                    y_entry = True

                


        print_food()

        for i in range(number_of_blocks):


            print_snake_block()


            if CHECK_COLLISION():

                EAT_sound = mixer.Sound('EAT.wav')
                EAT_sound.play()



                speed_incrementer += 1
                if speed_incrementer == 4:
                    speed_incrementer = 0
                    left_change *= 2
                    right_change *= 2
                    up_change *= 2
                    down_change *= 2

                score += 1
                show_score()


                food_x = random.randint(0 , 700 )
                food_y = random.randint(300 , 700 )



            
            
                number_of_blocks += 40
                for i in range(40):
                    x_val.append(-300)
                    y_val.append(-300)
          
                    prev_x_val.append(-300)
                    prev_y_val.append(-300)
            print_food()

            if x_val[i] == x_val[0] and y_val[i] == y_val[0] and i != 0:
                game_over_entry = True
       
        if x_val[0] <= 0 or x_val[0] >= 770  or y_val[0] <= 80 or y_val[0] >= 770:
                X_CHANGE = 0
                Y_CHANGE = 0
                right_change = 0
                left_change = 0
                up_change = 0 
                down_change = 0
                game_over_entry = True
                
        



            
        

    pygame.display.update()
game_over_screen