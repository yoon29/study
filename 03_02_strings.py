# https://wikidocs.net/20623
'''
02. Python Strings
1. 문자열이란?
문자열(String)이란 문자와 단어 등으로 구성된 문자들의 집합을 의미합니다.
다른 많은 인기있는 프로그래밍 언어와 마찬가지로 Python의 문자열은 유니 코드 문자를 나타내는 바이트 배열입니다. 그러나 파이썬에는 문자 데이터 유형이 없으며 단일 문자는 길이가 1 인 문자열입니다.
숫자도 따옴표안에 있으면 문자열 입니다.
파이썬의 문자열 리터럴은 작은 따옴표 또는 큰 따옴표로 묶습니다.
다른 방법으로는 작은 따옴표 또는 큰 따옴표 세개를 연달아 입력하는 방법이 있습니다.
다음은 모두 문자열 입니다.

'Python String! 한글 1234 !@#$%^'
"Python String! 한글 1234 !@#$%^"
'''Python String! 한글 1234 !@#$%^'''
"""Python String! 한글 1234 !@#$%^"""
'''

########################################################################################################################

'''
2. 문자열 만드는 방법
파이썬에서는 문자열을 사용할 때 주로 작은따옴표를 사용합니다. 물론 " "(큰따옴표)로도 문자열을 사용할 수도 있습니다. 문자열을 만들어 바로 출력할 수도 있지만 가공하거나 여러가지 작업을 하기 위해서는 변수에 저장하여 처리합니다.

str1 = 'Hello Python!!!'
str2 = "Hello Python!!!"
str3 = '''Hello Python!!!'''
str4 = """Hello Python!!!"""
그런데 문자열을 만드는 방법이 왜 이렇게 많을까요?
문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때 다른 언어들은 다음과 같이 확장문자열을 이용해야 합니다. 하지만 Python은 문자열을 만드는 여러 방법이 있으므로 편리하게 만들 수 있습니다.

# 문자열 안에 따옴표 자체를 포함하는 방법
str5 = 'Python String! "한글" 1234 !@#$%^'
str6 = 'Python String! \'한글\' 1234 !@#$%^'
str7 = "Python String! '한글' 1234 !@#$%^"
str8 = "Python String! \"한글\" 1234 !@#$%^"
Python은 기본 확장 문자(escape sequence)를 지원합니다. 확장문자의 사용은 표준 출력 부분을 참조하시기 바랍니다.

Ex05_string1.py
'''

# 파이선 문자열
str1 = 'Python String! 한글 1234 !@#$%^'
str2 = "Python String! 한글 1234 !@#$%^"
str3 = '''Python String! 한글 1234 !@#$%^'''
str4 = """Python String! 한글 1234 !@#$%^"""
print(str1, str2, str3, str4, sep="\n")

# 문자열 안에 따옴표 자체를 포함하는 방법
str5 = 'Python String! "한글" 1234 !@#$%^'
str6 = 'Python String! \'한글\' 1234 !@#$%^'
str7 = "Python String! '한글' 1234 !@#$%^"
str8 = "Python String! \"한글\" 1234 !@#$%^"
print(str5, str6, str7, str8, sep="\n")
'''
실행 결과

Python String! 한글 1234 !@#$%^
Python String! 한글 1234 !@#$%^
Python String! 한글 1234 !@#$%^
Python String! 한글 1234 !@#$%^
Python String! "한글" 1234 !@#$%^
Python String! '한글' 1234 !@#$%^
Python String! '한글' 1234 !@#$%^
Python String! "한글" 1234 !@#$%^
다른 이유로는 여러 줄의 문자열을 입력하고 싶을때 입니다.

Ex06_string2.py
'''

# 파이선 문자열
str1 = '첫번째 줄 두번째 줄 세번째 줄'
str2 = '첫번째 줄\n두번째 줄\n세번째 줄\n'
str3 = '''첫번째 줄
두번째 줄
세번째 줄
'''
str4 = """첫번째 줄
두번째 줄
세번째 줄
"""
str5 = "첫번째 줄 " +  \
       "두번째 줄 " + \
       "세번째 줄"
print(str1, str2, str3, str4, sep="\n")
print(str5)
'''
실행 결과

첫번째 줄 두번째 줄 세번째 줄
첫번째 줄
두번째 줄
세번째 줄

첫번째 줄
두번째 줄
세번째 줄

첫번째 줄
두번째 줄
세번째 줄

첫번째 줄 두번째 줄 세번째 줄
여러 줄을 입력할때 기본 확장 문자(escape sequence)을 사용하는것 보다 작은 따옴표 또는 큰 따옴표 세개를 연달아 입력하는 방법이 편리 합니다.
마지막의 str5는 여러 줄로 나누어 입력했지만 1줄입니다.

'''

########################################################################################################################

'''
3. 파이썬 문서 문자열
Docstring이란 무엇입니까? 파이썬 문서화 문자열 (또는 문서화 문자열)은 파이썬 모듈, 함수, 클래스 및 메소드와 문자열을 연결시키는 것을 말합니다.

작성하는 모듈, 함수, 클래스 및 메소드의 첫번째 줄에 개체의 정의에 포함시킵니다. 주석과 같지만 소스 코드에서 문서화하기 위해 사용됩니다. 모든 함수에는 docstring이 있어야합니다.

Docstring은 객체의 doc 속성과 help명령을 통해 액세스 할 수 있습니다.

작은 따옴표 또는 큰 따옴표 세개를 연달아 입력하는 방법으로 Docstring을 지정합니다. 권장사항으로 큰따옴표 세개를 사용합니다.

Ex07_string3.py
'''

# 파이선 문자열
def show1(message):
    '''
    메시지를 출력해주는 함수
    형식) show1(message)
    '''
    print(message)


def show2(message='Hello Python!!'):
    """
    메시지를 출력해주는 함수
    형식) show2(message='Hello Python!!')
    """
    print(message)


print(show1.__doc__)
print('-' * 50)

help(show1)
print('*' * 50)

print(show2.__doc__)
print('*' * 50)

help(show2)
print('*' * 50)

show1("반갑습니다. 파이썬!!!")
show2()
'''
실행 결과

    메시지를 출력해주는 함수
    형식) show1(message)

--------------------------------------------------
Help on function show1 in module __main__:

show1(message)
    메시지를 출력해주는 함수
    형식) show1(message)

**************************************************

    메시지를 출력해주는 함수
    형식) show2(message='Hello Python!!')

**************************************************
Help on function show2 in module __main__:

show2(message='Hello Python!!')
    메시지를 출력해주는 함수
    형식) show2(message='Hello Python!!')

**************************************************
반갑습니다. 파이썬!!!
Hello Python!!
'''

########################################################################################################################

'''
4. 간단한 문자열 처리 함수들
문자열을 다루는 방법은 세번째 계단에서 자세하게 다루도록 하겠습니다. 여기서는 간단하게 몇가지 자주 사용되는 몇가지 정보만 알아보도록 하겠습니다.

문자열 길이 구하기
len(문자열)
문자열의 길이를 구해줍니다. 한글, 공백, 특수문자도 1글자로 인식합니다.
참고로 파이썬 3에서 len은 문자의 개수를 구해주지만 파이썬 2.7에서는 실제 바이트 수를 구해주는 차이점이 있습니다. 즉, 한글 문자열의 길이를 구할 때 파이썬 버전에 따라 결과가 다르므로 주의해야 합니다.

문자열 연결과 반복하기
문자열1 + 문자열2
문자열 * 정수
+ 연산자를 이용하여 문자열을 더합니다.
문자열에 정수를 곱하면 동일한 문자열을 정수만큼 반복합니다. 문자열과 숫자를 + 연산자로 결합하면 아래와 같은 에러가 발생합니다. 이때는 숫자를 문자열로 변경해주는 str()함수를 사용해야 합니다.

Traceback (most recent call last):
  File "..../Ex08_string4.py", line 16, in <module>
    print("'" + str1 + "'의 길이는 " + len(str1) + "입니다.")
TypeError: must be str, not int
문자열 잘라내기
문자열[n:m]
[n] : 1글자 잘라내기
[n:m] : n부터 m-1까지 문자열을 리턴합니다.
[:m] : 앞의 숫자를 생략하면 0부터 시작합니다.
[n:] : 뒤의 숫자를 생략하면 끝 글자까지 입니다.
[:] : 모두 생략하면 전체입니다.
[-n] : 음수 값을 지정하면 뒤에서부터 카운팅합니다.

앞뒤 공백없애기
문자열.strip() , 문자열.lstrip(), 문자열.rstrip
strip() : 앞, 뒤 공백을 모두 없앱니다.
lstrip() : 왼쪽 공백을 없앱니다.
rstrip() : 오른쪽 공백을 없앱니다.

문자 개수세기
문자열.count(문자열)
문자열에서 지정 문자열의 개수를 세어 줍니다.

간단한 예제
Ex08_string4.py
'''

# 파이선 문자열
str1 = "Hello Python!!"
str2 = "반갑다 파이썬!!"

# 문자열 길이
print(str1, "의길이", len(str1))  # 14
print(str2, "의길이", len(str2))  # 9 : 한글도 1글자로 인식

# 문자열 연결하기
str3 = str1 + str2
str4 = "^" * 10

print(str3)
print(str4)

# 문자열과 숫자형의 결합
# print("'" + str1 + "'의 길이는 " + len(str1) + "입니다.")
print("'" + str1 + "'의 길이는 " + str(len(str1)) + "입니다.")

# 문자열 잘라내기
print(str1[0], str1[6])  # 1글자 잘라내기
print(str1[3:7])  # [n:m] : n부터 m-1까지 문자열을 리턴합니다.
print(str1[:5])   # 앞의 숫자를 생략하면 0부터 입니다.
print(str1[6:])   # 뒤의 숫자를 생략하면 끝 글자까지 입니다.
print(str1[:])    # 모두 생략하면 전체입니다.
print(str1[:-2])  # 음수 값을 지정하면 뒤에서부터 카운팅합니다.

# 앞뒤 공백 없애기
str5 = "  앞 뒤에 공백이 있습니다.  "
print('[', str5, ']',sep='')
print('[', str5.lstrip(), ']',sep='')
print('[', str5.rstrip(), ']',sep='')
print('[', str5.strip(), ']',sep='')

print('"', str5,'"', '의 공백의 개수는 ', str5.count(' '), '개입니다.', sep='')
print('"', str1, '"', '의 ll의 개수는 ', str1.count('ll'), '개입니다.', sep='')
'''
실행 결과

Hello Python!! 의길이 14
반갑다 파이썬!! 의길이 9
Hello Python!!반갑다 파이썬!!
^^^^^^^^^^
'Hello Python!!'의 길이는 14입니다.
H P
lo P
Hello
Python!!
Hello Python!!
Hello Python
[  앞 뒤에 공백이 있습니다.  ]
[앞 뒤에 공백이 있습니다.  ]
[  앞 뒤에 공백이 있습니다.]
[앞 뒤에 공백이 있습니다.]
"  앞 뒤에 공백이 있습니다.  "의 공백의 개수는 7개입니다.
"Hello Python!!"의 ll의 개수는 1개입니다.
'''
'''
대, 소문자 바꾸기
문자열.upper(), 문자열.lower()
문자열을 대문자 또는 소문자로 바꿔줍니다.

문자열 찾기
문자열.find(문자열)
문자열.index(문자열)
두개의 차이점은 find()는 없으면 -1을 리턴하고 index()는 에러를 발생합니다.

문자열 바꾸기
문자열.replace('원본문자열', '바뀔문자열',개수=None)

※ Python에서 문자열은 불변객체입니다.
자신이 변경되는것이 아니라 항상 새로운 객체를 만들어 리턴합니다.
변경을 하려고하면 다음과 같이 에러를 발생합니다.

str1[0] = 'H' # 에러 : 불변객체

TypeError: 'str' object does not support item assignment
문자열 나누기, 합치기
문자열 나누기 : 문자열.split(self, sep=None, maxsplit=-1)
문자열 합치기 : 문자열.join(self, iterable)

간단한 예제
Ex09_string5.py
'''

str1 = "hello python!!"
print(str1)
print(str1.lower())
print(str1.upper())
print(str1[0].upper())
print(str1.find(' '))
print(str1[0].upper() + str1[1:str1.find(' ')])
print(str1[str1.find(' ')+1].upper())
print(str1[str1.find(' ')+2:])

# 단어의 첫글자만 대문자로 바꾸기
print(str1[0].upper() + str1[1:str1.find(' ')] + ' ' +
      str1[str1.find(' ')+1].upper() + str1[str1.find(' ')+2:])

print(str1[0].upper() + str1[1:str1.index(' ')] + ' ' +
      str1[str1.index(' ')+1].upper() + str1[str1.index(' ')+2:])
print(str1.capitalize())
print('-' * 50)

print(str1.replace('python', 'world'))
print(str1)  # 원본 변경 않됨
print(str1.replace('!', '^-^', 1))  # 세번째 인수는 개수
print('-' * 50)

# str1[0] = 'H' # 에러 : 불변객체

str2 = "한놈 두식이 석삼 너구리 오징어"
str3 = str2.split()
print(str2, type(str2))
print(str3, type(str3))

str4 = "한놈, 두식이, 석삼, 너구리, 오징어"
str5 = str4.split(", ")
print(str4, type(str4))
print(str5, type(str5))

str6 = ","
print(str6.join(str3))
str6 = "|"
print(str6.join(str5))
'''
실행 결과

hello python!!
hello python!!
HELLO PYTHON!!
H
5
Hello
P
ython!!
Hello Python!!
Hello Python!!
Hello python!!
--------------------------------------------------
hello world!!
hello python!!
hello python^-^!
--------------------------------------------------
한놈 두식이 석삼 너구리 오징어 <class 'str'>
['한놈', '두식이', '석삼', '너구리', '오징어'] <class 'list'>
한놈, 두식이, 석삼, 너구리, 오징어 <class 'str'>
['한놈', '두식이', '석삼', '너구리', '오징어'] <class 'list'>
한놈,두식이,석삼,너구리,오징어
한놈|두식이|석삼|너구리|오징어
'''
'''
간단한 변환함수
ord : 문자의 아스키 코드값을 리턴하는 함수
hex : hex(x)는 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수
otc : oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴하는 함수
chr : 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자를 리턴하는 함수
capitalize : 단어의 첫글자만 대문자로 변환하는 함수

간단한 예제
Ex10_string6.py
'''

# 파이선 문자열
# ord : 문자의 아스키 코드값을 리턴하는 함수
# hex : hex(x)는 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수
# otc : oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴하는 함수이다.
print(ord("A"))       # 출력 결과: 65
print(hex(ord("A")))  # 출력 결과: 0x41
print(oct(ord("A")))  # 출력 결과: 0o101

# chr : 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자를 리턴하는 함수
print(chr(65))        # 출력 결과: A
print(chr(0x41))      # 출력 결과: A

# 대소문자 변환
print(chr(ord('A')+32))  # 출력 결과: a
print(chr(ord('Z')+32))  # 출력 결과: z
print(chr(ord('a')-32))  # 출력 결과: A
print(chr(ord('z')-32))  # 출력 결과: Z

# 1자리 숫자 문자열을 숫자로 변환
print(ord('1') - ord('0'), type(ord('1') - ord('0')))
print(ord('9') - ord('0'), type(ord('9') - ord('0')))

# 1자리 숫자를 숫자 문자열로 변환
print(chr(1 + ord('0')), type(chr(1 + ord('0'))))
print(chr(9 + ord('0')), type(chr(9 + ord('0'))))
'''
실행 결과

65
0x41
0o101
A
A
a
z
A
Z
1 <class 'int'>
9 <class 'int'>
1 <class 'str'>
9 <class 'str'>
'''


