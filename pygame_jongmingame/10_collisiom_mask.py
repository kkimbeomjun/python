# 충돌처리마스크
import os
import pygame
import math

class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image 
        self.original_image = image
        self.rect = image.get_rect(center=position)
           
        self.offset = pygame.math.Vector2(default_offset_x_claw,0) #위치 초기화
        self.position = position 

        self.direction = LEFT #집게의 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의 (오른쪽 끝)

    def update(self, to_x):
           
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
            
        self.offset.x += to_x
        self.rotate()
        
    def rotate(self):
          self.image = pygame.transform.rotozoom(self.original_image,-self.angle, 1)
          offset_rotated = self.offset.rotate(self.angle)
          self.rect = self.image.get_rect(center=self.position+offset_rotated) # 네모 사각형 형태를 그려준다
    
    def set_direction(self, direction): # 방향 선택 하기
        self.direction = direction
    
    def draw(self , screen): #그림그리기
        screen.blit(self.image, self.rect) # 클래스가 가지는 정보를 이용하여 실행
        pygame.draw.line(screen, BLACK, self.position, self.rect.center,5)
         
    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed): # 점수와 스피드 값 생성하기 
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price 
        self.speed = speed
    
    def set_position(self, position, angle): ## 집게 이미지 중심 좌표 position 
        r = self.rect.size[0] // 2 #동그라이 이미지 기준으로 반지름
        rad_angle = math.radians(angle) # 각도
        to_x = r * math.cos(rad_angle) #삼각형의 밑변
        to_y = r * math.sin(rad_angle) #삼격형 높이
        self.rect.center = (position[0] + to_x, position[1] + to_y)

def setup_gemstone():

    small_gold_price, small_gold_speed = 100,5
    big_gold_price, big_gold_speed = 300, 2 
    stone_price, stone_speed = 10 ,2
    diamone_price, diamond_speed = 600,7

    small_stone = Gemstone(gemstone_images[0], (200, 380) , small_gold_price, small_gold_speed) # 번째 이미지를 (200, 380)
    
    gemstsone_group.add(small_stone)
    
    gemstsone_group.add(Gemstone(gemstone_images[1], (300, 500),  big_gold_price, big_gold_speed))
    
    gemstsone_group.add(Gemstone(gemstone_images[2], (300, 380) ,   stone_price, stone_speed))
    
    gemstsone_group.add(Gemstone(gemstone_images[3], (900, 420),   diamone_price, diamond_speed ))

pygame.init()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

# 게임 관련 변수
default_offset_x_claw = 40 # 중심적으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수
caught_gemstone = None # 집게를 뻗어서 잡은 보석 정보

#속도 변수 
move_speed = 12 # 발사할 때 이동 스피드
return_speed = 20 #아무것도 없이 돌아올 때 이동 스피드

LEFT = -1 #왼쪽방향
STOP = 0 # 이동 방향이 좌우가 아닌 고정인 상태 (집게를 뻗음)
RIGHT = 1 #오른쪽방향

#색깔 변수
RED = (255,0,0) #RED
BLACK = (0,0,0) #검은색

current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "big_stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()
]

gemstsone_group = pygame.sprite.Group() # 모든 보석들이 들어있는 곳
setup_gemstone()

#집게
claw_imag = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw = Claw(claw_imag , (screen_width // 2, 110)) #가로위는 화면 가로 기준으로 절반, 위에는 110 정도


running = True
while running:
    clock.tick(30) #FPS 값이 30 으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("게임 종료")
        
        if event.type == pygame.MOUSEBUTTONDOWN :  #마우스를 누를 떄 집게를 뻗음
           claw.set_direction(STOP) # 좌우멈춤
           to_x = move_speed # move_speed 만큼 빠르게 쭉 뻗음
       
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed

    if claw.offset.x < default_offset_x_claw: #윈위치에 오면
        to_x = 0
        claw.set_init_state() # 처음 상태로 되돌림

        if caught_gemstone: # 잡힌 보석이 있다면
             # update_score(caught_gemstone.price) #점수 업데이트 처리
             gemstsone_group.remove(caught_gemstone) # 그룹에서 잡힌 보석 제외
             caught_gemstone = None

    if not caught_gemstone: # 잡힌 보석이 없다면 충돌 체크
        for gemstone in gemstsone_group:
            # if claw.rect.colliderect(gemstone.rect): 직사각형 기준으로 충돌 처리
            if pygame.sprite.collide_mask(claw , gemstone) : # 투평 영역은 제외하고 실제 이미지 만 함
                 caught_gemstone = gemstone #잡힌보석
                 to_x = -gemstone.speed #잡힌 보석의 속도에 - 한 값을 이동 속도로 설정
                 break

    if caught_gemstone:
         caught_gemstone.set_position(claw.rect.center, claw.angle)


    screen.blit(background, (0, 0))

    gemstsone_group.draw(screen)
    claw.update(to_x) # 통해서 동작의 변화를 바꾼다
    claw.draw(screen)   
    
    pygame.display.update()

pygame.quit()
