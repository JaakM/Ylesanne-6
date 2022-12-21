
import pygame  #impordin pygame mooduli ja random mooduli
import sys   #impordin sys mooduli
pygame.init()   #käivitan pygame mooduli

# värvid
lBlue = [176, 244, 250]   #omastan muutujale "lblue" RGB väärtuse 150, 204, 255.
black = [0, 0, 0]

#ekraan
screenX = 640   # määran ekraani x-telje suuruseks 640px (akna kõrgus)
screenY = 480   # määran ekraani y-telje suuruseks 480px (akna laius)
screen = pygame.display.set_mode([screenX, screenY])   #omastan muutujale "screen" väärtused (muutujad screenX, screenY)
pygame.display.set_caption("Ülesanne 6 - Jaak Mõttus")   #lisan mängu päisesse ülesande numbri ja enda nime
screen.fill(lBlue)  #täidan ekraani helesinise värviga, RGB 150, 284, 255
clock = pygame.time.Clock()   #omastan muutujale "clock" kella

posX, posY = 0, 0   #muutuja "posX" algkordinaat on 0 ja muutuja "posY" algkordinaat on 0
alusX, alusY = 200, screenY/1.5   #muutuja alusX algkordinaat on 200 ja
#muutuja alusY kordinaat on Y-tleje maksimum väärtus jagatud 1.5 ehk 320
speedX, speedY = 4, 5   #X-teljeline kiirus on 3 ja Y teljeline kiirus on 4
score = 0   #omastan muutujale "score" väärtuse 0
liikumise_suund = 0   #omastan muutujale "liikumise_suund väärtuse 0

#tausta muusika
pygame.mixer.music.load("taust3.wav")   #laadin muusika
pygame.mixer.music.play(1)  #panen eelnevalt laaditud muusika mängima, 0 tähendab, et lugu hakkab korduma
pygame.mixer.music.set_volume(0.2)   #muudan helitugevust 80% peale


while True:   #panen whlie loppi käima ehk ekraani uuendama
    clock.tick(60)    # ekraani uuendatakse 60 korda sekundis

    # mängu sulgemine ristist
    sisend = pygame.event.poll()
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:   #kui sisendi tüüp on võrdne pygame quitiga
            sys.exit()   #siis mängust väljutakse

    # heliefektid
    pygame.mixer.music.set_volume(0.2)   #muudan helitugevust 80% peale
    porge = pygame.mixer.Sound("porge.ogg")
    aluselt_porge = pygame.mixer.Sound("porge.ogg")
    game_over = pygame.mixer.Sound("felldown.wav")


    #alus
    alusepilt = pygame.image.load("pad.png")   #laadin pad.png pildi ja omastan selle muutujale "alusepilt"
    alusepilt = pygame.transform.scale(alusepilt, [120, 20])  #muudan muutuja "alusepilt" suuruseks 120*20px
    alus = pygame.Rect(alusX, alusY, 120, 20)  #tekitan meetodi "rect" abil ristküliku, asukoht alusx, alusY, suurus 120*20px
    screen.blit(alusepilt, alus)  # panen blit-ga ekraanile alusepildi aluse peale

    # pall
    pallipilt = pygame.image.load("ball.png")   #omastan muutujale "pallipilt" png faili ball, mille laadin pygame.image.load abil
    pall = pygame.Rect(posX, posY, 20, 20)   #omastan muutujale "pall" Rect meetodi abil loodud ristküliku asukohaga posX, posy ja suurusega 20*20px,
    screen.blit(pallipilt, pall)   #kuvan blit abil ekraanile muutuja "pall" peale muutuja "pallipilt"

    # palli liikumine
    posX += speedX   # muutuja posX väärtus suureneb muutuja speedX võrra
    posY += speedY   # muutuja posY väärtus suureneb muutuja speedY võrra

    if posX > screenX - pallipilt.get_rect().width or posX < 0:  #kui muutuja posX on suurem kui ekraani x-telje
        # maksimaalne väärtus või kui muutuja posX on väiksem kui null (sisuliselt, kui posX on vahemikus 1 kuni 619)
        speedX = -speedX   #siis muutuja "speedX" muutub negatiivseks (pall põrkab seinast).
        pygame.mixer.Sound.play(porge)   #siis, kui pall seinaga kokku puutub, mängitakse seda heli faili "porge".

    if posY < 0:  #kui palli y kordinaat on väiksem kui 0,
        speedY = -speedY   #siis pall põrkab
        pygame.mixer.Sound.play(porge) #mängitakse heli faili "porge"

    # palli põrkamine aluse pealt
    if pall.colliderect(alus) and posY > 0:   #kui pall puutub kokku alusega ja posY on suurem kui 0
        speedY = -speedY   #siis speedY muutub negatiivseks ehk pall põrkab
        score += 1   #ja score suureneb 1 võrra
        pygame.mixer.Sound.play(aluselt_porge)   #mängitakse heli faili "aluselt_põrge"

    if pall.colliderect(alus) and speedY > 0.5:   #kui pall puutub kokku alusega ja speedY on suurem kui 0.5
        speedY = -speedY   #siis speedY muutub negatiivseks ehk pall põrkab
        score -= 1   #ja score väheneb 1 võrra


    #nooltega aluse juhtimine x-teljel
    if sisend.type == pygame.KEYDOWN:   #kui mängija vajutab klavhi alla
        if sisend.key == pygame.K_RIGHT:   #kui mängija vajutab nool paremale klahvi
            liikumise_suund = "paremale"   #siis omastakse liikumise_suunale "paremale" väärtus
        elif sisend.key == pygame.K_LEFT:   #kui mängija vajutab nool vasakule klahvi
             liikumise_suund = "vasakule"   #siis omastatakse liikumise_suunale "vasakule" väärtus

    if sisend.type == pygame.KEYUP:   #kui mängija tõstab klahvi ülesse
        if sisend.key == pygame.K_RIGHT:  #kui lahti lastud klahv on parem
            liikumise_suund = 0   #siis liikumine on 0 ehk seisab paigal
        elif sisend.key == pygame.K_LEFT:   #kui lahti lastud klahv on vasak
            liikumise_suund = 0   #siis liikumine on 0 ehk seisab paigal

    if liikumise_suund == "vasakule":   #kui liikumise_suund võrdub vasakule
        if alusX > 0:   #ja aluse x kordinaat on suurem kui 0
            alusX -= 10   #siis aluse x kordinaat väheneb 10px võrra iga ekraani uuendusega (iga loopiga)
    if liikumise_suund == "paremale":   #kui liikumise:suund võrdub paremale
        if alusX +120 < screenX:   #ja kui aluse x kordinaat + 120px on väiksem kui ekraani maks x kordinaat
             alusX += 10   #siis aluse x kordinaat suureneb 10 px võrra iga ekraani uuendusega

    if posY == 440:   #kui pall y kordinaat on 440
        pygame.mixer.Sound.play(game_over)   #mängi heli "game_over"

    if posY == screenY:   #kui pall puutub alumist äärt
        sys.exit()   #siis mäng lõpetatakse

    # Teksti seaded ja skoori kuvamine
    game_font = pygame.font.Font("freesansbold.ttf", 24)   #omastan muutujale game_font fondi freesansbold suuruega 24px
    text = game_font.render("SKOOR: " + str(score), True, black)  #omastan muutujale text sõna SKOOR, millele liidan
    # striimina score väärtuse ja see kõik on musta värvi
    screen.blit(text, (20,20))   #kuvan blit abil sreen peale texti, asukoht 20px x-telg ja 20px y telg

    pygame.display.flip()   #kuvab kõik, mis sellele eelneb ehk ekraani värskendamine
    screen.fill(lBlue)   #täidan ekraani eelnevalt muutujale "lBlue" omistatud värviga
    # see vajalik, et peale palli liikumist ei jääks näha kollane teekond ehk palli pildid eelmistest kaadritest


