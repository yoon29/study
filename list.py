'''
05. Python List
'''

########################################################################################################################

'''
1. list란?
list는 자료들의 모임입니다.
입력된 순서가 유지 됩니다.
list()생성자나 []로 리스트를 만듭니다.
set과 다르게 1개짜리 리스트도 만들 수 있습니다.
어떤 자료 형도 저장이 가능합니다.
Ex19_list1.py
'''

list1 = list()
print(type(list1), list1)

list2 = []
print(type(list2), list2)

list3 = [1, 2, 3, 4, 5]
print(type(list3), list3)

list4 = [1]
print(type(list4), list4)

list5 = [1, 2, 3, 1.1, 2.2, 'A', True,(1,2,3)]
print(type(list5), list5)
'''
실행 결과

<class 'list'> []
<class 'list'> []
<class 'list'> [1, 2, 3, 4, 5]
<class 'list'> [1]
<class 'list'> [1, 2, 3, 1.1, 2.2, 'A', True, (1, 2, 3)]
'''

########################################################################################################################

'''
2. 리스트의 길이, 추가, 삽입, 수정,
len() 함수를 이용하여 요소 개수를 얻을 수 있습니다.
[n:m] 값을 이용하여 접근이 가능합니다.
append() 메서드를 이용하여 추가가 가능합니다.
insert() 메서드를 이용하여 삽입이 가능합니다.
remove() 메서드를 이용하여 삭제가 가능합니다.
clear() 메서드를 이용하여 모든 요소 삭제가 가능합니다.
Ex20_list2.py
'''

import random as rnd
list1 = [];
print("리스트의 길이 :",len(list1))
for i in range(1,10):
    list1.append(rnd.randrange(1,100))  # 추가

print("리스트의 길이 :",len(list1))
print(list1)
print('2번째부터 4번째까지  :',list1[2:5])

print(list1[0])
list1[0] = 99 # 수정
print(list1[0])

list1.insert(3,88) # 삽입
list1.insert(3,77)
print(list1)

# 삭제 : 인덱스가 변하므로 주의해야 함
for i in list1:
    if i > 50:
        list1.remove(i)
print(list1)

# 삭제 뒤에서 부터 해야함
for index in range(len(list1)-1, -1, -1):
    if list1[index] > 50:
        list1.remove(list1[index])
print(list1)

# 모두 지우기
list1.clear()
print(list1)

'''
실행 결과

리스트의 길이 : 0
리스트의 길이 : 9
[61, 20, 63, 11, 98, 4, 51, 35, 75]
2번째부터 4번째까지  : [63, 11, 98]
61
99
[99, 20, 63, 77, 88, 11, 98, 4, 51, 35, 75]
[20, 77, 11, 4, 35]
[20, 11, 4, 35]
[]
'''

########################################################################################################################

'''
3. 정렬, 뒤집기, 복사
reverse()메서드를 이용하여 뒤집기가 가능합니다.
sort() 메서드를 이용하여 정렬이 가능합니다.
sorted() 함수를 이용하여 정렬이 가능합니다.
copy() 메서드를 이용하여 복사가 가능합니다.
Ex21_list3.py
'''

import random as rnd
list1 = []
for i in range(1,10):
    list1.append(rnd.randrange(1,100))  # 추가
print(list1)
# 뒤집기
list1.reverse()
print(list1)

# 오름 차순 정렬
list1.sort()  # 자신이 변경됨
print(list1)
# 내림 차순 정렬
list1.sort(reverse=True)
print(list1)

list2 = sorted(list1)  # 정렬된 리스트 반환
print(list1, list2)

list2 = sorted(list1, reverse=True)
print(list1, list2)

# 얕은복사 : 주소가 복사됨
list2 = list1
print(list1, list2)
list2[0] = 999  # 1개변경
print(list1, list2) # 둘다 변경 : 같은 객체이다.


# 깊은복사 : 값이 복사됨
list2 = list1.copy()
print(list1, list2)
list2[0] = 777  # 1개 변경
print(list1, list2) # 1개만 변경 : 다른 객체이다.
'''
실행 결과

[34, 46, 58, 56, 22, 62, 34, 97, 57]
[57, 97, 34, 62, 22, 56, 58, 46, 34]
[22, 34, 34, 46, 56, 57, 58, 62, 97]
[97, 62, 58, 57, 56, 46, 34, 34, 22]
[97, 62, 58, 57, 56, 46, 34, 34, 22] [22, 34, 34, 46, 56, 57, 58, 62, 97]
[97, 62, 58, 57, 56, 46, 34, 34, 22] [97, 62, 58, 57, 56, 46, 34, 34, 22]
[97, 62, 58, 57, 56, 46, 34, 34, 22] [97, 62, 58, 57, 56, 46, 34, 34, 22]
[999, 62, 58, 57, 56, 46, 34, 34, 22] [999, 62, 58, 57, 56, 46, 34, 34, 22]
[999, 62, 58, 57, 56, 46, 34, 34, 22] [999, 62, 58, 57, 56, 46, 34, 34, 22]
[999, 62, 58, 57, 56, 46, 34, 34, 22] [777, 62, 58, 57, 56, 46, 34, 34, 22]
'''






