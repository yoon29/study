# https://wikidocs.net/20557
'''
01. 키워드(Keyword)
키워드(Keyword)는 파이썬에서 이미 예약되어있는 문자열로서 다른 용도로 사용이 불가능한 문자열 입니다. 다음의 코드를 키워드를 확인할 수 있습니다.

Ex01_keyowrd1.py

import keyword
# print(keyword.kwlist)
kwlist = keyword.kwlist
for i in range(0,len(kwlist)):
    print("[{:10}]".format(kwlist[i]), end=" ")
    if (i+1)%5==0: print()
실행 결과

[False     ] [None      ] [True      ] [and       ] [as        ]
[assert    ] [break     ] [class     ] [continue  ] [def       ]
[del       ] [elif      ] [else      ] [except    ] [finally   ]
[for       ] [from      ] [global    ] [if        ] [import    ]
[in        ] [is        ] [lambda    ] [nonlocal  ] [not       ]
[or        ] [pass      ] [raise     ] [return    ] [try       ]
[while     ] [with      ] [yield     ]
앞으로 배워나가면서 알게되겠지만 몇 가지만 먼저 알아보도록 하겠습니다.
'''

########################################################################################################################

'''
1. True/False
True/False는 파이썬에서 진리 값입니다. 그것들은 파이썬에서의 비교 연산 또는 논리적 (Boolean) 연산의 결과입니다.
'''

# 진리값
print("참 : ", True)
print("거짓 : ", False)
print(1==1)
print(3>5)
print(3<5)
print(True or False)
print(True and False)
print(not False)
print(True==1)
print(False==0)
print(True + True)
'''
실행 결과

참 :  True
거짓 :  False
True
False
True
True
False
True
True
True
2
'''

########################################################################################################################

'''
2. None
값이 없음을 나타내는 Python의 특수 상수입니다.
'''

# 진리값
print("None : ", None)
print(None == 0)
print(None == [])
print(None == False)
print(None == "")
x = None
y = None
print(x == y)

# 아무값도 리턴하지 않는 함수
def void_function():
    a = 10
    b = 20
    c = a + b

result = void_function()
print(result)
print("값이없음" if result==None else result)
# ※ 3항 연산자 : 연산 대상이 3개인 연산자
# 참일때 값 if 조건 else 거짓일때값
'''
실행 결과

None :  None
False
False
False
False
True
None
값이없음
'''

########################################################################################################################

'''
3. assert
assert 디버깅 목적으로 사용됩니다.
디버그(debug), 디버깅(debugging)은 컴퓨터 프로그램의 정확성이나 논리적인 오류(버그)를 찾아내는 테스트 과정을 뜻합니다.
일반적으로 디버깅을 하는 방법으로 테스트 상의 체크, 기계를 사용하는 테스트, 실제 데이터를 사용해 테스트하는 방법이 있습니다.

사용형식 : assert condition, message

프로그래밍하는 동안 때때로 우리는 프로그램의 내부 상태를 알고 싶거나 우리의 가정이 사실인지 확인하기를 원합니다.
assert이 작업을 수행하고 버그를보다 편리하게 찾을 수 있습니다. assert뒤에 조건이옵니다.

조건이 true이면 아무 일도 발생하지 않습니다. 그러나 조건이 거짓이면 AssertionError가 발생합니다.
'''

# assert 디버깅 목적으로 사용됩니다.
a = 10
assert a > 5
# assert a < 5
assert a < 5, "a의 값이 너무 큽니다."
'''
# 메시지를 지정하지 않은 경우
Traceback (most recent call last):
  File "C:/PyThonProjects/Ex01/basic04/Ex04_keyword4.py", line 4, in <module>
    assert a < 5
AssertionError

# 메시지를 지정한 경우
Traceback (most recent call last):
  File "C:/PyThonProjects/Ex01/basic04/Ex04_keyword4.py", line 5, in <module>
    assert a < 5, "a의 값이 너무 큽니다."
AssertionError: a의 값이 너무 큽니다.
'''
'''
뒤에 메시지를 쓰면 지정한 메세지로 AssertionError를 발생합니다.
다음의 식과 같은 역할을 합니다. 예외 처리하는 방법은 뒤에 자세하게 배우게 됩니다.

if not condition:
    raise AssertionError(message)
'''

########################################################################################################################







