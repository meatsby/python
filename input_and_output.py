# 8-1. 표준입출력
print('Python', 'Java', 'JavaScript', sep=' vs ')  # sep 를 통해 출력간 사이에 어떤 문자가 들어갈 지 설정 가능
print('Python', 'Java', 'JavaScript', end='?')  # end 를 통해 출력문 마지막에 들어갈 문자를 설정 (기본값은 줄바꿈)
scores = {'수학' : 0, '영어' : 50, '코딩' : 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')
    # ljust() = 왼쪽 정렬
    # rjust() = 오른쪽 정렬

for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))
    # zfill() = 세개 공간을 확보 후 남은 공간은 0 으로 채우기

# 8-2. 다양한 출력포맷
    print('{0: >+10}'.format(500))  # 10칸 확보, 오른쪽 정렬, 양수음수 구분
    print('{0:_<+10}'.format(500))  # 10칸 확보, 왼쪽 정렬, 양수음수 구분, 빈칸은 밑줄로 채우기
    print('{0:+,}'.format(100000000))  # 3자리마다 콤마 찍어주고, 부호 구분
    print('{0:^<+30,}'.format(100000000))  # 3자리마다 콤마 찍어주고, 부호 구분, 30자리 확보, 왼쪽정렬, 빈자리 ^로 채우기
    print('{0:.2f}'.format(5/3))  # 소수점 2번째자리까지 출력

# 8-3. 파일입출력
    score_file = open('score.txt', 'w', encoding='utf8')
    print('수학 : 0', file=score_file)
    print('영어 : 50', file=score_file)
    score_file.close()  # 파일 닫기
    # open(파일이름, 목적, encoding='utf8')

    score_file = open('score.txt', 'a', encoding='utf8')
    score_file.write('과학 : 80')
    score_file.write('\n코딩 : 100')
    score_file.close()
    # 'a' 를 통해 append
    # .write() 를 통해 내용 추가, 줄바꿈 필요

    score_file = open('score.txt', 'r', encoding='utf8')
    print(score_file.read())
    score_file.close()
    # 전체 파일 읽기

    score_file = open('score.txt', 'r', encoding='utf8')
    while True:
        line = score_file.readline()  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
        if not line:
            break
        print(line, end='')  # realline() 과 print() 가 줄바꿈을 하기 때문에
    score_file.close()
    # 파일이 몇줄인지 모를 경우 while 문 사용

    score_file = open('score.txt', 'r', encoding='utf8')
    lines = score_file.readlines()  # 모든 라인을 리스트 형태로 저장
    for line in lines:
        print(line, end='')
    score_file.close()

# 8-4. pickle (컴퓨터가 알아볼 수 있는 데이터형태로 저장)
import pickle
profile_file = open('profile.pickle', 'wb')  # wb = write binary
profile = {'이름' : '박명수', '나이' : 30, '취미' : ['축구', '골프', '코딩']}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file)  # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# 8-5. with (파일을 읽고 쓰는데 있어서 코드가 간결해지고 매번 파일을 닫아줄 필요가 없음)
with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))
# 위에 파일을 읽기 정보를 가져오는 과정이랑 같지만 파일을 다시 닫아줄 필요가 없음
# pickle 없이 파일 쓰기
with open('study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')
# pickle 없이 파일 읽기
with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())
