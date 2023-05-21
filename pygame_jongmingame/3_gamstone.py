import os
import pygame

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position): 
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)

def setup_gemstone():
    global gemstsone_group
    small_stone = Gemstone(gemstone_images[0], (200, 380))
    gemstsone_group.add(small_stone)
    gemstsone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    gemstsone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    gemstsone_group.add(Gemstone(gemstone_images[3], (900, 420)))

pygame.init()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_stone.png")),
    pygame.image.load(os.path.join(current_path, "big_stone.png")),
    pygame.image.load(os.path.join(current_path, "stone.png")),
    pygame.image.load(os.path.join(current_path, "diamond.png"))
]

gemstsone_group = pygame.sprite.Group()
setup_gemstone()

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstsone_group.draw(screen)

    pygame.display.update()

pygame.quit()
