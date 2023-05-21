#배경 이미지 설정
import os
import pygame # 파일게임 참조

pygame.init()

screen_width = 1000 # 가로세로 정하기
screen_height = 500
screen = pygame.display.set_mode((screen_width , screen_height)) #생성해주기
pygame.display.set_caption("Gold Miner") # 게임 이름

clock = pygame.time.Clock() # 시간 정해죽 


#배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path,"background.png")) #파일 이름은 current_path 로 설정 했기 떄문에 사용
# 파일에 있는 백그라운드 사진 배경화면으로 첨부

screen.blit(background, (0, 0))

pygame.display.update() # 계속 해서 업데이트

running = True
while running:
    clock.tick(30) #FPS 값이 30 으로 고정

    for event in pygame. event.get():
        if event.type == pygame.QUIT:
            running = False
# 타임 루프 끝나면 게임 종료를 한다는 것을 설정 해준 것
pygame.quit()