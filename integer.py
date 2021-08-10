# 3-3. 숫자처리함수
print(abs(-5))  # 5
print(pow(4, 2))  # 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 3

# math library
from math import *  # math lib 에 있는 모든 기능을 쓰겠다.
print(floor(4.99))  # 4
print(ceil(3.14))  # 4
print(sqrt(16))  # 4

# 3-4. 랜덤함수 (무작위로 숫자를 뽑아줌)
from random import *
print(random())  # 0.0 ~ 1.0 미만의 무작위 실수를 반환
print(randrange(1, 46))  # 1 ~ 46 미만의 무작위 실수를 반환
print(randint(1, 45))  # 1 ~ 45 이하의 무작위 정수를 반환
lst = list(range(1, 21))
shuffle(lst)  # lst 값의 위치를 무작위로 변경
print(sample(lst, 1))  # lst 에서 무작위 값을 1 개 반환
