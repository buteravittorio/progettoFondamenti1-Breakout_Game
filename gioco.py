import pygame
import random
import sys

# Inizializzazione globale
pygame.init()

# Costanti di gioco
LARGHEZZA, ALTEZZA = 800, 600
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)
ARANCIONE = (255, 126, 0)
GIALLO = (255, 255, 0)

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Breakout Game - Progetto Fondamenti")

# Caricamento Asset (con gestione errori)
def carica_immagine(nome, dimensioni=None):
    try:
        img = pygame.image.load(nome).convert_alpha()
        if dimensioni:
            img = pygame.transform.scale(img, dimensioni)
        return img
    except:
        # Se l'immagine manca, crea un rettangolo colorato di backup
        surf = pygame.Surface(dimensioni if dimensioni else (50, 50))
        surf.fill((100, 100, 100))
        return surf

# Funzioni Schermate
def menu():
    sfondo_menu = carica_immagine("1.1.png", (LARGHEZZA, ALTEZZA))
    font_titolo = pygame.font.Font(None, 80)
    font_testo = pygame.font.Font(None, 50)

    while True:
        schermo.blit(sfondo_menu, (0, 0))
        btn_gioca = font_titolo.render("GIOCA!", True, BIANCO)
        btn_esci = font_testo.render("ESCI", True, BIANCO)
        
        rect_gioca = schermo.blit(btn_gioca, (300, 260))
        rect_esci = schermo.blit(btn_esci, (360, 500))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_gioca.collidepoint(event.pos):
                    gioco()
                if rect_esci.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def punteggio(punti):
    sfondo = carica_immagine("1.1.png", (LARGHEZZA, ALTEZZA))
    font_m = pygame.font.Font(None, 40)
    font_l = pygame.font.Font(None, 60)
    
    colore_punti = ROSSO if punti < 50 else VERDE
    testo_punti = font_l.render(f"{punti}/100", True, colore_punti)
    testo_label = font_m.render("IL TUO PUNTEGGIO E':", True, BIANCO)
    testo_cont = font_m.render("CLICCA PER CONTINUARE", True, GIALLO)

    while True:
        schermo.blit(sfondo, (0, 0))
        schermo.blit(testo_label, (230, 220))
        schermo.blit(testo_punti, (350, 280))
        schermo.blit(testo_cont, (230, 500))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

def vittoria(punti):
    sfondo = carica_immagine("1.1.png", (LARGHEZZA, ALTEZZA))
    font = pygame.font.Font(None, 70)
    testo = font.render("HAI VINTO!!!", True, VERDE)
    
    while True:
        schermo.blit(sfondo, (0, 0))
        schermo.blit(testo, (250, 260))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                return

# Funzione Principale di Gioco
def gioco():
    clock = pygame.time.Clock()
    
    # Paddle
    larg_paddle, alt_paddle = 120, 15
    x_paddle = (LARGHEZZA - larg_paddle) // 2
    y_paddle = 550
    paddle_img = carica_immagine("2.jpg", (larg_paddle, alt_paddle))

    # Palla
    raggio = 8
    x_palla, y_palla = LARGHEZZA // 2, y_paddle - 20
    sp_x, sp_y = 5, -5
    palla_img = carica_immagine("3.png", (raggio*2, raggio*2))

    # Sfondo
    sfondo_img = carica_immagine("1.jpg", (LARGHEZZA, ALTEZZA))

    # Blocchi
    blocchi = []
    colori_righe = [ROSSO, ARANCIONE, GIALLO, BIANCO, VERDE]
    for riga in range(5):
        for col in range(10):
            rect = pygame.Rect(col * 80 + 2, riga * 25 + 50, 76, 20)
            blocchi.append({'rect': rect, 'colore': colori_righe[riga]})

    punti = 0
    pausa = False

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_p:
                    pausa = not pausa

        if not pausa:
            # Movimento Paddle
            tasti = pygame.key.get_pressed()
            if tasti[pygame.K_LEFT] and x_paddle > 0:
                x_paddle -= 8
            if tasti[pygame.K_RIGHT] and x_paddle < LARGHEZZA - larg_paddle:
                x_paddle += 8

            # Movimento Palla
            x_palla += sp_x
            y_palla += sp_y

            # Collisioni Muri
            if x_palla <= 0 or x_palla >= LARGHEZZA - raggio*2:
                sp_x *= -1
            if y_palla <= 0:
                sp_y *= -1
            
            # Game Over
            if y_palla > ALTEZZA:
                punteggio(punti)
                return

            # Collisione Paddle
            paddle_rect = pygame.Rect(x_paddle, y_paddle, larg_paddle, alt_paddle)
            palla_rect = pygame.Rect(x_palla, y_palla, raggio*2, raggio*2)

            if palla_rect.colliderect(paddle_rect):
                # Calcola rimbalzo basato su dove tocca il paddle
                centro_paddle = x_paddle + larg_paddle / 2
                distanza_dal_centro = (x_palla + raggio) - centro_paddle
                sp_x = distanza_dal_centro / (larg_paddle / 8) # Angolazione variabile
                sp_y = -abs(sp_y) # Sempre verso l'alto

            # Collisione Blocchi
            
            for b in blocchi[:]:
                if palla_rect.colliderect(b['rect']):
                    sp_y *= -1
                    blocchi.remove(b)
                    punti += 1
                    break 

            if not blocchi or punti >= 100:
                vittoria(punti)
                return

        # Disegno
        schermo.blit(sfondo_img, (0, 0))
        schermo.blit(paddle_img, (x_paddle, y_paddle))
        schermo.blit(palla_img, (int(x_palla), int(y_palla)))
        
        for b in blocchi:
            pygame.draw.rect(schermo, b['colore'], b['rect'])

        if pausa:
            font_p = pygame.font.Font(None, 100)
            testo_p = font_p.render("PAUSA", True, GIALLO)
            schermo.blit(testo_p, (250, 250))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    menu()