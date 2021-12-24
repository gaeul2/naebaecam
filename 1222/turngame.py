# '몬스터' 와 '플레이어'가 각각 존재하고 모두 이름/hp/공격력이라는 공통속성가짐
# 공통속성을 가진부분을 부모 클래스로 만들어주면 되겠지?
# 그리고 Object클래스는 공격이라는 메소드를 가지고 있다.
# return 위치 잘못두면 내가 원하는대로 실행안되고, 인자와 꼭 맞게 연결되도록 잘 써라!!
class Object:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    def attack(self,target):#이 함수는 '공격하고자 하는 대상을 인자로받으며
        #공격시 누가 누구를 공격했고, 그에따라 공격받은 대상의 체력이 얼마나 남았는지 출력
        print(f'{self.name}이(가) {target.name}을(를) 공격!')
        print(f'{target.name}에게 {self.power}만큼의 데미지!')
        #실행시 공격하고자 하는 대상의 hp를 자신의 공격력만큼 감소시킴.
        target.hp = target.hp - self.power
        #target을 인자로 받기때문에 인자를 잘 입력해주면 a.hp = self.hp처럼 작동하여 a의 hp에 적용됨
        #
        if(target.hp <= 0):
            print(f'{target.name}을(를) 죽였습니다!')# 나였으면 여기에다 또 그 죽은아이의 상태를 넘겨주려고 했을거야..
        else:
            print(f'{target.name}의 HP가 {target.hp}이 되었습니다.')

# # 플레이어 클래스는 object클래스를 상속받으며, 마법이라는 메소드를 가지고있음.
class Player(Object): #여기서 player의 체력,공격력 을 명시했다면 잘못된 방법
    def magic(self, target): # 공격하고자 하는 대상을 인자로 받음. target을 인자로 받기때문에 우리가 공격할때
                             # 몬스터 이름(ex.b)을 말하면 b가 Object의 인스턴스이므로 target.name하면 b.name이고
                             # target.hp라면 b.hp가 되는 원리리        print(f'{self.name}이(가) {target.name}에게 마법을 사용!') # 공격시 누가 누구를 공격했고,
        print(f'{self.name}이(가) {target.name}에게 마법을 사용!')
        print(f'{target.name}에게 50만큼의 데미지')
        target.hp = target.hp - 50 #마법공격은 공격하고자 하는 대상의 HP를 50만큼 감소시킴
        if (target.hp <= 0):
            print(f'{target.name}을(를) 죽였습니다.')
        else:
            print(f'{target.name}의 HP가 {target.hp}이 되었습니다.')#공격받은 대상의 체력이 얼마나 남았는지 출력


#Monster 클래스는 Object 클래스를 상속받으며, '대기'와 '치료'라는 메소드를 가지고 있습니다.
class Monster(Object): #여기서 Monster의 체력,공격력 을 명시했다면 잘못된 방법
    def stay(self):#대기라는 함수는 self 외에는 다른 인자를 받지 않으며,
        print(f'{self.name}(이)가 대기했습니다.') # 그냥 "~~가 대기했습니다" 만 출력됩니다.
#자기 자신의 HP를 10 증가시키는 기능을 가지고 있습니다. 증가시킬 때는 "~~가 자신의 체력을 10만큼 회복했다" 가 출력됩니다.
    def cure(self): #치료라는 함수는 self 외에는 다른 인자를 받지 않으며,
        self.hp = self.hp + 10 #자기 자신의 HP를 10 증가시키는 기능을 가지고 있습니다.
        print(f'{self.name}이(가) 자신의 체력을 10만큼 회복했다. 현재체력은 : {self.hp}')

#@title [함수 생성 파트]
from random import choice
from time import sleep #sleep은 게임을 진행할때 텍스트를 보기편하게 하기위함

def createobjects(): # 생성함수로 플레이어와 몬스터들을 만든다. 쉽게!
    # 전사는 Player 클래스의 인스턴스로서, 100의 체력, 10의 공격력을 가지고 있습니다.
    Warrior = Player('전사',100,10)

    # input으로 누구를 공격하겠다 했을때 미니고블린으로 쳤다고해서 그게 인스턴스 미니고블린이라는건 아님
    # 그래서 input에 미니고블린이라고 치면 playerturn함수에서 Monsters["target"]에 미니고블린이 들어감.
    # 그럼 '미니고블린'이라는 키값을 가진 그안에 저장된 미니고블린 인스턴스값이 나옴
    # 고블린들은 모두 Monster 클래스의 인스턴스로서,
    Monsters = {} #얘네를 딕셔너리로 관리하면 편하겠지?     #Object클래스를 상속받은 Monster클래스에서 몬스터 생성과정인거고
    Monsters['미니고블린'] = Monster('미니고블린',10,10) #  미니고블린은 10의 체력과 10의 공격력을,
    Monsters['고블린'] = Monster('고블린',30,30) # 고블린은 30의 체력과 30의 공격력을,
    Monsters['슈퍼고블린'] = Monster('슈퍼고블린',50,50) # 슈퍼고블린은 50의 체력과 50의 공격력을 가지고 있습니다.
    #딕셔너리 키값 = value값 기억하고있지? 없는 키값,벨류값넣으면 저장이 된다는것도!
    return Warrior, Monsters #전사생성, 몬스터생성후 Monsters 딕셔너리로 반환 ! 이값은 맨밑 실행구역에 등장!.


#정보 표시 함수 : 턴이 시작하기 전에, 우선은 해당 턴을 시작할 때
def showinfo(Player, Monsters): #플레이어와 몬스터딕셔너리를 인자로 받는다(확인해야하니까)
    print("-----------턴 시작------------")
    print(f'{Player.name}의 체력:{Player.hp}') #플레이어는 한명이니까 바로 이렇게 표시하고
    #몬스터들은 딕셔너리안에 있으니 반복문으로 꺼내온다.
    for key, value in Monsters.items(): # 딕셔너리는 말이야 딕셔너리이름.items()하면 그안에 (키,벨류)가 이렇게나와
        #그러니까 반복문으로 key값은 key에 넣고 value값은 value에 넣어서!!
        print(f'{value.name}의 체력 : {value.hp}') #고블린들의 체력이 얼마인지를 표시합니다.
    # (단, 이미 체력이 0이 되어서 죽은 고블린의 체력은 표시하지 않습니다.) 이건 어디서 처리하냐면!! 몬스터 사망여부체크함수에서!!
#플레이어 턴 함수
def playerturn(Player,Monster): #인자와 return을 꼭 써주는게 중요함!! 둘다 안쓰게되면 외부에 변수가 너무많아졌을때 내가 정확히 어디서 오류가 났는지 찾기 힘들다고 이해하면 좋다.
    # playerturn(Warrior, Monsters)로 실행해서
    #플레이어와 몬스터를 인자로 받아야 함수내부에서 내부변수로 안전하게 처리함
    print('---------- 플레이어 턴 -----------')
    #예외처리는 나중에 (실습은 작성할 코드 자체가 많으므로, input 값에 따른 예외처리는 아예 하지 않는 것을 권장합니다!)
    # 전사의 행동 (공격/마법 + 그 대상) 은 Input 에 따라 이루어집니다.
    command = input('공격? 마법? : ') #. 사용자한테 공격을 선택할지, 마법을 선택할지를 input 함수로 물어보고,
    target = input('누구를 공격? : ') # 누구를 공격할지 또한 Input 함수로 물어봅니다.
    if command == '공격': #공격이라고 치면 attack메소드를 실행해야겠지? 인자로 target이 들어가도록 하고
        #Player를 인자로 받지않고 Warrior.attack으로 작성하면 위험한 규칙. 함수외부의 변수를 실행하는것이므로
        Player.attack(Monsters[target])#그러면 그 target으로 받은 값을 토대로 전사는 하나의 몬스터를 대상으로 공격을 하거나
    elif command =='마법':##마법이라고 치면 magic메소드를 실행해야겠지? 인자로 target이 들어가도록 g한다.
        Player.magic((Monster[target]))
    return Monsters #플레이어가 공격하면 몬스터의 체력값이 바뀌므로 메소드실행에 따른 값변화를 Monsters로 반환한다.

#몬스터 사망 여부 체크 함수 : 플레이어 턴이 끝났을 때, 체력이 0 이하인 몬스터가 있다면 해당 몬스터는 앞으로 정보가 표시되지 않도록 하는 작업을 진행합니다.
def check_mdead(Monsters):
    #이번턴에 죽은 몬스터 있나 확인
    dead_monsters = [] #리스트 만들어주고
    for key, value in Monsters.items():
        if value.hp<= 0 : #반복문 돌면서 hp가 0인 애있으면
            dead_monsters.append(key) # 그아이의 key값을 dead_Monsters의 리스트에 넣어!
    #죽은 몬스터는 몬스터명단에서 삭제
    for i in dead_monsters: #dead_Monsters 리스트에서 반복돌려서 나온값은 key값이지?
        del Monsters[i]    # 딕셔너리는 key를 del로 지우면, 딕셔너리에서 키랑 값이 같이 사라져
    #남은몬스터가 없다면 승리 출력, 있다면 몬스터 그대로 리턴~
    if len(Monsters) <= 0:# 여기서 사망 여부를 체크했더니, 모든 몬스터가 다 사망했다면,
                            # 함수 밖에서 '승리' 를 출력하고 While 문을 빠져나오도록 작성합니다. (즉, 게임을 종료)
        return Monsters, True #return으로 반환하는값은 몬스터정보, True 이렇게 두개인것이다!!
    else:
        return Monsters, False #참거짓으로 어디쓰이는지 잘봐!! 얘는 맨밑에 와일문에서 쓰인다!!

#몬스터 턴 함수 :
# (즉, 몬스터 턴에서는 몬스터 3마리 각각 하나의 행동을 실행해야 합니다. )
def monsterturn(Player, Monsters):
    print('---------- 몬스터 턴 -----------')
    sleep(3) #시간으로 몬스터생각하는척. # 몬스터 중 1마리만 행동을 실행하고 턴이 넘어가는 것이 아닙니다!
    for key,value in Monsters.items():#모든 몬스터는 각각 랜덤하게 하나의 행동을 실행합니다. 그래서 몬스터마다 행동을 랜덤하게 뽑도록
        command = ['cure','attack','stay'] #몬스터의 행동 (치료, 대기, 공격) 은 랜덤하게 이루어집니다.
        command = choice(command) #따라서 플레이어턴때와 달리 input이 아닌 3가지 선택지를 리스트에 넣고 랜덤으로 받아서
                                   #몬스터 턴의 행동을 고름
        if command =='cure':
            value.cure()#value는 몬스터정보이니까 몬스터클래스의 cure메소드 적용
        elif command =='stay':
            value.stay()#몬스터클래스의 stay메소드 적용
        elif command =='attack':
            value.attack(Player) # attack이 골라지면 attack메소드. 얘는 target인자가 필요하므로 Player넣어줌
    return Player # 몬스터니까 플레이어 hp에 변화가 생겼겠지? 거기에 리턴!


#플레이어 사망 여부 체크 함수 : 몬스터 턴이 끝났을 때, 플레이어의 체력이 0 이하라면 함수 밖에서 '패배'를 출력하고 While 문을 빠져나오도록 작성합니다.
def check_pdead(Player):#플레이어 죽었나 확인해야되니까 Player인자로 받음
    if Player.hp <=0: # 여기서 플레이어 hp를 체크했더니, 0이라면
        return True  #함수 밖에서 '패배' 를 출력하고 While 문을 빠져나오도록 작성합니다. (즉, 게임을 종료)
    else:
        return False


#<시작>
#위에 함수로 객체생성함수를 만들었으니 워리어와 몬스터를 이렇게 만들어보자!!
Warrior, Monsters = createobjects()
# 객체생성함수에서 return값이 Warrior와, MOnsters이니 그대로 받아!!
#게임턴은 주고받을거니까 While문안에 넣자
while True:
    # 1번순서 : 체력확인
    showinfo(Warrior, Monsters) #showinfo함수는 Player와 Monster인수 받음
    # 2번순서 :플레이어턴부터 시작. 플레이어턴에서 줄어든 몬스터hp값을 몬스터딕셔너리에 넣기
    Monsters = playerturn(Warrior,Monsters) #playerturn은 Player와 Monster인수 받음
    sleep(1) #잠깐 시간을 줘야 읽기편함
    # 3번순서 : 몬스터 사망여부 체크
    Monsters, ismdead = check_mdead(Monsters)
    # 왜 두개냐면 check_mdead함수에서 return으로 Monster와 True/False를 넘겨주기때문!
    # 함수에서 두개를 넘겨줬는데 받는 그릇이 하나라는건 안된다라는게 튜터님의 설명!
    # 몬스터 사망여부 체크함수로 변화된 몬스터딕셔너리 값과, 딕셔너리값에 아무것도 없다면 True/아직있다면 False를 각각
    # Monsters에 저장하고 ismdead에 저장!!
    if ismdead: #True는 늘 생략이니까 ismdead =True 와 같은뜻
        print('승리!!') #몬스터가 다 죽었으면 승리출력하고 while문 빠져나옴(게임종료)
        break
    # 4번 순서: 몬스터턴
    Warrior = monsterturn(Warrior,Monsters)
    # 5번순서: 플레이어 사망여부 체크
    ispdead = check_pdead(Warrior)
    if ispdead: #플레이어 체력이 없으면 패배출력하고 while문 빠져나옴(게임종료)
        print('패배!!')
        break
    sleep(1)
