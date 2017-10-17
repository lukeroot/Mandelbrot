import pygame, math, random

xRes = 800
yRes = 800

xOffSet = 0
yOffSet = 0

zoom = 0
change = 30

xRes_2 = xRes/2.0
yRes_2 = yRes/2.0

xRes_4 = xRes_2/2.0
yRes_4 = yRes_2/2.0
arra = []
def initVar():

    global xRes_2, yRes_2, xRes_4, yRes_4
    xRes_2 += xOffSet
    yRes_2 += yOffSet

    yRes_4 += zoom
    xRes_4 += zoom

screen = pygame.display.set_mode((xRes,yRes))
pygame.init()

def mad(x, y, n):
    c = complex((x - xRes_2)/xRes_4, (y - yRes_2)/yRes_4)
    #is abs(x, y):
    z = 0
    for s in range(0,int( abs(n) % 255) ):
        z = z**2 + c
        if abs(z) > 2 and abs(z) != 0:
            return (255,255,1)
            return ((abs((z * 102) % 255) * 100) % 255, (abs((z * 101) % 255) * 1000) % 255, (abs((z * 100) % 255) * 10000) % 255)
            #mad((abs(z**2 + (abs((z**2 +c ) % 255)** 2)) % 255),(abs(z**2 + (abs((z**2 +c ) % 255)** 2)) % 255),(abs(z**2 + (abs((z**2 +c ) % 255)** 2)) % 255))
            #mad(abs(abs(z**2 + c)**2 + c) % 255, abs(abs(z**2 + c)**2 + c) % 255, abs(abs(z**2 + c)**2 + c) % 255)
        mad(0,0,0)

# lastX =
# lastY =
def norm(x, y):
    global end_pos, start_pos

    xRes_2 = x - start_pos/2.0
    yRes_2 = y - end_pos/2.0

    xRes_4 = xRes_2/2.0
    yRes_4 = yRes_2/2.0

    return complex((x  - xRes_2)/xRes_4, (y - yRes_2)/yRes_4)

def mandel(c, n):
    global xRes_2, yRes_2, xRes_4, yRes_4
    #start_pos = x * start_pos
    #y = abs(complex(800,800) - end_pos) / 2
    x, y = c
    c = complex((x  - xRes_2)/xRes_4, (y - yRes_2)/yRes_4)
    #is abs(x, y):
    z = 0
    for s in range(0, int(abs(n))):
        z = z**2 + c
        if abs(z) > 2:
            # return (255,255,1)
            return ((abs((z**2 + c) % 255) * 101.0) % 255, (abs((z**2 + c) % 255) * 101.01) % 255,(abs((z**2 + c) % 255) * 101.001) % 255)
            # return (mad(x, y, z), mad(x, y, z), mad(n, n, n))
    return (0,0,0)

def draw():

    global screen
    screen.fill((0,0,0))
    for x in range(0, xRes, change):
        for y in range(0, yRes, change):
            # mandel(x, y, 250)
            try:
                screen.set_at((x, y), mandel((x, y), 800))

            except RuntimeError:

                pass
start_pos = 1
end_pos = 1
draw()

while (True):
    pygame.event.get()
    pygame.display.flip()
    # if pygame.mouse.get_pressed() == (1,0,0):
    #     start_pos = pygame.mouse.get_pos()
    #     while pygame.mouse.get_pressed() == (1,0,0):
    #         end_pos = pygame.mouse.get_pos()





    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                change -= 1
                if change < 1:
                    change = 1
                else:

                    draw()
            if event.key == pygame.K_2:
                change += 1
                if change > 100:
                    change = 100
                else:
                    draw()
            if event.key == pygame.K_q:

                pygame.quit()
                quit()

            if event.key == pygame.K_UP:
                yOffSet += 10
                initVar()
                draw()

            if event.key == pygame.K_DOWN:
                yOffSet -= 10
                initVar()
                draw()

            if event.key == pygame.K_LEFT:
                xOffSet += 10
                initVar()
                draw()

            if event.key == pygame.K_RIGHT:
                xOffSet -= 10
                initVar()
                draw()

            if event.key == pygame.K_p:
                zoom += 50
                initVar()
                draw()

            if event.key == pygame.K_l:
                zoom -= 50
                initVar()
                draw()

