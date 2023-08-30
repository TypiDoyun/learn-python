class Human:
    def __init__(self, name, height):
        
        self.name = name
        
        self.height = height
    
    def sayHello(self):
        print(f"안녕하세요 제 이름은 {self.name}이며, 키는 {self.height}cm입니다.")

class Doyun(Human):
    def __init__(self, name, height):
        self.name = name
        self.height = height


doyun = Doyun("김도윤", "180")

doyun.sayHello()