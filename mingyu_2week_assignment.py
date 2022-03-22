# 문제 1번
from xml.sax import SAXNotRecognizedException


def sum(a,b):
    sum = a+b
    return sum

# 문제 2번
def sub(a,b):
    sub = a-b
    return sub

# 문제 3번
def mul(a,b):
    mul = a*b
    return mul

# 문제 4번
def div(a,b):
    div = a/b
    return div

# 문제 5번
def distance(x1,y1,x2,y2):
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    return distance

# 문제 6번
def short():
    lylic = "life is short art is long"
    slice = lylic[8:14]
    return slice

# 문제 7번
def myReverse(string):
    string = string[::-1]
    return string

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오: ")
    hobby = input("취미를 입력하시오: ")
    uni = input("재학 중인 대학을 입력하시오: ")
    birth = input("생일을 입력하시오(예시 : 981128): ")
    hi = "제 이름은 %s입니다. 제 취미는 %s이구요. 저는 %s를 다니고 있습니다. 제 생일은 %d월 %d일 입니다." %(name, hobby, uni, int(birth[2:4]), int(birth[4:]))
    return hi 

# 문제 9번
def calcAI():
    first = input("첫 번째 숫자를 입력하시오: ")
    second = input("두 번째 숫자를 입력하시오: ")
    a = int(first) + int(second)
    b = "두 수의 합은 %d입니다." %(a)
    return b
