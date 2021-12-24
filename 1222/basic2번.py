#이름 동물 지정 인스턴스 생성하는 동물 클래스
class Animal:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

        print(f'동물 {self.kind} {self.name}이(가) 생성되었습니다.')
        # print('동물 {0} {1}이(가) 생성되었습니다.'.format(self.kind, self.name))
        # #이건 제가 그냥 적어본겁니다.

class Cat(Animal):
    def meow(self):
        return f'{self.name}은 야옹' #바로 리턴값에서 f-string쓰고 문장으로 값 반환

class Dog(Animal):
    def bark(self,mung):
        self.mung = mung
        print(f'동물 {self.kind} {self.name}이(가) 생성되었습니다. {self.mung}하고 우네요')
        # return쓰지 않고 바로 print되도록 하고 대신 값은 반환되지는 않겠지?
#
# a = Animal('햄스터','토리')
b = Cat('고양이', '꾸꾸')
print(b.meow()) #값반환한거 보려면 print.

c = Dog('강아지', '보름이') #강아지를 animal클래스에서 생성해서 c객체를 만들고
c.bark('멍멍') #c객체로 .bark메소드를 사용하면서 인자로 '멍멍'을 줌. 그럼 bark메소드가 실행되면서
              # print문이 실행됨