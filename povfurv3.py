import pygame
from pygame.locals import *
#import dfur
import math
import socket
import sys
import time




d = []
def rotate(img, pos, angle):
    w, h = img.get_size()
    img2 = pygame.Surface((w*2, h*2), pygame.SRCALPHA)
    img2.blit(img, (w-pos[0], h-pos[1]))
    return pygame.transform.rotate(img2, angle)
 
pygame.init()
font =  pygame.font.SysFont('arial', 36)
screen = pygame.display.set_mode((800,800))
screen.fill((135, 206, 250))
pygame.display.set_caption("Вращение")
wd , hd = screen.get_size()
f = open('par.txt', 'r')
d = []
for line in f:
    d.append(int(line))
f.close()
f = open('osi.txt', 'r')
osi = []
for line in f:
    osi.append(int(line))
f.close()
k  = (d[1] - d[3] * 2  + d[4]) / ( hd * 0.75 ) 
wfur = d[0] // k
hfur = d[1] // k
hcab = d[2] // k
hsed = d[3] // k
mosi = osi
hpric = d[4] // k
hpricsed = d[5] // k
hcol = d[6] // k
dcol = d[7] // k
#dfur.fur(wfur , hfur , hcab , hsed , mosi)
#dfur.pric(wfur,hpric) 
#dfur.col(wfur  , dcol  )
imagec = pygame.image.load("fursv.png").convert_alpha()
imagecc = pygame.image.load("pricsv.png").convert_alpha()
imagecs = pygame.image.load("stena.png").convert_alpha()

# отрисовка колёс
imageccol1 = pygame.image.load("col.png").convert_alpha()
imageccol2 = pygame.image.load("col.png").convert_alpha()
center_imagecol = ( wfur // 20 , dcol // 2 )
angelcol = 0 
hcolofsed = hfur - hsed - hcol

#положение тягоча
hc = hfur-hsed+hsed//15
wc = wd // 2
pivot = (wc, hc ) # положение центра вращения на экране
angle = 0
center_image = (wfur // 2 ,hfur - hsed ) # положение центра вращения на изображении 
clock = pygame.time.Clock()

#положение прицепа
pivotc = (wc, hc ) # положение центра вращения на экране
anglec = 0
center_imagec = ( wfur // 2 ,  int (hpricsed) ) # положение центра вращения на изображении 



imagepric = rotate(imagecc, center_imagec , anglec)
rectc = imagepric.get_rect()
rectc.center = pivotc

imagef = pygame.image.load('fon.png').convert_alpha()
hsten1 = d[0]
hsten = d[0]
motion = [0,0,0,0,0,0,0,0,0,0,0]
running = True
points = []
ct = time.perf_counter()
minY = 200000

while running:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
        if  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                motion[7] = 1
            if  event.key == pygame.K_LEFT:
                motion[8] = 1
            if  event.key == pygame.K_UP:
                motion[1] = 1
            if  event.key == pygame.K_DOWN:
                motion[2] = 1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT]:
                motion[7] = 0
            if  event.key in [pygame.K_LEFT]:
                motion[8] = 0
            if  event.key in [pygame.K_UP]:
                motion[1] = 0
            if  event.key in [pygame.K_DOWN]:
                motion[2] = 0
    
    if motion[1] == 1:
        hc -= 1
        wc -= angelcol // 30
        pivot = (wc, hc )
    if motion[2] == 1:
        hc += 1
        wc += angelcol // 30
        pivot = (wc, hc )
    if motion[7] == 1:
        angelcol = angelcol - 1
    if motion[8] == 1:
        angelcol = angelcol + 1

    screen.fill((69,69,69))
    px = wd / 800
    pygame.draw.polygon(screen,(48,51,69),[(350*px//2,0),(350*px//2,110*px//2),(330*px//2,110*px//2) , (330*px//2,130*px//2) , (0,130*px//2) , (0,0)])
    pygame.draw.ellipse(screen, (48,51,69),(330*px//2 - (130*px//2 - 110*px//2) ,110*px//2 - (130*px//2 - 110*px//2) ,(130*px//2 - 110*px//2) * 2  , (130*px//2 - 110*px//2) * 2))
    pygame.draw.polygon(screen,(108,130,135),[(340*px//2,10*px//2),(340*px//2,40*px//2),(320*px//2,40*px//2) , (320*px//2,60*px//2) , (10*px//2,60*px//2) , (10*px//2,10*px//2)])
    pygame.draw.ellipse(screen, (108,130,135), (320*px//2 - (60*px//2 - 40*px//2) ,40*px//2 - (60*px//2 - 40*px//2) ,(60*px//2 - 40*px//2) * 2  , (60*px//2 - 40*px//2) * 2))
    pygame.draw.polygon(screen,(108,130,135),[(340*px//2,70*px//2),(340*px//2,100*px//2),(320*px//2,100*px//2) , (320*px//2,120*px//2) , (10*px//2,120*px//2) , (10*px//2,70*px//2)])
    pygame.draw.ellipse(screen, (108,130,135), (320*px//2 - (120*px//2 - 100*px//2) ,100*px//2 - (120*px//2 - 100*px//2) ,(60*px//2 - 40*px//2) * 2  , (60*px//2 - 40*px//2) * 2))
    pygame.draw.polygon(screen,(255,255,255),[(350*px//2,hd),(350*px//2,hd-(100*px//2)),(330*px//2,hd-(100*px//2)),(330*px//2,hd-(120*px//2)),(0,hd-(120*px//2)),(0,hd)])
    pygame.draw.ellipse(screen, (255,255,255), (330*px//2 - (120*px//2 - 100*px//2) ,hd-(120*px//2),(120*px//2 - 100*px//2) * 2  , (120*px//2 - 100*px//2) * 2))
    
    #рисование дуги 
    #pygame.draw.line(screen,(255,0,0),(hd//2-wfur*2,minY//k+hc+hpric-hpricsed),(hd//2+wfur*2,minY//k+hc+hpric-hpricsed),4)
    #pi = 3.14
    #pygame.draw.arc(screen, (255,0,0), (wc - hfur // 2, hc - hfur // 2, hfur, hfur), math.radians(90 + angle)  , 1.5*pi, 3)
    
    #отрисовка колёс
    if ( angelcol > 0 ):
        imagecol1 = rotate(imageccol1, center_imagecol , angle + angelcol // 1.5)
        imagecol2 = rotate(imageccol2, center_imagecol , angle + angelcol)
    else:
        imagecol1 = rotate(imageccol1, center_imagecol , angle + angelcol)
        imagecol2 = rotate(imageccol2, center_imagecol , angle + angelcol//1.5)
    pivotcol1 = (int(wc - math.sin(math.radians(angle)) * hcolofsed +math.cos(math.radians(angle)) * ( wfur * 0.45 ) ) , int(hc - math.cos(math.radians(angle)) * hcolofsed - math.sin(math.radians(angle)) * ( wfur * 0.45 ))   )
    pivotcol2 = (int(wc - math.sin(math.radians(angle)) * hcolofsed - math.cos(math.radians(angle)) * ( wfur * 0.45 )) , int(hc - math.cos(math.radians(angle)) * hcolofsed + math.sin(math.radians(angle)) * ( wfur * 0.45 ))  )
    rectcol1 = imagecol1.get_rect()
    rectcol2 = imagecol2.get_rect()
    rectcol1.center = pivotcol1
    rectcol2.center = pivotcol2
    screen.blit(imagecol1, rectcol1)
    screen.blit(imagecol2, rectcol2)

    #отрисовка фуры
    image = rotate(imagec, center_image , angle)
    rect = image.get_rect()
    rect.center = pivot
    screen.blit(image, rect)

    #трисовка прицепа
    #screen.blit(imagepric, rectc)

    # вывод информации о градусах
    font = pygame.font.SysFont('arial', int((30 * px)//2))
    text = font.render("Угол складывания " + str(math.fabs(angle))+'°', 2, (0, 0, 0))
    place = text.get_rect(topleft=(20*px//2,20*px//2))       
    screen.blit(text, place)
    textAngelCol = font.render("Поворот колёс " + str(math.fabs(angelcol))+'°', 2, (0, 0, 0))
    placeAngelCol = text.get_rect(topleft=(20*px//2,80*px//2))
    screen.blit(textAngelCol, placeAngelCol)
    fontLogo = pygame.font.SysFont('arial', int((90 * px)//2))
    textLogo = fontLogo.render("ABTOC", 2, (255, 0, 0))
    placeLogo = text.get_rect(topleft=(20*px//2,hd-(120*px//2)))
    screen.blit(textLogo, placeLogo)
    textLen = font.render(str(int(minY))+" мм", 2, (255, 255, 255))
    placeLen = text.get_rect(topleft=(hd//2-wfur*2,minY//k+hc+hpric-hpricsed+5))
    screen.blit(textLen, placeLen)
    pygame.display.update()
 
pygame.quit()