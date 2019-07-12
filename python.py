Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> a1=t.Turtle()
>>> for i in range(250):
	a1.forward(i)
	a1.left(91)
>>>t.done()
SyntaxError: invalid syntax
>>> import turtle as t
>>> a1=t.Turtle()
>>> for i in range(250):
	a1.forward(i)
	a1.left(91)
t.done()
SyntaxError: invalid syntax
>>> import turtle as t
>>> a1=t.Turtle()
>>> for i in range(250):
	a1.forward(i)
	a1.left(91)

	
t.done()
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red')
SyntaxError: invalid syntax
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolour(colour[i%6])
	width(x/100+1)
	forward(x)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    pencolour(colour[i%6])
NameError: name 'pencolour' is not defined
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolour(colours[i%6])
	width(x/100+1)
	forward(x)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    pencolour(colours[i%6])
NameError: name 'pencolour' is not defined
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolor(colours[i%6])
	width(x/100+1)
	forward(x)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 3, in <module>
    width(x/100+1)
NameError: name 'x' is not defined
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolor(colours[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    pencolor(colours[i%6])
IndexError: list index out of range
>>> from turtle import *
>>> colours=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolor(colors[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    pencolor(colors[i%6])
NameError: name 'colors' is not defined
>>> from turtle import *
>>> colors=['blue','green','yellow','orange','red']
>>> for i in range(250):
	pencolor(colors[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    pencolor(colors[i%6])
IndexError: list index out of range
>>> from turtle import *
>>> colors=['blue','green','yellow','orange','red','purple']
>>> for i in range(250):
	pencolor(colors[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
Traceback (most recent call last):
  File "<pyshell#47>", line 5, in <module>
    left(59)
  File "<string>", line 8, in left
  File "C:\Users\susha\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1699, in left
    self._rotate(angle)
  File "C:\Users\susha\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Users\susha\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Users\susha\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Users\susha\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> for i in range(250):
	pencolor(colors[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
>>> from turtle import *
>>> goto(50,50)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    goto(50,50)
  File "<string>", line 5, in goto
turtle.Terminator
>>> from turtle import *
>>> colors=['blue','green','yellow','orange','red','purple']
>>> for i in range(360):
	pencolor(colors[i%6])
	width(i/100+1)
	forward(i)
	left(59)

	
>>> from turtle import *
>>> goto(50,50)
>>> goto(-50,50)
>>> goto(100,50)
>>> goto(-50,-50)
>>> from turtle import *
>>> for angle in range of (0,360,15):
	
SyntaxError: invalid syntax
>>> from turtle import *
>>> for angle in range(0,360,15):
	setheading(angle)
	forward(100)
	write(str(angle)+'o')
	backward(100)

	
Traceback (most recent call last):
  File "<pyshell#70>", line 2, in <module>
    setheading(angle)
  File "<string>", line 5, in setheading
turtle.Terminator
>>> from turtle import *
>>> for angle in range(0,360,15):
	setheading(angle)
	forward(100)
	write(str(angle)+'o')
	backward(100)

	
>>> for angle in range(0,360,15):
	setheading(angle)
	forward(100)
	write(str(angle)+'o')
	backward(100)

	
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    setheading(angle)
  File "<string>", line 5, in setheading
turtle.Terminator
>>> from turtle import *
>>> for angle in range(0,360,15):
	setheading(angle)
	forward(100)
	write(str(angle)+'o')
	backward(100)

	
>>> from turtle import *
>>> for i in range(20):
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)
	right(90)
	forward(100)
	right(90)

	
Traceback (most recent call last):
  File "<pyshell#89>", line 4, in <module>
    forward(100)
  File "<string>", line 5, in forward
turtle.Terminator

>>> from turtle import *
>>> for i in range(20):
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)
	right(90)
	forward(100)
	right(90)

	
>>> from turtle import *
>>> for i in range(20):
	forward(100)
	left(90)
	forward(10)
	left(90)
	forward(100)
	right(90)
	forward(10)
	right(90)

	
Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    forward(100)
  File "<string>", line 5, in forward
turtle.Terminator
>>> from turtle import *
>>> for i in range(15):
	forward(100)
	left(90)
	forward(10)
	left(90)
	forward(100)
	right(90)
	forward(10)
	right(90)

	
>>> from turtle import *
>>> pensize(50)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    pensize(50)
  File "<string>", line 5, in pensize
turtle.Terminator
>>> from turtle import *
>>> pensize[50]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    pensize[50]
TypeError: 'function' object is not subscriptable
>>> from turtle import *
>>> pensize(30)
>>> pencolor('blue')
>>> forward(250)
>>> pencolour(0,1,0,0)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    pencolour(0,1,0,0)
NameError: name 'pencolour' is not defined
>>> from turtle import *
>>> pensize(30)
>>> pencolor('blue')
>>> forward(250)
>>> forward(250)
>>> from turtle import *
>>> from turtle import *
>>> pensize(30)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    pensize(30)
  File "<string>", line 5, in pensize
turtle.Terminator
>>> from turtle import *
>>> pensize(30)
>>> pencolor('blue')
>>> forward(250)
>>> pencolor('green')
>>> forward(250)
>>> pensize(10)
>>> goto(-400,50)
>>> for red in range(4):
	for green in range(4):
		for blue in range(4):
			pencolor[red/4.0,green/4.0,blue/4.0]
			forward(10)

			
Traceback (most recent call last):
  File "<pyshell#130>", line 4, in <module>
    pencolor[red/4.0,green/4.0,blue/4.0]
TypeError: 'function' object is not subscriptable
>>> from turtle import *
>>> colors=['blue','green','yellow','orange','red','purple']
>>> reset()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    reset()
  File "<string>", line 5, in reset
turtle.Terminator
>>> from turtle import *
>>> colors=['blue','green','yellow','orange','red','purple']
>>> reset()
>>> from turtle import *
>>> fillcolour('purple')
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    fillcolour('purple')
NameError: name 'fillcolour' is not defined
>>> from turtle import *
>>> fillcolor('purple')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    fillcolor('purple')
  File "<string>", line 5, in fillcolor
turtle.Terminator
>>> 
