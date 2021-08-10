# 4-3. 문자열처리함수
var = 'Python is Amazing'
print(var.lower())  # 소문자 변환
print(var.upper())  # 대문자 변환
print(var[0].isupper())  # 대문자인지 확인 (True, False)
print(len(var))  # 문자열의 길이 반환
print(var.replace('Python', 'Java'))  # 'Python' 을 'Java' 로 변환
index = var.index('n')  # 'n' 이라는 문자의 위치 반환
index = var.index('n', index + 1)  # 처음 찾은 index 다음에 나오는 'n' 문자 위치 반환
print(var.find('Java'))  # 원하는 값이 없을 경우 -1 을 반환
# .index 와 .find 의 차이 : 원하는 값이 없을 경우 index 는 에러 find 는 -1
print(var.count('n'))  # 'n' 이 총 몇번 나오는지 반환

# 4-4. 문자열포맷
# Method 1
print('I am %d years old.' % 20)  # %d 는 정수만 반환 가능 decimal
print('I like %s.' % 'Python')  # %s 는 문자열만 반환 가능 string
print('Apple starts with %c.' % 'A')  # %c 는 한문자만 반환 가능 character
print('I like %s and %s.' % ('blue', 'red'))  # 뒷 부분에 소괄호를 이용하여 여러개 반환 가능
# Method 2
print('I am {} years old.'.format(20))  # % 대신에 format 함수를 활용하여 {}로 같은 기능 활용 가능
print('I like {0} and {1}.'.format('blue', 'red'))  # {} 안에 index 를 부여함으로써 format 함수에 들어있는 값들을 순서에 맞게 반환 가능
print('I am {age} and I like {color}.'.format(age=20, color='red'))  # {} 안에 변수를 선언함으로써 format 함수에 들어있는 값들을 변수에 맞게 반환 가능
# Method 3
age = 20
color = 'red'
print(f'I am {age} and I like {color}.')  # .format() 대신 f 로도 사용 가능

# 4-5. 탈출 문자
'\n'  # 줄바꿈
'\''  # 작은 따옴표를 문자로 변환
'\\'  # '\' 문자로 변환
'\r'  # 커서를 맨 앞으로 이동
'\b'  # 한 글자 삭제
'\t'  # 탭
