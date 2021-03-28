### 02. Python(파이썬) 표준 출력 ###

#  출력에 대하여 알아보자
# print함수의 도움말을 확인해 보자
help(print)
'''
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''


print("hello World")
print( 1/2 )
print( type(1/2) )
print( type('hello') )
print( type(u'hello') )
print( 2**30 )
print( type(2**30) )
print( 2**100 )
print( type(2**100) )
print('-' * 40)

print("하나","둘","셋",1,2,3)
print("하나","둘","셋",1,2,3,sep='-')
print("첫번째 값")
print("두번째 값") # 다른 줄에 출력
print("첫번째 값", end=" ---> ")
print("두번째 값") # 같은 줄에 출력
# 출력 방향 변경
file = open("test.txt","w")
print("Hello Python!!", file=file) # 파일로 출력
file.close()
print('-' * 40)

print('Hello World!!')
print("Hello World!!")
print("나의 이름은 '한사람'입니다.")
print('나의 이름은 "한사람"입니다.')
print("나의 이름은 \"한사람\"입니다.")
print('나의 이름은 \'한사람\'입니다.')
print('-' * 40)

print('Hello \tWorld!!')
print("Hello \nWorld!!")
print("나의 이름은 \"한사람\"입니다.")
print('나의 이름은 \'한사람\'입니다.')
print('-' * 40)
print('1 \n')
print('2 \012')
print('3 \x0A')
print('-' * 40)
print('n')
print('\156')
print('\x6E')
print('-' * 40)

# Unicode 명으로 escape
unicode_a = '\N{LATIN SMALL LETTER A}'
print(unicode_a)
# Unicode 명으로 escape
unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
print('-' * 40)



# 형식에 맞추어 출력하기

# 이전 방식
print('나의 이름은 %s입니다'%('한사람'))
print('나의 이름은 "%s"입니다. 나이는 %d세이고 성별은 %s입니다.'%('한사람',33,'남성'))
print('나이는 %d세이고 성별은 %s입니다. 나의 이름은 "%s"입니다. '%(33,'남성','한사람'))
print('나이는 %03d세이고 신장은 %6.2f입니다. 나의 이름은 "%s"입니다. '%(33,56.789,'한사람'))
print('-' * 40)

# 파이썬(Python) 3 포맷팅 방식
print('나의 이름은 {}입니다'.format('한사람'))
print('나의 이름은 "{0}"입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('한사람',33,'남성'))
print('나이는 {1}세이고 성별은 {2}입니다. 나의 이름은 "{0}"입니다. '.format('한사람',33,'남성'))
print('나이는 {age}세이고 성별은 {gender}입니다. 나의 이름은 "{name}"입니다. '
         .format(name='한사람',age=33,gender='남성'))
print('만세삼창 :  {0}!!! {0}!!! {0}!!! '.format('만세'))
print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7))
print('-' * 40)

#  앞의 빈칸 0으로 채우기
print('12'.zfill(5))
print('-12'.zfill(5))
print('3.141'.zfill(7))
print('-3.141'.zfill(7))
print('3.14159265359'.zfill(5))
print('-3.14159265359'.zfill(5))
print('문자열'.zfill(10))
print('문자열'.zfill(1))
print('-' * 40)

# 6. 길이와 정렬
# {:길이} : 출력할 데이터의 길이를 지정합니다. 문자열(왼쪽 정렬), 숫자(오른쪽 정렬)
# {:<길이} : 왼쪽 정렬
# {:>길이} : 오른쪽 정렬
# {:^길이} : 가운데 정렬

print('Python is [{:15}]'.format('good'))
print('Python is [{:<15}]'.format('good'))
print('Python is [{:>15}]'.format('good'))
print('Python is [{:^15}]'.format('good'))
print('당신의 나이는 [{:15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('당신의 나이는 [{:>15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('-' * 40)


# 왼쪽 정렬
for x in range(1, 4):
    print('[{0:2d}] [{1:3d}] [{2:4d}]'.format(x, x*x, x*x*x))
print()
# 가운데 정렬
for x in range(1, 4):
    print('[{0:^2d}] [{1:^3d}] [{2:^4d}]'.format(x, x*x, x*x*x))
print()
# 오른쪽 정렬
for x in range(1, 4):
    print('[{0:<2d}] [{1:<3d}] [{2:<4d}]'.format(x, x*x, x*x*x))
print()
# 0으로 채우기
for x in range(1, 4):
    print('[{0:02d}] [{1:03d}] [{2:04d}]'.format(x, x*x, x*x*x))
print()
# 부호 출력
print('[{0:05d}] [{1:05d}] [{2:05d}]'.format(1,-2,3))    # 음수만 부호
print('[{0:+05d}] [{1:+05d}] [{2:+05d}]'.format(1,-2,3)) # 부호
print('[{0:<5d}] [{1:<5d}] [{2:<5d}]'.format(1,-2,3))     # 정렬
print('-' * 40)


# 7. 채움문자와 숫자 표시형식
# {[인덱스]:[채움문자][정렬][길이][,|_][형식문자]
# 공백을 채움문자로 채워줍니다.
# , : 천단위 마다 콤마를 붙여줍니다.
# _ : 천단위 마다 밑줄을 붙여줍니다.
# e : 숫자를 지수 형식으로 만들어 줍니다.
# = : 숫자 형식에만 사용합니다. 부호를 항상 제일 앞에 출력합니다.
print('[{0:05d}] [{1:05d}] [{2:05d}]'.format(1,-2,3))
print('[{0:★<5d}] [{1:★<5d}] [{2:★<5d}]'.format(1,-2,3))
print('[{0:★>5d}] [{1:★>5d}] [{2:★>5d}]'.format(1,-2,3))
print('[{0:★^5d}] [{1:★^5d}] [{2:★^5d}]'.format(1,-2,3))
print('[{0:5d}] [{1:5d}] [{2:5d}]'.format(1,-2,3))
print('[{0:=5d}] [{1:=5d}] [{2:=5d}]'.format(1,-2,3))
print('[{0:=05d}] [{1:=05d}] [{2:=05d}]'.format(1,-2,3))
# 숫자 표시 형식( , _)
print('[{0:>5,}] [{1:>5,}] [{2:>5,}]'.format(11544435,-2544254,35454343))
print('[{0:>5_}] [{1:>5_}] [{2:>5_}]'.format(11544435,-2544254,35454343))
print('[{0:>5e}] [{1:>5e}] [{2:>5e}]'.format(11544435,-2544254,35454343))
print('-' * 40)


# 8. 진법과 실수 출력 형식지정
# b(2진수), o(8진수), x(16진수 소문자), X(16진수 대문자)
# {[인덱스]:[전체자릿수][.소수이하자릿수]f
print('[{0:5b}] [{1:5b}] [{2:5b}]'.format(11,-22,33))    # 2진수
print('[{0:5o}] [{1:5o}] [{2:5o}]'.format(11,-22,33))    # 8진수
print('[{0:5x}] [{1:5x}] [{2:5x}]'.format(11,-22,33))    # 16진수 소문자
print('[{0:5X}] [{1:5X}] [{2:5X}]'.format(11,-22,33))    # 16진수 대문자
print('-' * 40)

import math
print('원주율 [{0:.3f}]'.format(math.pi))
print('원주율 [{0:.7f}]'.format(math.pi))
print('원주율 [{0:10.3f}]'.format(math.pi))
print('원주율 [{0:20.7f}]'.format(math.pi))
print('원주율 [{0:0.5f}]'.format(math.pi))
print('-' * 40)


# 9. {}와 % 출력
# {}를 출력하려면 "{"과 "}"을 세번 연달아 입력해야 합니다.
# % 자체를 출력하려면 %%로 입력해야 합니다.

print('{0}씨는 상위 {1}%안에 있는 사람입니다.'.format('한사람',10))
print('{{0}}씨는 상위 {{1}}%안에 있는 사람입니다.'.format('한사람',10))
print('{{{0}}}씨는 상위 {{{1}}}%안에 있는 사람입니다.'.format('한사람',10))
print('%s씨는 상위 %d%%안에 있는 사람입니다.'%('한사람',10))
print('-' * 40)


'''
10. 출력형식 정리
    
    표준 형식 지정자의 일반적인 형식 은 다음과 같습니다.
    
    format_spec :: = [[ fill] align] [ sign] [#] [0] [ width] [ grouping_option] [. precision] [ type]
    fill :: = <모든 문자>
    align :: = "<"| ">"| "="| "^"
    sign :: = "+"| "-"| ""
    width :: = digit+ grouping_option :: = "_"| ","
    precision :: = digit+
    type :: = "b"| "c"| "d"| "e"| "E"| "f"| "F"| "g"| "G"| "n"| "o"| "s"| "x"| "X"
    
    fill(채움문자) : 어떠한 문자도 가능합니다.
    align(정렬) : <(왼쪽정렬, 문자열 기본값), >(오른쪽 정렬, 숫자 기본값), ^(가운데정렬)
    =(숫자에만 사용, '+000000120'형식으로 필드를 인쇄하는 데 사용)
    sign(부호) : +(양수도 부호 표시), -(음수에 대해서만 부호를 사용,기본값)
    width(폭) : 전체 폭을 양의 정수로 지정합니다.
    , | _ : 천단위마다 콤마(,) 또는 밑줄(_)을 붙여줍니다.
    precision(소수이하 자리수) : 소수이하 자리수를 정수로 지정합니다.
    type(형식) : 문자열(s), 정수(b, c, d, o, x, X, n), 실수(e, E, f, F, g, G, n)
'''



