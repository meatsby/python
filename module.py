# 11-1. 모듈 (부품처럼 만들어진 파일, 유지보수 쉽고 코드의 재사용도 수월)
# 모듈은 파일과 같은 경로에 있거나 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용가능
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv  # as 를 통해 줄여서 사용가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *  # 다른 구문 없이 함수를 바로 사용가능
# price(3)
# price_morning(4)
# price_soldier(5)

# 11-2. 패키지 (하나의 디렉토리에 여러 모듈 파일들을 모아놓은 집합)
# import travel.thailand  # 패키지.모듈
# trip_to = travel.thailand.ThailandPackage()  # 객체 = 패키지.모듈.클래스
# trip_to.detail()  # 객체.함수

# from travel.vietnam import VietnamPackage  # from 패키지.모듈 import 클래스
# trip_to = VietnamPackage()  # trip_to 객체에 VietnamPackage() 클래스 선언
# trip_to.detail()  # 객체.함수

# 11-3. __all__
# from travel import *
# * 을 쓸 경우 travel package 에서 개발자가 설정한 공개범위에 따라 사용가능
# 패키지 안에 있는 __init__ 파일에서 __all__ 로 공개할 모듈을 설정해줘야함
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 11-4. 모듈 직접 실행
# 모듈이 잘 작동하는지 테스트
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 11-5. 패키지, 모듈 위치
# import inspect  # inspect 를 통해 패키지나 모듈의 위치를 확인
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# 11-6. pip.install (pip 로 패키지 설치하기)
# pip install beautifulsoup4 (패키지 설치)
# pip list (현재 설치된 패키지)
# pip show beautifulsoup4 (패키지 정보)
# pip install --upgrade beautifulsoup4 (패키지 업데이트)
# pip uninstall beautifulsoup4 (패키지 삭제)

# 11-7. 내장함수
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# import random  # 외장 함수
# print(dir(random))  # random 모듈 내에서 쓸 수 있는 함수들

# 11-8. 외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir 과 같은 기능)
# import glob
# print(glob.glob("*.py"))  # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())  # glob 과 비슷한 기능

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

# 11-9. 퀴즈 #10
# import byme
# byme.sign()
