-------------
-------------
Create a funtcion to trigger AttributeError

def testatterror():
    n = 5
    n.append(4)
    print n
   .....:     

In [104]: testatterror()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-104-e6cab665e2fa> in <module>()
----> 1 testatterror()

<ipython-input-103-d6290a627534> in testatterror()
      1 def testatterror():
      2     n = 5
----> 3     n.append(4)
      4     print n
      5 

AttributeError: 'int' object has no attribute 'append'

In [105]: 




-------------
-------------
Create a funtcion to trigger TypeError


def testtypeerror():
    n = '5'
    m =  5
    mn = m + n
    print mn
   ....:     

In [99]: testtypeerror()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-99-2c3a32be449d> in <module>()
----> 1 testtypeerror()

<ipython-input-98-dc82486ac12c> in testtypeerror()
      7     n = '5'
      8     m =  5
----> 9     mn = m + n
     10     print mn
     11 

TypeError: unsupported operand type(s) for +: 'int' and 'str'

In [100]: 




-------------
-------------
Create a funtcion to trigger NameError
def testnameerror():
    print nn
   

In [89]: testnameerror()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-89-23be1ea02b92> in <module>()
----> 1 testnameerror()

<ipython-input-88-e54aba5a1687> in testnameerror()
      1 def testnameerror():
----> 2     print nn
      3 

NameError: global name 'nn' is not defined




-------------
-------------
Create a function to trigger SyntaxError

def testnameerror()
    print n

In [85]: def testnameerror()
  File "<ipython-input-85-0ef4b784a7a2>", line 1
    def testnameerror()
                       ^
SyntaxError: invalid syntax

