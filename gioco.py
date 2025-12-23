import pygame
import random
def menu():
    pygame.init()
    finestra = pygame.display.set_mode((800, 600))
    sfondo = pygame.image.load("1.1.png").convert()
    finestra.blit(sfondo, (0, 0))
    
    gioca = pygame.font.Font(None, 80).render("GIOCA!", True, (255, 255, 255))
    esci = pygame.font.Font(None, 50).render("ESCI", True, (255, 255, 255))
    finestra.blit(gioca, (300, 260))
    finestra.blit(esci, (360, 500))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 280 < x < 500 and 250 < y < 310:
                    gioco()
                elif 360 < x < 440 and 500 < y < 530:
                    pygame.quit()


def punteggio(punti):
    pygame.init()
    finestra = pygame.display.set_mode((800, 600))
    sfondo = pygame.image.load("1.1.png").convert()
    finestra.blit(sfondo, (0, 0))
    x = str(punti)+'/100'
    y = "IL TUO PUNTEGGO  E' DI:"
    punteggio = pygame.font.Font(None, 40).render(y, True, (200, 200, 200))
    if punti < 20:
        punteggio1 = pygame.font.Font(None, 60).render(x, True, (255,0,0))
    if punti in range(20,40):
        punteggio1 = pygame.font.Font(None, 60).render(x, True, (255,126,0))
    if punti in range(40,60):
        punteggio1 = pygame.font.Font(None, 60).render(x, True, (255,255,0)) 
    if punti in range(60,80):
        punteggio1 = pygame.font.Font(None, 60).render(x, True, (255,255,255))
    if punti in range(80,101):
        punteggio1 = pygame.font.Font(None, 60).render(x, True, (0,255,0))

    continua = pygame.font.Font(None, 30).render("CONTINUA", True, (255, 255, 255))
    finestra.blit(punteggio, (230, 260))
    finestra.blit(punteggio1, (350, 300))
    finestra.blit(continua, (350, 500))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 < x < 470 and 500 < y < 530:
                    menu()


def vittoria(punti):
    pygame.init()
    finestra = pygame.display.set_mode((800, 600))
    sfondo = pygame.image.load("1.1.png").convert()
    finestra.blit(sfondo, (0, 0))
    x = str(punti)+'/100'
    y = "HAI VINTO!!!"
    vittoria = pygame.font.Font(None, 60).render(y, True, (0,255,0))
    punteggio1 = pygame.font.Font(None, 60).render(x, True, (0,255,0))
    continua = pygame.font.Font(None, 30).render("CONTINUA", True, (255, 255, 255))
    finestra.blit(vittoria, (280, 260))
    finestra.blit(punteggio1, (330, 300))
    finestra.blit(continua, (350, 500))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 < x < 470 and 500 < y < 530:
                    menu()


def gioco():   
    pygame.init()
    schermo = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Breakout")

    #variabili di gioco
    pausa = False
    gioco_finito = False
    
    #spostamento della palla
    spostamento_x = -.6
    spostamento_y = .6
    #dimensioni della pallina
    raggio = 10
    #dimensioni del blocco
    larghezza_blocco = 78
    altezza_blocco = 20
    #dimensioni del paddle
    larghezza_paddle = 100
    altezza_paddle = 10
    #coordinate del paddle
    x_paddle = 580
    y_paddle = 580
    #coordinate della palla
    x_palla = x_paddle
    y_palla = 560

    #lista dei blocchi
    numero_blocchi = 10
    blocchi = []
    l=0
    y = 40
    while l < 10:  
        for i in range(numero_blocchi):
            x = i * (larghezza_blocco + 2) + 1
            blocchi.append(pygame.Rect(x, y, larghezza_blocco, altezza_blocco))
        y += 25
        l +=1 

    def disegna_blocchi(blocchi):
        BIANCO = (255,255,255)
        ARANCIONE = (255,126,0)
        ROSSO = (255,0,0)
        GIALLO = (255,255,0)
        VERDE = (0,255,0)
        for blocco in blocchi:  
            if blocchi.index(blocco) in range(20):
                pygame.draw.rect(schermo, VERDE, blocco)
            if blocchi.index(blocco) in range(20,40):
                pygame.draw.rect(schermo, BIANCO, blocco)
            if blocchi.index(blocco) in range(40,60):
                pygame.draw.rect(schermo, GIALLO, blocco)
            if blocchi.index(blocco) in range(60,80):
                pygame.draw.rect(schermo, ARANCIONE, blocco)
            if blocchi.index(blocco) in range(80,100):
                pygame.draw.rect(schermo, ROSSO, blocco)


    #caricare le immagini
    immagine_palla = pygame.image.load('3.png')
    immagine_paddle = pygame.image.load('2.jpg')
    immagine_sfondo = pygame.image.load('1.jpg')
    
    punti = 0
    
    #game loop
    while not gioco_finito:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gioco_finito = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausa = not pausa

        #spostare il paddle con la freccie
        tasti = pygame.key.get_pressed()
        if tasti[pygame.K_RIGHT]:
            x_paddle = min(x_paddle + 3, 800 - larghezza_paddle)
        if tasti[pygame.K_LEFT]:
            x_paddle = max(x_paddle - 3, 0)

        #spostare il paddle
        if not pausa:
            x_palla += spostamento_x
            y_palla += spostamento_y

        #verificare se la palla colpisce il paddle
        if y_palla + raggio > y_paddle and x_palla + raggio > x_paddle and x_palla - raggio < x_paddle + larghezza_paddle:
            if x_palla + raggio < x_paddle + int(larghezza_paddle/5):
                spostamento_y = -1
                spostamento_x = -1
            if x_palla + raggio > x_paddle + int(larghezza_paddle-20):
                spostamento_y = -1
                spostamento_x = +1
            if x_palla + raggio in range(x_paddle + int(larghezza_paddle/5),x_paddle+larghezza_paddle-60):
                spostamento_y = -2
                spostamento_x = -.5
            if x_palla + raggio in range(x_paddle + larghezza_paddle-40,x_paddle+larghezza_paddle-20):
                spostamento_y = -2
                spostamento_x = +1
            if x_palla + raggio in range(x_paddle + larghezza_paddle-60,x_paddle+larghezza_paddle-40):
                spostamento_y = -1
                spostamento_x = 0

        #verificare se la palla colpisce un blocco
        for blocco in blocchi:
            if y_palla - raggio < blocco.bottom and x_palla + raggio > blocco.left and x_palla - raggio < blocco.right:
                spostamento_y = -spostamento_y
                blocchi.remove(blocco)
                punti += 1

        #verificare se la palla colpisce un muro
        if x_palla + raggio > 800 or x_palla - raggio < 0:
            spostamento_x = -spostamento_x
        if y_palla - raggio < 0:
            spostamento_y = 1
        if y_palla + raggio > 600:
            gioco_finito = True
        
     
        #disegnare lo sfondo
        schermo.blit(immagine_sfondo, (0, 0))
        #disegnare la pallina
        schermo.blit(immagine_palla, (x_palla - raggio, y_palla - raggio))
        #disegnare il paddle
        schermo.blit(immagine_paddle, (x_paddle, y_paddle))
        #disegnare i blocchi
        disegna_blocchi(blocchi)
        #aggiornare lo schermo
        pygame.display.flip()

        
        #uscita con pnteggio massimo 
        if punti == 100:   
            gioco_finito = True
            vittoria(punti)
    #uscita dal gioco dopo aver fatto cadere la pallina
    t=True
    while t:
        for event in pygame.event.get():
            punteggio(punti)

menu()
