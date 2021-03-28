'''
03. 변수, 상수 그리고 리터럴
1. 변수(Variable)
컴퓨터가 어떠한 일을 하기위해서는 모든 데이터는 보조기억장치(SSD,HDD,USB 등)에서 주기억 장치(RAM)로 읽혀져야만 중앙처리장치(CPU)가 주기억 장치의 내용을 읽어서 데이터를 가공처리합니다.

그런데 이 주기억 장치는 Byte마다 번지가 지정되어 있습니다. 번지는 숫자이므로 프로그램을 작성하려면 "10번지의 값을 읽어서 20번지의 값과 더하여 30번지의 값에 저장하여라" 등의 명령어를 내리게 됩니다. 프로그래머가 모든 번지를 제어하려면 힘들것입니다. 그래서 번지에 별명을 붙여 "이곳은 name이라고 하고 저곳은 score라고 하자"는 것이 변수입니다.

메모리 관리는 운영체제가 맡아서 합니다. 프로그래머가 메모리가 필요하면 변수를 선언하고 값을 할당하면 됩니다. 그러면 운영체제가 알아서 현재 사용하지 않는 메모리를 확보해서 그곳에 변수명을 할당합니다. 그 후로 프로그래머는 그 변수명을 이용하여 메모리에 접근하여 프로그램을 작성하면 됩니다.

메모리 관리원칙
메모리 관리의 주체는 운영체제입니다.
운영체제는 메모리가 있는 한은 할당 요청을 거절하지 않습니다.
한 번 할당된 메모리 공간은 절대로 다른 목적을 위해 재할당되지 않습니다.
응용 프로그램이 할당된 메모리를 해제하면 운영체제는 이 공간을 빈 영역으로 인식하고 다른 목적을 위해 사용할 수 있도록 합니다.
결론적으로 변수(Variable)는 문자나 숫자 같은 값을 담는 컨테이너입니다. 컴퓨터로 어떤한 일을 한다는 것은 필요한 데이터를 담아서 가공 처리하여 사용자가 원하는 결과를 만들어내는것 입니다. 가공처리하는 과정에 발생하는 데이터들을 어딘가에 보관해서 계속 처리를 해야 된다면 어디에 담아놓을 까요? 그래서 저장해놓는 기억 공간이 필요하게 되는데 이때 변수를 사용하는거서 입니다. 변수는 프로그램 실행 중에 변경되는 값을 일시적으로 저장하는 임시 기억장소의 별명이라고 할 수 있습니다. 변수는 항상 맨 마지막에 저장한 값만을 저장합니다. 다시말하면 변수는 값을 저장하는 그릇과 같습니다.

파이썬에서 변수 선언하기
파이썬에서 변수는 메모리 공간을 예약하기 위해 선언 할 필요가 없습니다. "변수 선언"또는 "변수 초기화"는 변수에 값을 할당 할 때 자동으로 발생합니다.

파이썬에서 변수에 값 할당하기
대입 연산자 =를 사용하여 변수에 값을 할당 할 수 있습니다 .
=(대입연산자)는 우변의 값을 좌변에 넣으라는 뜻 입니다.
'''

website = "some.com"
print(website)
website = "another.com"
print(website)
'''
some.com
another.com
'''

########################################################################################################################

a=b=c="모두같은 값"
print("a의 값 : {}".format(a))
print("b의 값 : {}".format(b))
print("c의 값 : {}".format(c))

d,e,f = "한사람",23,178.9
print("d의 값 : {}".format(d))
print("e의 값 : {}".format(e))
print("f의 값 : {}".format(f))

# 일반 언어의 경우 두 변수값 교환
g,h = 100,200
print("g의 값 : {}, h의 값 :{}".format(g,h))
t = g;
g = h;
h = t;
print("g의 값 : {}, h의 값 :{}".format(g,h))

# 파이선의 경우 두 변수값 교환
g,h = 100,200
print("g의 값 : {}, h의 값 :{}".format(g,h))
g,h = h,g
print("g의 값 : {}, h의 값 :{}".format(g,h))
'''
a의 값 : 모두같은 값
b의 값 : 모두같은 값
c의 값 : 모두같은 값
d의 값 : 한사람
e의 값 : 23
f의 값 : 178.9
g의 값 : 100, h의 값 :200
g의 값 : 200, h의 값 :100
g의 값 : 100, h의 값 :200
g의 값 : 200, h의 값 :100
'''

########################################################################################################################

'''
2. 상수(constant)
상수(constant)는 항상 똑같은 값을 저장하고 있는 곳이라 할 수 있습니다. 프로그래머나 시스템에 의해 미리 정해져있는 것으로,
복잡한 숫자의 값을 인지하기 쉬운 문자로 변경하여 사용하고자 할 때 주로 사용합니다.
'''

'''
constant1.py
PI = 3.14
GRAVITY = 9.8
'''
import constant1

print(constant1.PI)
print(constant1.GRAVITY)
constant1.PI = 3.141592 # 변경된다. 상수가 아니다.
print(constant1.PI)
'''
3.14
9.8
3.14159
'''

'''
constant2.py
class _constant2:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception('변수에 값을 할당할 수 없습니다.')
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise Exception('변수를 삭제할 수 없습니다.')

import sys
sys.modules[__name__] = _constant2()
'''
import constant2

constant2.PI = 3.14
constant2.MAX = 1000
print(constant2.PI)
print(constant2.MAX)

constant2.PI = 3.141592
constant2.MAX = 2000
print(constant2.PI)
print(constant2.MAX)
'''
3.14
Traceback (most recent call last):
1000
  File "C:/PyThonProjects/Ex01/basic04/Ex08_constant2.py", line 8, in <module>
    constant2.PI = 3.141592
  File "C:\PyThonProjects\Ex01\basic04\constant2.py", line 4, in __setattr__
    raise Exception('변수에 값을 할당할 수 없습니다.')
Exception: 변수에 값을 할당할 수 없습니다.
'''

########################################################################################################################

'''
3. 리터럴(liternal)
리터럴(liternal)은 "값" 그 자체로, 고정된 값을 표현하는 것을 의미합니다.
파이썬에는 다음과 같은 다양한 유형의 리터럴이 있습니다.
숫자 리터럴
정수 리터럴, 실수 리터럴, 복소수 리터럴 3가지가 있습니다.
정수 리터럴 : 0b로 시작하면 2진수, 0o로 시작하면 8진수 ,0~9로 시작하면 10진수, 0x로 시작하면 16진수
실수 리터럴 : 소숫점을 포함하거나 e를 포함합니다.
복소수 리터럴 : j로 끝나면 복소수의 허수를 나타냅니다.
'''

# Integer Literals
a = 0b1010 # Binary Literals
b = 100 # Decimal Literal
c = 0o310 # Octal Literal
d = 0x12c # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.512e2

# Complex Literal
x = 1.1 + 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.real, x.imag)
'''
10 100 200 300
10.5 151.2
(1.1+3.14j) 1.1 3.14
'''

########################################################################################################################

'''
문자 리터럴
문자열 리터럴은 따옴표로 묶인 일련의 문자입니다. 문자열에 대해 단일, 이중 또는 삼중 따옴표를 모두 사용할 수 있습니다. 그리고 문자 리터럴은 작은 따옴표 또는 큰 따옴표로 묶인 단일 문자입니다.
'''

# String Literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
# ※ "r"문자는 raw string으로 백슬래시 문자를 해석하지 않고 남겨두기 때문에 정규표현식과 같은 곳에 유용합니다.

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
'''
This is Python
C
This is a multiline string with more than one line code.
Ünicöde
raw \n string
'''

########################################################################################################################

'''
논리값 리터럴
논리값 리터럴은 다음 두 값 중 하나를 가질 수 있습니다. True 또는 False.
'''

# Boolean Literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
'''
x is True
y is False
a: 5
b: 10
'''

########################################################################################################################

'''
특수 리터럴
파이썬에는 특별한 리터럴이 하나가 들어 있습니다.
None. 우리는이 필드를 사용하여 생성되지 않은 필드를 지정합니다.
'''

# Special Literals
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)
'''
Available
None
'''

########################################################################################################################

'''
컬렉션 리터럴
자료형은 다음장에서 자세하게 배우게 됩니다.

[ ... ]로 감싸져 있으면 list자료형
( ... )로 감싸져 있으면 tuple자료형
{ 키:값, ... }로 감싸져 있으면 dictionary자료형
{ ... }로 감싸져 있으면 set자료형
'''

# Literal Collections
fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

'''
['apple', 'mango', 'orange']
(1, 2, 3)
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
{'a', 'e', 'u', 'o', 'i'}
'''


