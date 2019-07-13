Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> a1=t.Turtle()
>>> a1=pencolour('red')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a1=pencolour('red')
NameError: name 'pencolour' is not defined
>>> import turtle as t
>>> a1=t.Turtle()
>>> a1.pencolor('red')
>>> for i in range(250)
SyntaxError: invalid syntax
>>> import turtle as t
>>> a1=t.Turtle()
>>> a1.pencolor('red')
>>> for i in range(250):
	width(i/100+1)
	a1.forward(i)
	a1.left(91)

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    width(i/100+1)
NameError: name 'width' is not defined
>>> import turtle as t
>>> a1=t.Turtle()
>>> a1.pencolor('red')
>>> for i in range(250):
	width(x/100+1)
	forward(x)
	left(91)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    width(x/100+1)
NameError: name 'width' is not defined
>>> import turtle as t
>>> a1=t.Turtle()
>>> a1.pencolor('red')
>>> for i in range(250):
	a1.forward(i)
	a1.left(91)

	
>>> 
