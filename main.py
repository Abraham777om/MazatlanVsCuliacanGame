import pygame
from narco import Narco
pygame.init()

screenWidth = 1000
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("MAZATLAN VS CULIACAN")

#framesd
time = pygame.time.Clock()
FPS = 60
color = "yellow"


narco1size = 32
narco1scale = 5
narco1offset = [12, 0]
narco1data = [narco1size, narco1scale, narco1offset]
narco2size = 32
narco2scale = 6
narco2offset = [8, 4]
narco2data = [narco2size, narco2scale, narco2offset]

bg = pygame.image.load("WhatsApp Image 2022-07-22 at 9.08.51 AM.jpeg").convert_alpha()

narco1sheet =  pygame.image.load("Animaciones Komander2.png").convert_alpha()
narco2sheet = pygame.image.load("Fantasma Animacion.png").convert_alpha()

narco1animationSteps = [10, 8, 4, 8, 9, 10, 4]
narco2animationSteps = [12, 6, 4, 7, 9, 8, 4]


def background():
    newBG = pygame.transform.scale(bg, (screenWidth, screenHeight))
    screen.blit(newBG, (0, 0))

def healthBar(health, x, y):
    r = health / 100
    pygame.draw.rect(screen, "white", (x-5, y-5, 410, 40))
    pygame.draw.rect(screen, "red", (x, y, 400, 30))
    pygame.draw.rect(screen, color, (x, y, 400 * r, 30))
    pygame.draw.rect(screen, "orange", (x, y, 200, 10))


#Narco instancese
narco1 = Narco(1, 200, 250, narco1data, narco1sheet, narco1animationSteps)
narco2 = Narco(2, 700, 250, narco2data, narco2sheet, narco2animationSteps)

loop = True
while loop:
    tiempo = pygame.time.get_ticks()
    print(tiempo)
    time.tick(FPS)

    background()
    healthBar(narco1.health, 20, 20)
    healthBar(narco2.health, 580, 20)

    narco1.move(screenWidth, screenHeight, screen, narco2)
    narco2.move(screenWidth, screenHeight, screen, narco1)

    narco1.update()
    narco2.update()

    narco1.show(screen)
    narco2.show(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update()

pygame.quit()