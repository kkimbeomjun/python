# 레퍼런스 카운팅 방법
import sys
a = 3
print(sys.getrefcount(a))
# 각각 카운팅이 되는 것을 알 수 있다.
b = 3
c = 3
print(sys.getrefcount(3))

a = [0,1,2]
print(sys.getrefcount(a))

x = [1, 2, 3]
y = x

# 레퍼런스 카운트 출력
import sys
print(sys.getrefcount(x)) 


# 레퍼런스 카운트 출력
print(sys.getrefcount(x)) 

# 메모리 누수가 발생하는 예제

# 1. 순환 참조에 의한 메모리 누수
class Node:
    def __init__(self):
        self.next = None

nosu1 = Node()
nosu2 = Node()
nosu1.next = nosu2
nosu2.next = nosu1

# 2. 파일 리소스의 명시적인 해제를 하지 않은 경우
def read_large_file():
    file = open('test.txt', 'r')
    data = file.read()
    # 파일을 닫지 않고 함수가 종료됨

# 3. 큰 데이터 구조의 임시 사용 후 해제하지 않은 경우
def process_large_data():
    large_data = [1] * 10000
    # large_data를 사용한 후 더 이상 필요하지 않지만 해제하지 않음

read_large_file()