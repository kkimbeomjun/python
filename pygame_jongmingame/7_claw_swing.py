# 집게 흔들기 
import os
import pygame


# 집게 클래스 생성
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image 
        self.original_image = image
        self.rect = image.get_rect(center=position)
           
        self.offset = pygame.math.Vector2(100,0) #위치 초기화
        self.position = position 

        self.direction = LEFT #집게의 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의 (오른쪽 끝)

    def update(self):
           
        if self.direction == LEFT: # 왼쪽방향으로 이동하고 있다면
           self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT: # 오른쪽 방향으로 이동하고 있다면
           self.angle -= self.angle_speed # 이동 속도만큼 각도 감소
         
        # 만약에 허용 각도 범위를 벗어나면? 
        if self.angle > 170:
            self.angle = 170
            self.direction = RIGHT
        elif self.angle < 10 :
            self.angle = 10
            self.direction = LEFT
            
     
        self.rotate()
       #print(self.angle, self.direction)
       # rect_center = self.position + self.offset
       # self.rect = self.image.get_rect(center=rect_center)
 
    
    def rotate(self):
          self.image = pygame.transform.rotozoom(self.original_image,-self.angle, 1)
          
          offset_rotated = self.offset.rotate(self.angle)
          print(offset_rotated)
        
          self.rect = self.image.get_rect(center=self.position+offset_rotated
          ) # 네모 사각형 형태를 그려준다
          #print(self.rect)
          pygame.draw.rect(screen, RED, self.rect,1)
          
          # 회전 대상 이미지, 회전 각도, 이미지 크기
    def draw(self , screen): #그림그리기
        screen.blit(self.image, self.rect) # 클래스가 가지는 정보를 이용하여 실행
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        pygame.draw.line(screen, BLACK, self.position, self.rect.center,5)
         

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
LEFT = -1 #왼쪽방향
RIGHT = 1 #오른쪽방향

#색깔 변수
RED = (255,0,0) #RED
BLACK = (0,0,0) #검은색

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
            print("게임 종료")
    screen.blit(background, (0, 0))

    gemstsone_group.draw(screen)
    claw.update() #를 동해서 동작의 변화를 바꾼다
    claw.draw(screen)   

    pygame.display.update()

pygame.quit()
