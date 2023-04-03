import pygame
from pygame.locals import *
from random import *

def affich() :
    if ecran == 1 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,700,650))
        myfont = pygame.font.SysFont("Fixedsys",40)
        texte = myfont.render("Choisissez un mode de jeu :",False,(0,0,0))
        fenetre.blit(texte,(150,80))
        pygame.draw.rect(fenetre,(0,0,0),(145,195,410,90))
        pygame.draw.rect(fenetre,(255,255,255),(150,200,400,80))
        texte = myfont.render("Joueur contre joueur",False,(0,0,0))
        fenetre.blit(texte,(200,225))
        pygame.draw.rect(fenetre,(0,0,0),(145,395,410,90))
        pygame.draw.rect(fenetre,(255,255,255),(150,400,400,80))
        texte = myfont.render("Joueur contre IA",False,(0,0,0))
        fenetre.blit(texte,(225,425))
    elif ecran == 2 :
        pygame.draw.rect(fenetre,(0,0,160),(0,0,700,650))
        pygame.draw.rect(fenetre,(125,125,125),(0,0,700,50))
        myfont = pygame.font.SysFont("Fixedsys",40)
        if mode == 1 :
            texte = myfont.render("Joueur 1 :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.circle(fenetre,(237,28,36),(175,25),15)
            texte = myfont.render("Joueur 2 :",False,(0,0,0))
            fenetre.blit(texte,(510,10))
        elif mode == 21 :
            texte = myfont.render("Joueur :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.circle(fenetre,(237,28,36),(155,25),15)
            texte = myfont.render("IA :",False,(0,0,0))
            fenetre.blit(texte,(600,10))
        elif mode == 22 :
            texte = myfont.render("IA :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.circle(fenetre,(237,28,36),(85,25),15)
            texte = myfont.render("Joueur :",False,(0,0,0))
            fenetre.blit(texte,(530,10))
        pygame.draw.circle(fenetre,(255,208,47),(675,25),15)
        for i in range (7) :
            for j in range (6) :
                if plat[i][j] == "x" :
                    pygame.draw.circle(fenetre,(237,28,36),(i*100+50,j*100+100),40)
                elif plat[i][j] == "o" :
                    pygame.draw.circle(fenetre,(255,208,47),(i*100+50,j*100+100),40)
                else :
                    pygame.draw.circle(fenetre,(255,255,255),(i*100+50,j*100+100),40)

    elif ecran == 3 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,700,650))
        myfont = pygame.font.SysFont("Fixedsys",40)
        texte = myfont.render(gagne,False,(0,0,0))
        fenetre.blit(texte,(350-(len(gagne)//2)*15,310))

    pygame.display.flip()

def tour_ia() :
    global plat
    global plat2
    global j
    non = 0
    if j == 1 :
        a = "x"
    else :
        a = "o"
    for i in range (7) :
        if plat[i][0] == "-" :
            p = 0
            while p < 6 and plat[i][p] == "-" :
                p += 1
            plat2 = list(plat)
            plat2[i][p-1] = a
            if test(a) == 1 :
                non = 1
                plat[i][p-1] = a
                memp = [i,p]
                break
            else :
                plat[i][p-1] = "-"
    if non == 0 :
        if j == 1 :
            b = "o"
        else :
            b = "x"
        for i in range (7) :
            if plat[i][0] == "-" :
                p = 0
                while p < 6 and plat[i][p] == "-" :
                    p += 1
                plat2 = list(plat)
                plat2[i][p-1] = b
                if test(b) == 1 :
                    non = 1
                    plat[i][p-1] = a
                    memp = [i,p]
                    break
                else :
                    plat[i][p-1] = "-"
    if non == 0 :
        for i in range (7) :
            if plat[i][0] == "-" :
                p = 0
                while p < 6 and plat[i][p] == "-" :
                    p += 1
                plat3 = list(plat)
                plat3[i][p-1] = b
                total = 0
                for k in range (7) :
                    for l in range (6) :
                        if plat3[k][l] == "-" and i*6+p != k*6+l :
                            plat2 = list(plat3)
                            plat2[k][l] = b
                            if test(b) == 1 :
                                total += 1
                            plat[k][l] = "-"
                            plat3[k][l] = "-"
                if total >= 2 :
                    non = 1
                    plat[i][p-1] = a
                    memp = [i,p]
                    break
                else :
                    plat[i][p-1] = "-"
        if non == 1 :
            plat2 = list(plat)
            if test(b) == 1 :
                non = 0
                plat[memp[0]][memp[1]-1] = "-"
    if non == 0 :
        for i in range (7) :
            if plat[i][0] == "-" :
                p = 0
                while p < 6 and plat[i][p] == "-" :
                    p += 1
                plat3 = list(plat)
                plat3[i][p-1] = a
                total = 0
                for k in range (7) :
                    for l in range (6) :
                        if plat3[k][l] == "-" and i*6+p != k*6+l :
                            plat2 = list(plat3)
                            plat2[k][l] = a
                            if test(a) == 1 :
                                total += 1
                            plat[k][l] = "-"
                            plat3[k][l] = "-"
                if total >= 2 :
                    non = 1
                    plat[i][p-1] = a
                    memp = [i,p]
                    break
                else :
                    plat[i][p-1] = "-"
        if non == 1 :
            plat2 = list(plat)
            if test(b) == 1 :
                non = 0
                plat[memp[0]][memp[1]-1] = "-"

    if non == 0 :
        c = randint(0,6)
        t = [0,0,0,0,0,0,0]
        t[c] = 1
        while non == 0 :
            while not plat[c][0] == "-" :
                c = randint(0,6)
            p = 0
            while p < 6 and plat[c][p] == "-" :
                p += 1
            t[c] = 1
            plat[c][p-1] = a
            non = 1
            plat2 = list(plat)
            if test(b) == 1 and not t == [0,0,0,0,0,0,0] :
                non = 0
                plat[c][p-1] = "-"
    if j == 1 :
        j = 2
    else :
        j = 1

    affich()

def test(a) :
    non = 0
    for i in range (4) :
        for j in range (6) :
            if plat2[i][j] == plat2[i+1][j] == plat2[i+2][j] == plat2[i+3][j] == a :
                non = 1
    if non == 0 :
        for i in range (3) :
            for j in range (7) :
                if plat2[j][i] == plat2[j][i+1] == plat2[j][i+2] == plat2[j][i+3] == a :
                    non = 1
    if non == 0 :
        for i in range (4) :
            for j in range (3) :
                if plat2[i][j] == plat2[i+1][j+1] == plat2[i+2][j+2] == plat2[i+3][j+3] == a :
                    non = 1
    if non == 0 :
        for i in range (4) :
            for j in range (5,2,-1) :
                if plat2[i][j] == plat2[i+1][j-1] == plat2[i+2][j-2] == plat2[i+3][j-3] == a :
                    non = 1
    return non

def fin_partie() :
    global ecran
    global plat2
    global gagne
    plat2 = list(plat)
    if test("x") == 1 :
        ecran = 3
        if mode == 1 :
            gagne = "Le joueur 1 a gagné !"
        elif mode == 21 :
            gagne = "Vous avez gagné !"
        elif mode == 22 :
            gagne = "L'IA a gagné !"
    elif test("o") == 1 :
        ecran = 3
        if mode == 1 :
            gagne = "Le joueur 2 a gagné !"
        elif mode == 21 :
            gagne = "L'IA a gagné !"
        elif mode == 22 :
            gagne = "Vous avez gagné !"
    else :
        non = 0
        for i in range (7) :
            for j in range (6) :
                if plat[i][j] == "-" :
                    non = 1
        if non == 0 :
            ecran = 3
            gagne = "Egalité."

    affich()

pygame.init()

fenetre = pygame.display.set_mode((700,650))
pygame.display.set_caption("Puissance 4")

raccourci = __file__
raccourci = raccourci[0:-8]

icone = pygame.image.load(raccourci+"icone.png")
pygame.display.set_icon(icone)

plat = []
for i in range (7) :
    plat += [["-"]]
    for j in range (5) :
        plat[i] += ["-"]
ecran = 1
mode = 1

affich()

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN :
            if ecran == 1 :
                if event.pos[0] > 100 and event.pos[0] < 500 and event.pos[1] > 200 and event.pos[1] < 280 :
                    mode = 1
                    ecran = 2
                    j = 1
                elif event.pos[0] > 100 and event.pos[0] < 500 and event.pos[1] > 400 and event.pos[1] < 480 :
                    j = 1
                    mode = 20+randint(1,2)
                    ecran = 2
            elif ecran == 2 and (mode == 1 or mode == 21 and j == 1 or mode == 22 and j == 2) and event.pos[1] > 50 and plat[event.pos[0]//100][0] == "-" :
                if j == 1  :
                    p = 0
                    while p < 6 and plat[event.pos[0]//100][p] == "-" :
                        p += 1
                    plat[event.pos[0]//100][p-1] = "x"
                    j = 2
                else :
                    p = 0
                    while p < 6 and plat[event.pos[0]//100][p] == "-" :
                        p += 1
                    plat[event.pos[0]//100][p-1] = "o"
                    j = 1
                fin_partie()

            affich()
            if ecran == 2 and (mode == 21 and j == 2 or mode == 22 and j == 1) :
                tour_ia()
                fin_partie()
        elif event.type == KEYDOWN :
            if ecran == 3 :
                if event.key == K_RETURN :
                    ecran = 1
                    plat = []
                    for i in range (7) :
                        plat += [["-"]]
                        for j in range (5) :
                            plat[i] += ["-"]

            affich()