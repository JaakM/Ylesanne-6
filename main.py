import pygame, random   #impordin pygame mooduli ja random mooduli
pygame.init()   #käivitan pygame mooduli

# värvid
lBlue = [150, 204, 255]   #omastan muutujale "lblue" RGB väärtuse 150, 204, 255.
black = [0, 0, 0]
# ekraani seaded
screenX = 640   # määran ekraani x-telje suuruseks 640px
screenY = 480   # määran ekraani y-telje suuruseks 480px
screen = pygame.display.set_mode([screenX, screenY])   # omastan muutujale "screen" väärtused (väärtusteks on muutujad screenX ja screenY)
pygame.display.set_caption("Ülesanne 6 - Jaak Mõttus")   # lisan mängu päisesse ülesande numbri ja enda nime
#screen.fill(lBlue)  #täidan ekraani helesinise värviga, RGB 150, 284, 255
clock = pygame.time.Clock()   #omastan muutujale "clock" kella
posX, posY = 0, 0   # muutuja "posX" algkordinaat on 0 ja muutuja "posY" algkordinaat on 0.
speedX, speedY = 3, 4   #X-teljeline kiirus on 3 ja Y teljeline kiirus on 4
speedT = 5
score = 0   #NB!!!!!! "score = 0" peab olema kindlasti ennem while funktsiooni !!
padMovingDirection = 0
padSpeed = 7


gameover = False
while not gameover:   # kuni mäng ei ole läbi
    clock.tick(60)    # uuendatakse ekraani 60 korda sekundis

    # mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # pall ja palli liikumine
    pallipilt = pygame.image.load("ball.png")   #omastan muutujale "pallipilt" png faili ball, mille laadin pygame.image.load abil
    pall = pygame.Rect(posX, posY, 20, 20)   #omastan muutujale pall Rect funktsiooni, kusjuures Rect asukoht on märgitud muutujate posX ja posY abil (antud juhul on on x=0 ja y=0, sest skripti alguses sai sellised väärtused muutujatele posx ja posy omistatud), objekti Rect suurus on 20px korda 20px.
    screen.blit(pallipilt, pall)   #kuvame screen.blit abil rectile, milleks on muutuja "pall", palli pildi "pallImage"

    posX += speedX   # muutuja posX väärtus suureneb muutuja speedX võrra
    posY += speedY   # muutuja posY väärtus suureneb muutuja speedY võrra

    alusX = 200  # SIIA PANE HIIREGA LIIGUTAMINE
    alusY = screenY / 1.5

    alusepilt = pygame.image.load("pad.png")
    alus = pygame.Rect(alusX, alusY, 120, 20)
    screen.blit(alusepilt, alus)



    if posX > screenX - pallipilt.get_rect().width or posX < 0:  #kui muutuja posX on suurem kui ekraani x-telje maksimaalne väärtus või kui muutuja posX on võiksem kui null (sisuliselt, kui posX on vahemikus 0 kuni 640)
        speedX = -speedX   #siis muutuja "speedX" muutub negatiivseks (pall põrkab seinast). See tähendab, et muutuja "speedX" saab rahulikult speedX eelnevalt omistatud väärtuse võrra suureneda, kuni if lauses kirjeldatu saavutatakse (muutuja "posX" läheb suuremaks kui 640 või väiksemaks kui 0).

    #if posY > screenY - pallipilt.get_rect().height or posY < 0:   # NB! pane siin 1.5 asemele aluse aadress? Kuidas x-telge määrata aluselt põrkamisel?
     #   speedY = -speedY

    if posY < 0:  #kui palli y kordinaat on väiksem kui 0, siis kiirus läheb negatiivsseks ehk pall põrkab
        speedY = -speedY   #pall põrkab





    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
                Gameover = True
                exit()

    if sisend.type == pygame.KEYDOWN:
        if sisend.key == pygame.K.RIGHT:
            padMovingDirection = "Parem"
        elif sisend.key == pygame.K.LEFT:
            padMovingDirection = "Vasak"

    if sisend.type == pygame.KEYUP:
        if sisend.key == pygame.K.RIGHT:
            padMovingDirection = 0
        elif sisend.key == pygame.K.LEFT:
            padMovingDirection = 0

    #if pall.colliderect(alus) and speedY > 0:
    #   speedY = -speedY


    if padMovingDirection == "Parem":
        if padX + alusepilt.get_rect().widht < scrennX:
            padX += padSpeed
    elif padMovingDirection == "Vasak":
        if padX > 0:
            padX -= padSpeed





    '''if posY == alusX and alusY:
        speedY = -speedY'''



    '''score = 0
    if posY == screenY/1.5:  # see number (antud juhl screnYja 1.5 jagatis) peab lema põrkelaua Y-teljeline asukoht (kui muutuja posY on võrdne põrkelaua Y kordinaadiga, siis juhtub järgmisel real olev
        score += 1
        SKOOR = int(score)
        print(str(SKOOR))'''

        #def score(score):
        #font = pygame.font.Font(pygame.font.match_font('Daytona'), 30)
        #text = font.render("SKOOR: " + str(score), True, [0,0,0])
        #screen.blit(text, [0, 0])   #kuvame ekraanile muutuja "text" ja kuvamise asukohaks on x=opx ja y=o px e

    '''score = 0
    if posY == 320:
            score += 1'''

    '''score('text')'''
    '''score = 0
    k = pygame.image.load("ball.png")
    if posY == 320:
        score += 1
        screen.blit(str(score), (30, 0))'''

    #score
    '''score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 28)
    textX = 10
    textY = 10
    if posY == 310:
        score_value = score_value + 1
    def show_score(x, y):
        score = font.render("SKOOR: " + str(score_value), True, (0, 0, 0))
        screen.blit(score, (x, y))
    if posY == 310:
        score_value = score_value + 1
    show_score(textX, textY)'''


# text variables
    #score = 0
    game_font = pygame.font.Font("freesansbold.ttf", 24)

    text = game_font.render("SKOOR: " + f"{score}", True, black)  #  str() asemel on kasutatud f{} ja toimib .
    screen.blit(text, (20,20))

    if posY >= screenY-19:
        score += 1

    print(score)   # see peab olema lõpus, aga ennem flippimist

    pygame.display.flip()   #kuvab kõik, mis sellele eelneb
    screen.fill(lBlue)   #täidan ekraani helesinise värviga, RGB 150, 284, 255, et peale palli liikumist ei jääks näha kollane teekon ehk vanad palli pildid.

pygame.quit()