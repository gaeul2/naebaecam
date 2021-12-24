# 직사각형 생성 클래스
class Rectangle:
    def __init__(self, width, length):
        self.width = width #가로
        self.length = length #세로

    def Area(self): #넓이
        return self.width * self.length
    # 리턴값에 바로 식을 적어도 됨.

    def Dul(self): #둘레
        return (self.width + self.length) * 2


a1 = Rectangle(4,5)# 인자를 가로4, 세로5 준것
print('a1의 넓이는',a1.Area(),'입니다')
print('a1의 둘레는',a1.Dul(),'입니다')
# 객체로 메소드 사용할때 객체.메소드 이렇게사용
a2 = Rectangle(10,7)# 인자를 가로10,세로7준것
print('a2의 넓이는',a2.Area(),'입니다')
print('a2의 둘레는',a2.Dul(),'입니다')