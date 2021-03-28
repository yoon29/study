'''
06. Python Dictionary
'''

########################################################################################################################

'''
1. dictionary(사전) 란?
dictionary는 "키(Key)/값(Value)" 쌍을 요소로 갖는 자료형입니다.
dictionary는 흔히 Map 이라고도 불립니다. 키(Key)로 신속하게 값(Value)을 찾아내는 해시테이블(Hash Table) 구조를 갖습니다.
파이썬에서 dictionary는 "dict" 클래스로 구현되어 있습니다.
dictionary의 키(key)는 그 값을 변경할 수 없는 Immutable 타입이어야 하며, dictionary 값(value)은 Immutable과 Mutable 모두 가능합니다.
예를 들어, dictionary의 키(key)로 문자열이나 Tuple은 사용될 수 있는 반면, 리스트는 키로 사용될 수 없습니다.
dictionary의 요소들은 {} 를 사용하여 만듭니다. 여러개일 경우 콤마(,)로 구분합니다.
{}를 이용하여 만들 수 있습니다.
dict() 생성자를 이용하여 만들 수 있습니다.
Ex22_dictionary1.py
'''

# dictionary(사전)란?
dict1 = {}
print(dict1, type(dict1))

dict2 = {'name':'한사람','age':22, 'gender': True}
print(dict2, type(dict2))
print(dict2['name'])
print(dict2['age'])
print(dict2['gender'])

tuple1 = ('이름','나이','성별')
dict3 = {tuple1 : ('한사람', 22, True)}
print(dict3, type(dict3))

print(dict3[tuple1])
for index in range(0,3):
    print(tuple1[index],":", dict3[tuple1][index])

dict4 = dict(kor=87, eng=80, mat=85, edps=99)
print(dict4, type(dict4))
print(dict4['kor'])
'''
실행 결과

{} <class 'dict'>
{'name': '한사람', 'age': 22, 'gender': True} <class 'dict'>
한사람
22
True
{('이름', '나이', '성별'): ('한사람', 22, True)} <class 'dict'>
('한사람', 22, True)
이름 : 한사람
나이 : 22
성별 : True
{'kor': 87, 'eng': 80, 'mat': 85, 'edps': 99} <class 'dict'>
87
'''

########################################################################################################################

'''
2. dictionary 조작하기
keys() 메서드로 키값 만을 얻을 수 있습니다.
values() 메서드로 값만을 얻을 수 있습니다.
"dict객체[키]=값"으로 새로운 요소를 추가 가능합니다.
update()메서드로 한번에 여러게 요소를 추가 가능합니다.
같은 키에 다른값을 넣으면 수정이 됩니다.
"del dict객체[키]"으로 요소 삭제가 가능합니다.
items() 메서드로 (key,value)쌍 얻을 수 있습니다.
Ex23_dictionary2.py
'''

# Dictionary(사전)란?
dict1 = {'name': '한사람', 'age': 22, 'gender': True}
print(dict1, type(dict1))

# 키 반복
for key in dict1.keys():
    print(key, ':', dict1[key])

# 값 반복
for value in dict1.values():
    print(value)

# 추가
dict1['hobby'] = ['술', '춤', '잠']
dict1['weight'] = 78.65
print(dict1)

# 동시에 여러요소 추가
dict1.update({'weight':67.8,'height': 189.7})
print(dict1)

# 수정
dict1['hobby'] = ['술', '춤', '잠','게임','등산']
print(dict1)

# 요소 삭제
del dict1['weight']
print(dict1)

# (key,value)쌍 얻기
print(dict1.items())
for data in dict1.items():
    # print(data, type(data))
    print(data[0], ':', data[1])
'''
실행 결과

{'name': '한사람', 'age': 22, 'gender': True} <class 'dict'>
name : 한사람
age : 22
gender : True
한사람
22
True
{'name': '한사람', 'age': 22, 'gender': True, 'hobby': ['술', '춤', '잠'], 'weight': 78.65}
{'name': '한사람', 'age': 22, 'gender': True, 'hobby': ['술', '춤', '잠'], 'weight': 67.8, 'height': 189.7}
{'name': '한사람', 'age': 22, 'gender': True, 'hobby': ['술', '춤', '잠', '게임', '등산'], 'weight': 67.8, 'height': 189.7}
{'name': '한사람', 'age': 22, 'gender': True, 'hobby': ['술', '춤', '잠', '게임', '등산'], 'height': 189.7}
dict_items([('name', '한사람'), ('age', 22), ('gender', True), ('hobby', ['술', '춤', '잠', '게임', '등산']), ('height', 189.7)])
name : 한사람
age : 22
gender : True
hobby : ['술', '춤', '잠', '게임', '등산']
height : 189.7
'''


