# 5-1. 리스트
subway = ['유재석', '조세호', '박명수', '유재석']
subway.index('조세호')  # '조세호' 가 몇번째 자리에 있는지
subway.append('하하')  # '하하' 를 맨 마지막에 추가
subway.insert(1, '정형돈')  # '정형돈' 을 1번째 자리에 끼워넣음
subway.pop()  # 맨 마지막 원소를 반환 후 제거
subway.count('유재석')  # '유재석' 이 몇번 나오는지 확인
# 정렬
num = [5, 2, 4, 3, 1]
num.sort()  # 순서대로 정렬
num.reverse()  # 순서뒤집어서 정렬
num.clear()  # num 리스트를 초기화
num.extend(subway)  # num 에 subway 를 뒤에 붙힘

# 5-2. 사전
dict = {3 : 'three', 100 : 'hundred'}  # key:value 패턴으로 자료 저장
print(dict[3])  # key 가 3 인 value 를 출력
print(dict.get(3))  # key 가 3 인 value 를 출력
# [] 와 .get 의 차이 : 해당 key 가 없을 경우 [] 는 에러 후 프로그램 종료
# .get 은 None 을 출력 (문자열처리함수에서 .index 와 .find 와 비슷한 내용)
print(dict.get(5), '사용 가능')  # key 가 5인 value 가 없을 경우 '사용 가능' 출력
print(3 in dict)  # 3 이라는 key 가 dict 에 있을 경우 True 출력 없을 경우 False
dict['C-20'] = '이십'  # 새로운 key 와 value 선언
dict[3] = '삼'  # 기존에 있던 key 를 update
del dict[100]  # key 가 100 인 k,v 를 삭제
print(dict.keys())  # key 값들만 출력
print(dict.values())  # value 값들만 출력
print(dict.items())  # k,v 모두 출력
dict.clear()  # dict 의 모든 값 삭제

# 5-3. 튜플 (변경되지 않는 list, list 보다 속도가 빠름)
menu = ('돈까스', '치즈까스')

# 5-4. 세트 집합, set, 중복 안됨, 순서 없음
set = {1, 2, 3, 3, 3}  # {1,2,3}
java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 (java 와 python 을 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 혹은 python 을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 는 할 수 있지만 python 은 모르는 개발자)
print(java - python)
print(java.difference(python))

python.add('김태호')  # python 을 배운 개발자
java.remove('김태호')  # java 를 까먹음

# 5-5. 자료구조의 변경
menu = {'커피', '우유', '주스'}
menu = list(menu)  # set 이였던걸 list 로
menu = tuple(menu)  # list 였던걸 tuple 로
menu = set(menu)  # tuple 이였던걸 set 으로
