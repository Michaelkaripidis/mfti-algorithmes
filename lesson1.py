

import turtle

# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# буква S

# turtle.shape('turtle')
# turtle.width(20)
# turtle.forward(50)
# turtle.left(90)

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
# Пятиконечная звезда

# from turtle import *
# color('yellow', 'red')
# begin_fill()
# while True:
#     forward(-200)
#     left(144)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
# Colored Star

# Exercise 3 квадрат
# turtle.shape('turtle')
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)

# Exercise 4 круг

# turtle.circle(100)
# turtle.shape('turtle')
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)
# turtle.left(45)
# turtle.fd(50)


# Спираль петля
# i = 0
# while i < 61:
#     i += 1
#     turtle.left(i)
#     turtle.forward(2 * 3.14 * 100 /60)

# 4 Круг
# i = 0
# while i < 61:
#     i += 1
#     turtle.left(6)
#     turtle.forward(2 * 3.14 * 100 /60)

# i = 0
# while i < 361:
#     i += 1
#     turtle.left(1)
#     turtle.forward(2 * 3.14 * 100 /360)

# r = 360
# for i in range(r):
#     turtle.left(360 / r)
#     turtle.forward(2 * 3.14 * 100 / r)

from turtle import *

# def draw_square(a,color,x,y):
#     penup()
#     goto(x,y)
#     setheading(90)
#     backward(a//2)
#     setheading(0)
#     backward(a//2)
#     pendown()
#     pencolor(color)
#     for _ in range(4):
#         forward(a)
#         left(90)
#
# draw_square(20,"pink",0,0)
# draw_square(50,"pink",0,0)
# draw_square(70,"pink",0,0)
# draw_square(90,"pink",0,0)
# draw_square(110,"pink",0,0)

# x = 10
# for i in range(10):
#
#     turtle.pendown()
#
#     for ii in range(4):
#         turtle.forward(x)
#         turtle.right(90)
#
#     turtle.penup()
#
#     turtle.forward(1)
#     turtle.left(90)
#     turtle.forward(1)
#
#     x = x + 2

# x = 50
# for i in range(10):
#
#     turtle.pendown()
#
#     for ii in range(4):
#         turtle.forward(x)
#         turtle.right(90)
#
#     turtle.penup()
#
#     turtle.left(180)
#     turtle.forward(10)
#     turtle.left(90)
#     turtle.forward(10)
#
#     x = x + 20

# x = 50
# for i in range(10):
#
#     turtle.pendown()
#
#     for ii in range(4):
#         turtle.forward(x)
#         turtle.right(90)
#
#     turtle.penup()
#
#     turtle.left(90)
#     turtle.forward(10)
#     turtle.left(90)
#     turtle.forward(10)
#     turtle.left(180)
#
#     x = x + 20

# x = 50
# y = 10
#
# for i in range(10):
#
#     turtle.pendown()
#
#     for ii in range(4):
#         turtle.forward(x)
#         turtle.right(90)
#
#     turtle.penup()
#
#     turtle.left(90)
#     turtle.forward(y)
#     turtle.left(90)
#     turtle.forward(y)
#     turtle.left(180)
#
#     x = x + 2 * y

# def draw_square(x,y,z):
#     for i in range(z):
#         turtle.pendown()
#         for ii in range(4):
#             turtle.forward(x)
#             turtle.right(90)
#         turtle.penup()
#
#         turtle.left(90)
#         turtle.forward(y)
#         turtle.left(90)
#         turtle.forward(y)
#         turtle.left(180)
#
#         x = x + 2 * y
#
# draw_square(50,20,5)

# x = 12
# y = 100
#
# for i in range(x):
#     turtle.shape('turtle')
#     turtle.fd(y)
#     turtle.stamp()
#     turtle.left(180)
#     turtle.fd(y)
#     turtle.left(180 - 360 / x)

# for i in range(1000):
#     turtle.forward(i * 0.001)
#     turtle.left(1)

# from math import pi, sin, cos
#
# turtle.shape('turtle')
# for i in range(200):
#     t = i / 10 * pi
#     dx = t * cos(t)
#     dy = t * sin(t)
#     turtle.goto(dx, dy)

# Квадртаная спираль
# def draw_square(x,z):
#     for i in range(z):
#
#         for _ in range(4):
#             turtle.forward(x)
#             turtle.right(90)
#             x = x + 10
#
# draw_square(20,10)


# Разноцветная спирал пример
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.width(x/100+1)
#     t.fd(x)
#     t.left(61)

# def hello(name):
#     print('Hello', '', '!')

# Функции
# def hello(name):
#     print('Hello, ', name, '!' )
#
#
# hello('world')

# def sum(a, b):
#     return a + b
#
#
# print(sum(1, 2))
# print(sum(5, 24))
# print(sum(4, 44))


# from math import sin, pi
#
# def draw(n,R):
#     # цикл в зависимости от количесва углов нашего многоугольника
#     for i in range(n):
#         # включаем прорисовку
#         turtle.pendown()
#         # прорисуем одну сторону многоуголиника на длину стороны многоугольника(формула)
#         turtle.forward(2*R*sin(pi/n))
#         # повернем черепашку на угол многоугольника чтобы рисовать следующу грань при новом проходе цикла
#         turtle.left(360/n)
#
# # Начинаем с треугольника, вписанного в круг радиусом 30
# # другие многоугольники будут вписаны в круг с радиусом плюс 20 (центр круга всегда в одной и той же точке)
# dR = 30
#
# # задаем цикл для определенного количества многоугольников, помним, что песледнее число не входит в цикл
# #  то есть (3,10) значит от треугольника до 9-ти угольника
# for x in range (3,10):
#     # выключаем прорисовку
#     turtle.penup()
#     # становимся в вершуну многоугольник (координыты: радиус круга по оси Х, и нуль по оси Y)
#     turtle.goto(dR,0)
#
#     # сумма углов многоугольника (формула)
#     s = 180 * (x - 2)
#
#     # значит один угол нашего многоугольника:
#     u = s / x

    # развернем черепашку на половину внутреннего угла между сторонами
    # turtle.setheading(180 - u/2)

    # прорисуем многоугольник при помощи нашей функции
    # draw(x, dR)

    # сориетируем черепашку в исходное направление вправо
    # turtle.setheading(0)

    # прирастим радиус для следующего многоугольника в цикле
    # dR = dR + 20


# Дуга
# import turtle
# turtle.penup()
# turtle.setx(-300)
# turtle.pendown()
# turtle.setheading(90)
# for _ in range(5):
#     turtle.circle(-60, 180)
#     turtle.circle(-10, 180)

# turtle.circle(60)
# turtle.circle(-60)
# turtle.setheading(45)
# turtle.circle(60)
# turtle.circle(-60)
# turtle.setheading(135)
# turtle.circle(60)
# turtle.circle(-60)


# Бабочка ( задаем
# r = 30
# for i in range(6):
#     turtle.setheading(90)
#     turtle.circle(r + i * 10)
#     turtle.circle(-(r + i * 10))


# Миша смайлик
# turtle.home()
# turtle.hideturtle()
# turtle.begin_fill()
# turtle.fillcolor('yellow')
# turtle.circle(100)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-45,110)
# turtle.pendown()
# turtle.begin_fill()
# turtle.fillcolor('blue')
# turtle.circle(15)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(45,110)
# turtle.pendown()
# turtle.begin_fill()
# turtle.fillcolor('blue')
# turtle.circle(15)
# turtle.end_fill()
#
#
# turtle.penup()
# turtle.setpos(0, 100)
# turtle.pendown()
# turtle.pensize(8)
# turtle.setheading(270)
# turtle.forward(40)
#
# turtle.penup()
# turtle.setpos(50,60)
# turtle.pendown()
# turtle.pensize(8)
# turtle.setheading(270)
# turtle.circle(-50,180)

# Marat смайлик

# turtle.home()
# turtle.setheading(90)
# turtle.hideturtle()
# turtle.begin_fill()
# turtle.fillcolor('yellow')
# turtle.circle(100)
# turtle.end_fill()
#
# turtle.penup()
# turtle.setpos(-120,40)
# turtle.pendown()
#
# turtle.begin_fill()
# turtle.fillcolor('blue')
# turtle.circle(15)
# turtle.end_fill()
#
# turtle.penup()
# turtle.setpos(-50,40)
# turtle.pendown()
#
# turtle.begin_fill()
# turtle.fillcolor('blue')
# turtle.circle(15)
# turtle.end_fill()
#
# turtle.penup()
# turtle.setpos(-100,20)
# turtle.pendown()
#
# turtle.pensize(8)
# turtle.setheading(270)
# turtle.forward(40)
# turtle.penup()
#
# turtle.setpos(-50,-10)
# turtle.pendown()
# turtle.pensize(8)
# turtle.pencolor('red')
# turtle.setheading(270)
# turtle.circle(-50, 180)