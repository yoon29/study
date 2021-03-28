'''
01. Python Numbers
숫자로 이루어진 자료형을 말합니다.
정수형, 실수형, 복소수형이 있습니다.
'''

########################################################################################################################

'''
1. 정수형
양의 정수, 0, 음의 정수를 말합니다. 소수이하 값이 없는 자료형입니다.
파이썬에서 정수의 값은 비트 수에 의해 제한되지 않고 사용 가능한 메모리의 한계까지 확장 될 수 있습니다 . 따라서 큰 수를 저장하기위한 특별한 배열을 필요로하지 않습니다.
Ex01_number1.py
'''

# 정수형 : class 'int'
import sys

number1 = 127
number2 = 0
number3 = -128
print(number1, type(number1))
print(number2, type(number2))
print(number3, type(number3))

bin = 0b10  # 2진수
oct = 0o10  # 8진수
dec = 10    # 10진수
hex = 0x10  # 16진수
print(bin, type(bin))
print(oct, type(oct))
print(dec, type(dec))
print(hex, type(hex))

max = sys.maxsize
min = -max-1
print(max, type(max))
print(min, type(min))

print(max+1, type(max+1))
print(10**40, type(10**40))
# print(10**100, type(10**100))
x = 10000000000000000000000000000000000000000000;
x = x + 1
print(x)
'''
실행 결과

127 <class 'int'>
0 <class 'int'>
-128 <class 'int'>
2 <class 'int'>
8 <class 'int'>
10 <class 'int'>
16 <class 'int'>
9223372036854775807 <class 'int'>
-9223372036854775808 <class 'int'>
9223372036854775808 <class 'int'>
10000000000000000000000000000000000000000 <class 'int'>
10000000000000000000000000000000000000000001
'''

########################################################################################################################

'''
2. 실수형
실수형(Floating)은 소수점이 포함된 숫자를 말합니다.
부동 소수점 숫자는 소수점 이하 15 자리까지 정확합니다.
정수 및 부동 소수점은 소수점으로 구분됩니다. 1정수, 1.0부동 소수점 숫자입니다.
Ex02_number2.py
'''

# 실수형 : class 'float'
float_number1 = 123.456
float_number2 = -123.456
print(float_number1, type(float_number1))
print(float_number2, type(float_number2))

float_number3 = 123.e2
float_number4 = -123.456e-3
print(float_number3, type(float_number3))
print(float_number4, type(float_number4))

float_number5 = 10/3
float_number6 = 1.123456789012345678901234567890
print(float_number5, type(float_number5))
print(float_number6, type(float_number6))
'''
실행 결과

123.456 <class 'float'>
-123.456 <class 'float'>
12300.0 <class 'float'>
-0.123456 <class 'float'>
3.3333333333333335 <class 'float'>
1.1234567890123457 <class 'float'>
'''

########################################################################################################################

'''
3. 복소수형
x + yj 처럼 복소수 형태로 쓰여집니다. i가 아니라 j입니다.
x 는 실수 부분이고 y 는 허수 부분입니다.
실수부와 허수부를 따로 분리가 가능합니다.
복소수끼리의 연산도 지원 합니다.
Ex03_number3.py
'''

# 복소수형 : class 'complex'
complex_number1 = 1.2 + 3.4j
complex_number2 = 5.6 - 7.8j

print(complex_number1, type(complex_number1))
print(complex_number2, type(complex_number2))

complex_number3 = complex_number1 + complex_number2
complex_number4 = complex_number1 - complex_number2
complex_number5 = complex_number1 * complex_number2
complex_number6 = complex_number1 / complex_number2

print(complex_number3, type(complex_number3))
print(complex_number4, type(complex_number4))
print(complex_number5, type(complex_number5))
print(complex_number6, type(complex_number6))

print(complex_number1.real, complex_number1.imag)
print(complex_number2.real, complex_number2.imag)
'''
실행 결과

(1.2+3.4j) <class 'complex'>
(5.6-7.8j) <class 'complex'>
(6.8-4.4j) <class 'complex'>
(-4.3999999999999995+11.2j) <class 'complex'>
(33.24+9.68j) <class 'complex'>
(-0.21475054229934923+0.3080260303687635j) <class 'complex'>
1.2 3.4
5.6 -7.8
'''

########################################################################################################################

'''
4. 출력형식 지정
Ex04_number4.py
'''

# 형식화된 출력
# 출력만
number = 12345
print("{0:,}".format(number))

# 문자열로 변경
numberString = format(number, ',')
print(numberString)

# format 함수 사용
# format(데이터,"출력형식")
# 출력 형식은 표준 입출력의 출력 부분을 참조하세요
print(format(1234567890.56789, ",")) # 3자리마다 , 추가
print(format(1234567890.56789, "E")) # 지수로 표현
print(format(123, "x")) # 16진수로 표현
print(format(123, "o")) # 8진수로 표현
print(format(123, "b")) # 2진수로 표현
print(format(12345.56789, ">-12,.2f"))
print(format(12345.56789, "^-012,.2f"))
print(format(12345.56789, "<-012,.2f"))
print(format(12345.56789, "@>12,.2f"))
print(format(-12345.56789, "12,.2f"))
print(format(-12345.56789, "-12,.2f"))
print(format(12345.56789, "+12,.2f"))
print(format(0.1234, ".1%"))
'''
실행 결과

12,345
12,345
1,234,567,890.56789
1.234568E+09
7b
173
1111011
   12,345.57
012,345.5700
12,345.57000
@@@12,345.57
  -12,345.57
  -12,345.57
  +12,345.57
12.3%
'''



