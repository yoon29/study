# https://wikidocs.net/20624
'''
03. Python Tuple
1. tuple이란?
tuple 자료형은 데이터의 목록이라고 보면 됩니다.
콤마(,)로 데이터를 나열하면 tuple입니다.
괄호()안에 ,로 나열해도 tuple입니다.
길이 1개짜리 tuple을 만들려면 반드시 뒤에 콤마(,)를 붙여야 합니다.
tuple은 다른 자료형들로 만들 수 있습니다.
tuple은 tuple을 가질 수 있습니다.
Ex11_tuple1.py
'''

# tuple 자료형이란?
# tuple 만들기
tuple1 = 1, 2, 3, 4, 5
tuple2 = (6, 7, 8, 9, 10)
print(tuple1, type(tuple1))
print(tuple2, type(tuple2))

# 다음은 tuple이 아닙니다.
tuple3 = 1
tuple4 = (6)
print(tuple3, type(tuple3))
print(tuple4, type(tuple4))

# 다음은 tuple입니다.
tuple3 = 1,
tuple4 = (6,)
print(tuple3, type(tuple3))
print(tuple4, type(tuple4))

# 다른 자료형들의 모임
tuple5 = '한놈', 123, True
print(tuple5, type(tuple5))

# tuple이 tuple을 가짐
tuple6 = '회원목록', ('한놈','두식이'),(33,25), (True, False)
print(tuple6, type(tuple6))

'''
실행 결과

(1, 2, 3, 4, 5) <class 'tuple'>
(6, 7, 8, 9, 10) <class 'tuple'>
1 <class 'int'>
6 <class 'int'>
(1,) <class 'tuple'>
(6,) <class 'tuple'>
('한놈', 123, True) <class 'tuple'>
('회원목록', ('한놈', '두식이'), (33, 25), (True, False)) <class 'tuple'>
'''

########################################################################################################################

'''
2. tuple에 접근하기
len(tuple)로 요소의 개수를 알아낼 수 있습니다.
[n:m]으로 요소에 접근이 가능합니다. 사용법은 문자열과 동일합니다.
반복문을 이용하여 접근이 가능합니다.
+연산을 이용하여 결합이 가능합니다.
*연산을 이용하여 반복할 수 있습니다.
Ex12_tuple2.py
'''

# tuple 자료형이란?
tuple1 = 1, 2, 3
print(tuple1, type(tuple1))
print('*' * 50)

print("개수 : " + str(len(tuple1)))
print('*' * 50)

print(tuple1[0], tuple1[1],tuple1[2],tuple1[-1], type(tuple1[0]))
print(tuple1[0:1],type(tuple1[0:1]))
print(tuple1[1:3],type(tuple1[0:1]))
print('*' * 50)

for data in tuple1:
    print(data)
print('*' * 50)

tuple5 = '회원목록', ('한놈','두식이'), (33, 25), (True, False)
print(tuple5, type(tuple5))
print(tuple5[0])
title = ('', '이름', '나이', '성별')
for i in (1, 2, 3):
    print('[', title[i], ']')
    for j in (0, 1):
        print(tuple5[i][j])
    print('-' * 30)

print('*' * 50)
tuple2 = ('a', 'b', 'c', 'd')
tuple3 = tuple1 + tuple2
tuple4 = tuple2 * 3
print(tuple2)
print(tuple3)
print(tuple4)
'''
실행 결과

(1, 2, 3) <class 'tuple'>
**************************************************
개수 : 3
**************************************************
1 2 3 3 <class 'int'>
(1,) <class 'tuple'>
(2, 3) <class 'tuple'>
**************************************************
1
2
3
**************************************************
('회원목록', ('한놈', '두식이'), (33, 25), (True, False)) <class 'tuple'>
회원목록
[ 이름 ]
한놈
두식이
------------------------------
[ 나이 ]
33
25
------------------------------
[ 성별 ]
True
False
------------------------------
**************************************************
('a', 'b', 'c', 'd')
(1, 2, 3, 'a', 'b', 'c', 'd')
('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')
'''

########################################################################################################################

'''
3. tuple은 불변 객체
tuple의 요소 값 변경이 불가합니다.
tuple의 요소 삭제가 불가합니다.
값을 변경하면 다음과 같은 에러가 발생 합니다.

Traceback (most recent call last):
  File "..../Ex13_tuple3.py", line 7, in <module>
    tuple1[0] = 'A'
TypeError: 'tuple' object does not support item assignment
값을 삭제하면 다음과 같은 에러가 발생합니다.

Traceback (most recent call last):
  File "..../Ex13_tuple3.py", line 10, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
그러므로 다음과 같이 새로운 tuple을 생성해서 대입하여야 합니다.

Ex13_tuple2.py
'''

# Tuple 자료형이란?
# Tuple은 불변 객체
tuple1 = 1, 2, 3, 4
print(tuple1, type(tuple1))

# 요소 값 변경
# tuple1[0] = 'A'

# 요소 값 삭제
# del tuple1[0]

# 첫번째 값을 변경하려면 : 새로운 객체를 만들어야 합니다.
tuple1 = ('A',) + tuple1[1:]
print(tuple1)

# 세번째 값을 변경하려면
tuple1 = tuple1[:2] + ('C',) + tuple1[3:]
print(tuple1)

# 두번째 값을 삭제하려면
tuple1 = (tuple1[0],) + tuple1[2:]
print(tuple1)
'''
실행 결과

(1, 2, 3, 4) <class 'tuple'>
('A', 2, 3, 4)
('A', 2, 'C', 4)
('A', 'C', 4)
'''



