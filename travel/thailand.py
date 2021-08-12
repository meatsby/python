class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":  # thailand.py 에서 코드를 수정하고 직접 실행할 경우
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")  # module.py 에서 ThailandPackage 를 가져다 쓸 경우 실행
