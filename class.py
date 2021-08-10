# 9-1. 클래스
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = '마린'
hp = 40
damage = 5

print('{} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반모드/시즈모드
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))


def attack(name, location, damage):
    print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(name, location, damage))


attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)


class Unit:  # Class 는 붕어빵틀 과 같음
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))


marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank1 = Unit('탱크', 150, 35)

# 9-2. __init__ # 생성자, 객체는 어떤 클래스로부터 만들어지는것들, 마린과 탱크는 Unit 클래스의 인스턴스라고함

# 9-3. 멤버변수 # self.name, self.hp, self.damage, 클래스 내에서 정의된 변수, 클래스내에서 초기화할수도 있고 쓸수도 있음

wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))  # 클래스 외부에서 .name 과 같은 멤버변수에 접근 가능

wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True  # clocking 이라는 변수는 외부에서 선언

if wraith2.clocking:
    print('{0} 는 현재 클로킹 상태입니다.'.format(wraith2.name))
# 클래스 외부에서 변수 확장 가능, 그 변수는 내가 확장한 객체에만 적용이 됨
# 파이썬에서는 외부에서 어떤객체에 추가로 변수를 만들어서 사용 가능

# 9-4. 메소드


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))


firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25)

# 9-5. 상속


class Unit:  # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))


class AttackUnit(Unit):  # 자식 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # 다른 클래스에 비슷한 구문이 있을 경우 상속시켜줌
        self.damage = damage

# 9-6. 다중 상속


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):  # 여러가지 클래스를 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 9-7. 연산자 오버라이딩  (자식클래스에서 정의한 메소드를 쓰고싶을때 메소드를 새롭게 정의해서 사용하는 것을 오버로딩이라고 함)


vulture = AttackUnit('벌쳐', 80, 10, 20)
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.move('9시')

# 9-8. pass


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass  # 아무것도 안하고 일단 넘어가라


game_start()
game_over()

# 9-9. super


class BuildingUnit(Unit):  # 건물
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location
# 부모 클래스와 super()의 차이점 : __init__ 을 할 때 super() 는 self 를 사용하지 않아도 됨
# 다중상속을 할 경우 부모 클래스에 갯수에 따라 초기화를 해줘야함


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
