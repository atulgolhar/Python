#!usr/bin/env python3
# Calculatorv1.py

>>> class MuffledCalculator:
        muffled = False
        def calc(self, expr):
            try:
                return eval(expr)
            except ZeroDivisionError:
                if self.muffled:
                    print("Dear Human division by zero is illegal")
                else:
                    raise

>>> calculator
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    calculator
NameError: name 'calculator' is not defined

>>> call Calculator:    
SyntaxError: invalid syntax

>>> class Calculator:
        def calculate(self, expression):
            self.value = eval(expression)
        
>>> class Talker:
        def talk(self):
            print("Hi, my value is", self.value)
        
>>> class TalkingCalculator(Calculator, Talker):
        pass

>>> tc = TalkingCalculator()              # initial calculator call
>>> tc.calculate('1+2*3')                 # basic calculator math expression
>>> tc.talk()
Hi, my value is 7
>>> hasattr(tc, 'talk')
True
>>> callable(getattr(tc, 'talk', None))
True

>>> class Talker(ABC):
        @abstractmethod
        def talk(self):
            pass
 
>>> class Knigget(Talker):
        pass

>>> class Knigget(Talker):
        def talk(self):
            print("Ni!")

        
>>> k = Knigget()
>>> isinstance(k, Talker)
True
>>> k.talk()
Ni!
>>> type(MuffledCalculator)
<class 'type'>

>>> calculator = MuffledCalculator()
>>> calculator.calc("10/2")
5.0
>>> 

>>> calculator.calc('10/0')
Traceback (most recent call last):
  File "<pyshell#450>", line 1, in <module>
    calculator.calc('10/0')
  File "<pyshell#403>", line 5, in calc
    return eval(expr)
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero

>>> calculator.muffled = True
>>> calculator.calc('10/0')
Dear Human division by zero is illegal


