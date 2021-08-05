import pygame
from operator import itemgetter

def copydata():
    try:
        dataf = open("dataf.txt", "w")
    except:
        try:
            dataf = open("orderthing/dataf.txt", "w")
        except:
            dataf = open("Python/orderthing/dataf.txt", "w")
    cnt = 0
    while cnt != len(data):
        dataf.write(str(data[cnt][0]) + "||")
        dataf.write(str(data[cnt][1]) + "||")
        dataf.write(str(data[cnt][2]) + "||")
        dataf.write(str(data[cnt][3]) + "\n")
        cnt += 1

def checkscreen():
    w.blit(h2font.render("Name of Item                            Stock      Price", True, (0, 0, 0)), (50, 175))
    if not(place):
        w.blit(h2font.render("Price to Manufacture", True, (0, 0, 0)), (800, 175))
    count = 0
    while (count + checkmult) != len(data):
        t2 = "$" + str(format(data[count + checkmult][2], ".2f"))
        t3 = "$" + str(format(data[count + checkmult][3], ".2f"))
        t1 = str(round(data[count + checkmult][1]))
        w.blit(h3mfont.render((data[count + checkmult][0]), True, (placeclr[count])), (50, (count + 1) * 25 + 200))
        w.blit(h3mfont.render((t1), True, (placeclr[count])), (510, (count + 1) * 25 + 200))
        w.blit(h3mfont.render((t2), True, (placeclr[count])), (650, (count + 1) * 25 + 200))
        if not(place):
            w.blit(h3mfont.render((t3), True, (placeclr[count])), (800, (count + 1) * 25 + 200))
        count += 1

try:
    config = open("config.txt", "r")
except:
    try:
        config = open("orderthing/config.txt", "r")
    except:
        config = open("Python/orderthing/config.txt", "r")
try:
    dataf = open("dataf.txt", "r+")
except:
    try:
        dataf = open("orderthing/dataf.txt", "r+")
    except:
        dataf = open("Python/orderthing/dataf.txt", "r+")

run = True
screen = "menu"
clr = [(255,255,255), (255,255,255), (255,255,255)]
select = 10
checkmult = 0
place = False
edit = False
placeselect = 0
placeselectedit = 0
write = False
selectclr = (0,0,0)
selectlist = [0,1,2]

editmult = 1

cap = config.read()
lines = dataf.readlines()
data = []
count = 0
while count != len(lines):
    datal = lines[count].replace("\n", "").split("||")
    data.append(datal)
    data[count][1] = float(data[count][1])
    data[count][2] = float(data[count][2])
    data[count][3] = float(data[count][3])
    count += 1

pygame.init()
placeclr = []
count1 = 0
while count1 != len(data):
    placeclr.append((52,52,52))
    count1 += 1



h1font = pygame.font.SysFont("bahnschrift", 50, 0, 0)
h2font = pygame.font.SysFont("bahnschrift", 34, 0, 0)
h3font = pygame.font.SysFont("bahnschrift", 24, 0, 0)
h3mfont = pygame.font.SysFont("consolas", 24, 0, 0)
w = pygame.display.set_mode((1467,750))
pygame.display.set_caption(cap)




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           copydata()
           dataf.close()
           config.close()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if screen == "menu":
                if key == pygame.K_LEFT:
                    if select != 10:
                        clr[select] = (255,255,255)
                    else:
                        select = 1
                    select = (2,0,1)[select]
                    clr[select] = (210,210,210)
                elif key == pygame.K_RIGHT:
                    if select != 10:
                        clr[select] = (255,255,255)
                    else:
                        select = 1
                    select = (1,2,0)[select]
                    clr[select] = (210,210,210)
                elif key == pygame.K_KP_ENTER or key == pygame.K_RETURN and screen == "menu":
                    if select == 0:
                        screen = "check"
                        place = False
                        edit = False
                    elif select == 1:
                        screen = "check"
                        place = True
                        edit = False
                    elif select == 2:
                        screen = "check"
                        place = False
                        edit = True
            elif key == pygame.K_ESCAPE:
                screen = "menu"
            elif screen == "check":
                for x in range(len(data)):
                    placeclr.append((52,52,52))

                ### NEXT SCREEN BROWSING KEYS ###
                if key == pygame.K_PAGEDOWN and checkmult + 21 < len(data):
                    checkmult += 21
                elif key == pygame.K_PAGEUP and checkmult - 21 >= 0:
                    checkmult -= 21

                ### SORTING KEYS ###
                elif key == pygame.K_F1:
                    data = sorted(data, key=itemgetter(0))
                elif key == pygame.K_F2:
                    data = sorted(data, key=itemgetter(1))
                elif key == pygame.K_F3:
                    data = sorted(data, key=itemgetter(2))
                elif key == pygame.K_F4:
                    data = sorted(data, key=itemgetter(3))

                ### EDIT/PLACE KEYS ###
                if 286 <= key <= 293:
                    editmult = (0.01,0.10,0.50,1,2,5,10,50)[[pygame.K_F5,pygame.K_F6,pygame.K_F7,pygame.K_F8,pygame.K_F9,pygame.K_F10,pygame.K_F11,pygame.K_F12].index(key)]

                if place == True or edit == True:
                    ### EDIT/PLACE UP/DOWN BROWSING KEYS ###
                    if key == pygame.K_DOWN and placeselect + 1 < len(data):
                        placeselect += 1
                    elif key == pygame.K_UP and placeselect - 1 >= 0:
                        placeselect -= 1
                    elif edit == True:

                        ### EDIT LEFT/RIGHT BROWSING KEYS ###
                        if key == pygame.K_RIGHT and (placeselectedit + 1) != 4:
                            placeselectedit += 1
                            write = False
                        elif key == pygame.K_LEFT and placeselectedit - 1 >= 0:
                            placeselectedit -= 1
                            write = False

                        elif key == pygame.K_INSERT:
                            if write == False:
                                data.append(["New Item", 0, 0, 0 ])
                        elif key == pygame.K_DELETE:
                            del data[placeselect]
                            placeselect -= 1
                        elif placeselectedit != 0:
                            if key == pygame.K_RSHIFT:
                                data[placeselect][placeselectedit] += editmult
                            elif key == pygame.K_KP_ENTER or key == pygame.K_RETURN:
                                data[placeselect][placeselectedit] -= editmult
                        else:
                            if key == pygame.K_KP_ENTER or key == pygame.K_RETURN:
                                write = True
                            elif write == True:
                                if key == pygame.K_BACKSPACE:
                                    b = data[placeselect][placeselectedit]
                                    b = b[: -1]
                                    data[placeselect][placeselectedit] = b
                                elif key == pygame.K_KP_ENTER or key == pygame.K_RETURN:
                                    write = False
                                    placeselectedit = 1
                                else:
                                    if placeselect < len(data):
                                        if len(data[placeselect][placeselectedit]) < 34:
                                            data[placeselect][placeselectedit] += event.unicode

                    else:
                        if key == pygame.K_KP_ENTER or key == pygame.K_RETURN:
                            data[placeselect][1] -= editmult



    w.fill((150,150,150))
    for x in range(len(data)):
        if data[x][1] <= 10 and data[x][1] > 0:
            placeclr[x] = (255, 255,0)
        elif data[x][1] == 0:
            placeclr[x] = (204,0,0)
        elif data[x][1] < 0:
            placeclr[x] = (128, 0, 0)
        else:
            placeclr[x] = (52,52,52)

    if screen == "menu":
        w.blit(h1font.render(cap + " Menu", True, (0, 0, 0)), (50,50))

        pygame.draw.rect(w, clr[0], (50, 180, 370, 200))
        w.blit(h1font.render("Check Info", True, (0, 0, 0)), (115,247))

        pygame.draw.rect(w, clr[1], (555, 180, 370, 200))
        w.blit(h1font.render("Place Order", True, (0, 0, 0)), (615,247))

        pygame.draw.rect(w, clr[2], (1050, 180, 370, 200))
        w.blit(h1font.render("Edit Data", True, (0, 0, 0)), (1130,247))
    else:
        w.blit(h1font.render(cap, True, (0, 0, 0)), (50,50))
        w.blit(h3font.render("Press 'Esc' to go back to menu", True, (0, 0, 0)), (50,125))
        if screen == "check":
            checkscreen()
        if edit == True:
            if write == True:
                selectclr = (255,0,0)
            else:
                selectclr = (0,0,0)
            if placeselectedit == 0:
                pygame.draw.rect(w, selectclr, (45, (placeselect + 1) * 25 + 196, 450, 30), 2)
            elif placeselectedit == 1:
                pygame.draw.rect(w, selectclr, (505, (placeselect + 1) * 25 + 196, 100, 30), 2)
            elif placeselectedit == 2:
                pygame.draw.rect(w, selectclr, (650, (placeselect + 1) * 25 + 196, 100, 30), 2)
            else:
                pygame.draw.rect(w, selectclr, (795, (placeselect + 1) * 25 + 196, 100, 30), 2)
        elif place == True:
            pygame.draw.rect(w, selectclr, (45, (placeselect + 1) * 25 + 196, 700, 30), 2)

    pygame.display.update()
    pygame.time.delay(100)
pygame.quit()
