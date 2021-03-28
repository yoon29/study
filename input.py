### 03. Python(파이썬) 표준 입력 ###

# 표준 입력
# input함수의 도움말을 확인해 보자
help(input)
'''
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
'''
'''
input() : 표준 입력장치(키보드)로 부터 문자열을 입력 받습니다.
input('문자열') : 문자열을 출력하고 표준 입력장치(키보드)로 부터 문자열을 입력 받습니다.
입력된 값은 문자열 입니다.
사용자가 EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return)을 입력하면 EOFError를 발생시킵니다.
'''

########################################################################################################################

# 표준 입력
print('이름을 입력하세요', end="")
name = input();
print("이름 : {0}, type : {1}".format(name,type(name)))
name = input('이름을 입력하세요 ');
print("이름 : {0}, type : {1}".format(name,type(name)))
name = input('아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요');
'''
이름을 입력하세요 한사람
이름 : 한사람, type : <class 'str'>
이름을 입력하세요 두사람
이름 : 두사람, type : <class 'str'>
아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요^D
Traceback (most recent call last):
  File "C:/PyThonProjects/Ex01/basic03/Ex13_input1.py", line 7, in <module>
    name = input('아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요');
EOFError: EOF when reading a line
'''
########################################################################################################################

'''
2. 정수 입력
기본적으로 input함수는 문자열로 입력됩니다.
그래서 입력받은 값을 정수형으로 변환해서 사용해야 합니다.

eval() 함수 : 인수를 유효한 파이썬 표현식으로 리턴 합니다.
int() 클래스 : class int(x=0), class int(x,base=10)
숫자나 문자열 x 로 부터 만들어진 정수 객체를 돌려줍니다.
인자가 주어지지 않으면 0 을 돌려줍니다.
base는 진법을 나타내며 주로 2, 8, 10, 16을 사용합니다. 10이 기본값입니다.
'''
# 표준 입력
data = input("정수를 입력하시오 : ")
print(data, type(data))
# print(data, type(data), data + 1) 에러 문자열과 정수를 +(더하기)할 수 없습니다.

data = eval(input("정수를 입력하시오 : "))
print(data, type(data), data + 1)

data = int(input("정수를 입력하시오 : "))
print(data, type(data), data + 1)

data = int(input("2진수를 입력하시오 : "), 2)
print(data, type(data), data + 1)

data = int(input("8진수를 입력하시오 : "), 8)
print(data, type(data), data + 1)

data = int(input("10진수를 입력하시오 : "), 10)
print(data, type(data), data + 1)

data = int(input("16진수를 입력하시오 : "), 16)
print(data, type(data), data + 1)
'''
정수를 입력하시오 : 1
1 <class 'str'>
정수를 입력하시오 : 2
2 <class 'int'> 3
정수를 입력하시오 : 3
3 <class 'int'> 4
2진수를 입력하시오 : 1010
10 <class 'int'> 11
8진수를 입력하시오 : 10
8 <class 'int'> 9
10진수를 입력하시오 : 10
10 <class 'int'> 11
16진수를 입력하시오 : 1a
26 <class 'int'> 27
'''

########################################################################################################################

'''
3. 실수 입력
기본적으로 input함수는 문자열로 입력됩니다.
그래서 입력받은 값을 실수형으로 변환해서 사용해야 합니다.

eval() 함수 : 인수를 유효한 파이썬 표현식으로 리턴 합니다.
float() 클래스 : class float(x)
숫자나 문자열 x 로 부터 만들어진 실수 객체를 돌려줍니다.
인자가 주어지지 않으면 0 을 돌려줍니다.
'''
# 표준 입력
data = input("실수를 입력하시오 : ")
print(data, type(data))
# 에러 문자열과 실수를 +(더하기)할 수 없습니다.
# print(data, type(data), data + 1.2)

data = eval(input("실수를 입력하시오 : "))
print(data, type(data), data + 1.2)

data = float(input("정수를 입력하시오 : "))
print(data, type(data), data + 1.2)
'''
실수를 입력하시오 : 3.14
3.14 <class 'str'>
실수를 입력하시오 : 3.14
3.14 <class 'float'> 4.34
정수를 입력하시오 : 3.14
3.14 <class 'float'> 4.34
'''

########################################################################################################################

'''
4. 튜플(tuple), 리스트(list)로 입력받기
기본적으로 input함수는 문자열로 입력됩니다.

eval() 함수 : 인수를 유효한 파이썬 표현식으로 리턴 합니다.
'''
# 표준 입력
string = input("(1,2) 처럼입력하시오 ")
print(string, type(string))

string = eval( input("(1,2) 처럼입력하시오 "))
print(string, type(string))

string = input("[1,2,3,4,5,6] 처럼입력하시오 ")
print(string, type(string))

string = eval( input("[1,2,3,4,5,6] 처럼입력하시오 "))
print(string, type(string))
'''
(1,2) 처럼입력하시오 (1,2)
(1,2) <class 'str'>
(1,2) 처럼입력하시오 (1,2)
(1, 2) <class 'tuple'>
[1,2,3,4,5,6] 처럼입력하시오 [1,2,3]
[1,2,3] <class 'str'>
[1,2,3,4,5,6] 처럼입력하시오 [1,2,3]
[1, 2, 3] <class 'list'>
'''

########################################################################################################################






