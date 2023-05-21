# 집게를 어느 지점(pivot, 중심점) 으로부터 떨어트려서 배치하는 것
import os
import pygame


# 집게 클래스 생성
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image 
        self.rect = image.get_rect(center=position)
           
        self.offset = pygame.math.Vector2(default_offset_x_claw,0) #위치 초기화
        self.position = position 

    def update(self):
        rect_center = self.position + self.offset
        self.rect = self.image.get_rect(center=rect_center)

    def draw(self , screen):
        screen.blit(self.image, self.rect) # 클래스가 가지는 정보를 이용하여 실행
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시


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

default_offset_x_claw = 40 # 중심적으로부터 집게까지의 기본 x 간격


#색깔 변수
RED = (255,0,0) #RED

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

#집게
claw_imag = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_imag , (screen_width // 2, 110)) #가로위는 화면 가로 기준으로 절반, 위에는 110 정도


running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstsone_group.draw(screen)
    claw.update()
    claw.draw(screen)   

    pygame.display.update()

pygame.quit()
