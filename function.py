# 7.1. 함수
def open_account():
    print('새로운 계좌가 생성되었습니다.')


# 7.2. 전달값과 반환값
def deposit(balance, money):  # balance, money 는 전달값
    print('입금이 완료되었습니다. 잔액은 {}원입니다.'.format(balance + money))
    return balance + money  # balance + money 는 반환값


# 7.3. 기본값
def profile(name, age=17, main_lang='파이썬'):  # 전달값이 없을 경우 기본값 반환
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'.format(name, age, main_lang))


# 7.4. 키워드값
profile(name='유재석', main_lang='파이썬', age=20)  # 키워드에 맞게 함수 호출


# 7.5. 가변인자
def profile(name, age, *language):  # 서로 다른 갯수의 값을 사용할 때는 가변인자 *
    print('이름 : {0}\t나이 : {1}\t'.format(name, age), end=' ')
    for lang in language:
        print(lang, end=' ')
    print()

# 7.6. 지역변수와 전역변수
# 지역변수 : 함수내에서만 쓸 수 있는 변수
# 전역변수 : 프로그램내에서 어디서든 쓸 수 있는 변수


gun = 10  # 전역변수


def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun 사용
    # gun = 20 # 지역변수
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))


print('전체 총 : {0}'.format(gun))
checkpoint(2)
print('남은 총 : {0}'.format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun


print('전체 총 : {0}'.format(gun))
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}'.format(gun))
