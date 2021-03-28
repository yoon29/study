'''
04. 모듈의 사용(import )
1. 모듈이란?
파이썬(Python) 모듈(Module)이란? 자주 사용되는 코드나 유용한 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것입니다.
보통 하나의 파이썬 .py 파일이 하나의 모듈이 됩니다. 모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있으며, 실행 코드를 포함할 수도 있습니다.
여기서는 모듈의 사용법에 대하여만 알아보고 뒤에 모듈의 작성법부터 차례대로 알아보도록 하겠습니다.

2. 내장 모듈
파이썬은 기본적으로 상당히 많은 표준 라이브러리 모듈들을 제공하고 있으며, 3rd Party에서도 많은 파이쎤 모듈들을 제공하고 있습니다.
IDLE에서 다음과 같이 help("modules") 을 입력하면 설치된 모듈의 목록을 확인 할 수 있습니다.

help("modules") [Enter]

Please wait a moment while I gather a list of all available modules...

__future__          autocomplete        idle                sched
__main__            autocomplete_w      idle_test           scrolledlist
_ast                autoexpand          idlelib             search
_asyncio            base64              idna                searchbase
_bisect             bdb                 imaplib             searchengine

중간 생략.....

asyncio             hmac                rstrip              zoomheight
asyncore            html                run                 zzdummy
atexit              http                runpy
audioop             hyperparser         runscript

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".
'''

'''
3. 모듈의 사용(import)
이러한 모듈들을 사용하기 위해서는 모듈을 import하여 사용하면 되는데, import 문은 다음과 같이 하나 혹은 복수의 모듈을 불러들일 수 있습니다.

import 모듈
import 모듈1, 모듈2, 모듈3 ...
import 모듈명 as 별명

모듈에 있는 모든 내용을 포함시킵니다.
'모듈명.함수명'처럼 모듈명을 반드시 입력해야 합니다.
as를 사용하여 모듈명에 별명을 붙일 수 있습니다.

from 모듈 import 함수
from 모듈 import 함수1, 함수2, 함수3 ...
from 모듈 import *
from 모듈 import 함수 as 별명

form import 방식을 사용하면 모듈이름을 생략할 수 있습니다.
*를 사용하면 모듈에 있는 모든 내용이 포함됩니다.
as를 사용하여 함수명에 별명을 붙일 수 있습니다.
'''

########################################################################################################################

# 모듈(Module) 사용하기
import datetime
import math
import math as m
from math import pi
from math import *

# import datetime
now = datetime.datetime.now()
print(now)

# import math
print("The value of pi is", math.pi)

# import math as m
print("The value of pi is", m.pi)

# from math import pi
print("The value of pi is", pi)

# from math import *
print("The value of e is", e)
'''
2018-07-06 17:27:36.859288
The value of pi is 3.141592653589793
The value of pi is 3.141592653589793
The value of pi is 3.141592653589793
The value of e is 2.718281828459045
'''

########################################################################################################################

















