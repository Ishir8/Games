import pygame
import random
import math
#Important line
pygame.init()

#screen
screen = pygame.display.set_mode((800,600))
game_state = True 
#title and icon
pygame.display.set_caption("Space invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
hitSound = pygame.mixer.Sound('invaderkilled.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
#background
background = pygame.image.load("ship.png")
BACK = pygame.transform.scale(background,(800,600))


#player
playerimg = pygame.image.load("space-invaders.png")
retryimg = pygame.image.load("retry.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
num_of_enemies = 6
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =  []
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('spaceship.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(40)
#enemy bullet
bullet1X = 0
bullet1Y = 0
bullet1X_change = 0
bullet1Y_change = 5
bullet1_state = 'read'
bullet1img = pygame.image.load('bomb.png')

        
def shoot(x,y):
    global bullet1X 
    global bullet1Y
    global bullet1X_change
    global bullet1Y_change
    global bullet1img
    bullet1X += bullet1X_change
    bullet1Y += bullet1Y_change
    screen.blit(bullet1img,(x,y))
    
def shoot_bullet():
    global bullet1X 
    global bullet1Y
    global bullet1X_change
    global bullet1Y_change
    global bullet1img
    bullet_enem = random.randint(0,5)
    bullet1X = enemyX[bullet_enem]
    bullet1Y = enemyY[bullet_enem]

#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change =  10
bullet_state = 'ready'
num = 0

#score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
scoreX = 10
scoreY = 10
def score_s(x,y):
    score_show = font.render("score: " + str(score),True,(255,255,255))
    screen.blit(score_show,(x,y))
#detect the distance between enemy and bullet by maths

def collision(enemX,enemY,bulleX,bulleY):
    distance = math.sqrt((math.pow(enemX-bulleX,2)) + (math.pow(enemY - bulleY,2)))
    if distance < 27 :
        return True
        score += 1
    

def bullet(x,y):
  global bullet_state
  bullet_state = 'fire'
  screen.blit(bulletimg,(x+16,y+10))
  
  
def player(x,y):
  screen.blit(playerimg,(x,y))

def enemy(x,y,i):
  screen.blit(enemyimg[i],(x,y))
over = pygame.font.Font('freesansbold.ttf',64)
over1 = pygame.font.Font('freesansbold.ttf',34)
#game over text
def game_over_text():
    global player,playerX,playerY,playerX_change,enemyX,enemyY,num_of_enemies,enemyX_change,enemyY_change,enemyimg,bullet1X,bullet1Y_change,bullet1Y,bullet1X_change,score,game_state
    game_over = over.render("GAME OVER",True,(255,255,255))
    reset = over1.render("PRESS R TO PLAY AGAIN",True,(0, 255,255))
    score11 = over1.render("YOUR SCORE WAS " + str(score) + "!",True,(255,0,0))
    #R = over1.render("PRESR",True,(255,255,255))
    screen.blit(reset,(200,15))
    #screen.blit(R,(400,200))
    screen.blit(score11,(200,420))
    screen.blit(game_over,(200,250))
    screen.blit(retryimg,(350,70))
    game_state = False
    
    #for event in pygame.event.get():
        #if event.type == pygame.KEYDOWN:
           

   # hitSound.play()
  
#game loop
running = True
while running:
    #red,green and blue
    screen.fill((0,0,0))
    screen.blit(BACK,(0,0))
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          #keystroke
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  playerX_change = -5
              if event.key == pygame.K_RIGHT:
                   playerX_change = 5
              if event.key == pygame.K_r and game_state == False:
                print(game_state)
                score = 0
                playerX = 370
                playerY = 480
                playerX_change = 0
                game_state = True
                #enemy
                num_of_enemies = 6
                enemyimg = []
                enemyX = []
                enemyY = []
                enemyX_change = []
                enemyY_change =  []
                for i in range(num_of_enemies):
                    enemyimg.append(pygame.image.load('spaceship.png'))
                    enemyX.append(random.randint(0,736))
                    enemyY.append(random.randint(50,150))
                    enemyX_change.append(3)
                    enemyY_change.append(40)
                #enemy bullet
                bullet1X = 0
                bullet1Y = 0
                bullet1X_change = 0
                bullet1Y_change = 5
                bullet1_state = 'read'
                
               
              
              if event.key == pygame.K_SPACE:
              
              
                  if bullet_state == 'ready':
                  
                      bulletX = playerX
                      bullet(bulletX,bulletY)
          if event.type == pygame.KEYUP :
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0
                  
#distace 2.0
    distance2 = math.sqrt((math.pow(playerX-bullet1X,2)) + (math.pow(playerY - bullet1Y,2)))
    if distance2 < 50 and bullet1X > playerX:
        
        for i in range(num_of_enemies):
            enemyY_change[i] = 0
            enemyX_change[i] = 0
        for j in range(num_of_enemies):
                enemyY[j] = 20000
        game_over_text()
    elif distance2 < 20 and bullet1X < playerX:
        for i in range(num_of_enemies):
            enemyY_change[i] = 0
            enemyX_change[i] = 0
        for j in range(num_of_enemies):
                enemyY[j] = 20000
        game_over_text()
#bullet change
    if bulletY <= 0 :
      bulletY =  480
      bullet_state = 'ready'
      
    if bullet_state == "fire" :
      bullet(bulletX,bulletY)
      bulletY -= bulletY_change
    
#put boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
        
        
#enemy boundaries
    for i in range(num_of_enemies):
        #game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                game_over_text()
                
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        
#collsion detection
        colli = collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if colli:
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            hitSound.play()
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
            
#put stuff above screen.fill or it will come underneath
    player(playerX,playerY)
#score
    score_s(scoreX,scoreY)
    
    
#random bullet test
    rando = random.randint(1,20)
    if rando == 1:
        if bullet1_state != 'fire':
            bullet1_state = 'fire'
            
            shoot_bullet()
        
#enemy bullet
    if bullet1_state == 'fire':
        shoot(bullet1X,bullet1Y)
       
        if bullet1Y > 800 or distance2 < 27:
            bullet1_state = 'read'
            
        font
        
#important line
    pygame.time.delay(10)
    pygame.display.update()
    