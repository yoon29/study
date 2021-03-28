'''
04. Python Set
1. set이란?
set 자료형은 중복을 허용하지 않습니다.
set은 입력된 순서는 중요하지 않습니다.
set() 생성자 함수를 이용해서 만들 수 있습니다.
{}를 이용해서 만들 수 있습니다.
add() 메서드를 이용하여 추가가 가능합니다.
update() 메서드를 이용하여 동시에 여러개 추가가 가능합니다.
remove() 메서드를 이용하여 삭제가 가능합니다.
copy() 메서드를 이용하여 복사가 가능합니다.
clear() 메서드를 이용하여 모든 요소 삭제가 가능합니다.
Ex14_set1.py
'''

# set 자료형이란?
# 순서에 상관없이 중복을 제거하는 자료형
set1 = set("Hello Python!!!")
print(set1, type(set1))

set2 = {1,2,3, 'a', 'b', 'c', True, 3.14}
print(set2, type(set2))


set3 = set({1,2,3})
print(set3, type(set3))

set4 = set([1,2,3])
print(set4, type(set4))

set5 = set()
print(set5, type(set5))

for i in range(0,5):
    set5.add(i)

for i in range(0,5):
    set5.add(i)

print(set5, type(set5))

set5.add('a')
set5.add('문자열')
set5.add(34.6)
print(set5, type(set5))

set5.update({11, 22, 33})
print(set5, type(set5))

set5.remove(0)
set5.remove(2)
print(set5, type(set5))

set6 = set5.copy()
print(set6, type(set6))

set6.clear()
print(set6, type(set6))
'''
실행 결과

{'t', ' ', 'l', 'P', 'h', '!', 'H', 'e', 'y', 'o', 'n'} <class 'set'>
{1, 2, 3, 3.14, 'a', 'c', 'b'} <class 'set'>
{1, 2, 3} <class 'set'>
{1, 2, 3} <class 'set'>
set() <class 'set'>
{0, 1, 2, 3, 4} <class 'set'>
{0, 1, 2, 3, 4, 34.6, 'a', '문자열'} <class 'set'>
{0, 1, 2, 3, 4, 34.6, 33, 'a', 11, 22, '문자열'} <class 'set'>
{1, 3, 4, 34.6, 33, 'a', 11, 22, '문자열'} <class 'set'>
{1, 34.6, 3, 4, 33, 'a', 11, 22, '문자열'} <class 'set'>
set() <class 'set'>
'''

########################################################################################################################

'''
2. set활용하기
천자문은 동일한 글자는 세지 않는다면 한글로는 몇글자일까?
Ex15_set2.py

사용된 파일들
chunja.txt
chunja2.txt
national_anthem.txt
'''

# 텍스트 파일 읽기전용으로 열기
f = open('chunja.txt', 'r',encoding='UTF-8')
# 모든 내용을 리스트로 읽기
lines = f.readlines();
# 타입 검사
print(type(lines))
# set 만들기
hanja_set = set()
hangul_set = set()
# 1줄씩 끝까지 반복
for ch in lines:
    # print(ch.split("|")[1], ch.split("|")[2], sep='')
    # set에 추가
    hanja_set.add(ch.split("|")[1])
    hangul_set.add(ch.split("|")[2])

print("한자수 : {}글자".format(len(hanja_set)))
print("한글수 : {}글자".format(len(hangul_set)))
'''
실행 결과

<class 'list'>
한자수 : 1000글자
한글수 : 321글자
'''

########################################################################################################################

'''
애국가는 몇개의 단어로 만들어 졌을까?
Ex16_set3.py
'''

national_anthem = '''
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세 
무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세 
남산 위에 저 소나무 철갑을 두른듯 바람서리 불변함은 우리 기상일세 
무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세 
가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세 
무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세 
이 기상과 이 마음으로 충성을 다하여 괴로우나 즐거우나 나라사랑하세 
무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세
'''
# print(national_anthem)
national_anthem = national_anthem.replace('\n', '')
# print(national_anthem)

# '대한'이란 단어의 개수
print('애국가에는 "대한"이란 문자열이 {}개 나타납니다.'.format(national_anthem.count('대한')))
# 공백으로 구분하여 list로 만들기
word_list = national_anthem.split(' ')
# 전체 단어 수
print('애국가에 사용된 단어 수는 총 {}개 입니다.'.format(len(word_list)))
# 단어를 set으로 만들기
word_set = set(word_list)
print('애국가에는 총 {}개 단어가 사용되었습니다.'.format(len(word_set)))
print('애국가에는 총 {}개 단어가 중복 사용되었습니다.'.format(len(word_list)-len(word_set)))


# 단어 출력
# for str in word_set:
#     print('[',str,']')
'''
실행 결과

애국가에는 "대한"이란 문자열이 8개 나타납니다.
애국가에 사용된 단어 수는 총 70개 입니다.
애국가에는 총 44개 단어가 사용되었습니다.
애국가에는 총 26개 단어가 중복 사용되었습니다.
'''

########################################################################################################################

'''
중복되지 않는 번호 뽑기?
random 모듈을 이용하면 더 편리한 방법이 있습니다. 여기서는 set의 특징을 보는 예제 입니다.

Ex17_set4.py
'''

import random as rnd

game = int(input("몇게임?"))
for i in range(1, game+1):
    # 중복되지 않은 숫자 6개 뽑기
    lotto_set = set()
    while len(lotto_set) < 6:
        lotto_set.add(rnd.randint(1,45))

    # print(lotto_set)
    print(i, '게임 :', sorted(lotto_set))
    game -= 1
'''
실행 결과

몇게임?5
1 게임 : [2, 4, 11, 27, 37, 44]
2 게임 : [5, 20, 21, 32, 38, 42]
3 게임 : [1, 11, 12, 23, 33, 44]
4 게임 : [2, 8, 12, 23, 29, 43]
5 게임 : [1, 2, 12, 26, 37, 43]
'''


