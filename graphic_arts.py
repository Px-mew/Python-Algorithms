import turtle
import random
import math
"""
    тест - визуализация фигур с помощью библиотеки turtle
"""
def rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def triangle(side):
    for _ in range(3):
        turtle.right(120)
        turtle.forward(side)

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

def time():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.penup()
    for _ in range(6):
        turtle.forward(5)
        turtle.left(60)

def rhombus(side, angle):
    """
    Ромб. аргументы - сторона ромба и острый угол
    """
    for _ in range(2):
        turtle.forward(side)
        turtle.right(angle)
        turtle.forward(side)
        turtle.right((360-(angle*2))/2)

def rays(x, y, n):
    """
    лучи для снежинки
    """
    turtle.left(60)
    turtle.forward(n)
    turtle.backward(n)
    turtle.right(120)
    turtle.forward(n)
    turtle.backward(n)
    turtle.left(60)

def snowflake(x, y, n):
    """
    снежинки
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(6):
        turtle.forward(n/4)
        for _ in range(3):
            rays(turtle.xcor(), turtle.ycor(), n/4)
            turtle.forward(n/4)
        turtle.backward(n)
        turtle.left(60)


def random_stars():
    """
    # пятиконечная звезда
    """
    turtle.Screen().colormode(255)
    turtle.penup()
    turtle.goto(random.randint(-150, 150), random.randint(-150, 150))
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.left(random.randint(0, 360))
    turtle.begin_fill()
    size = random.randint(7, 20)
    for _ in range(5):
        turtle.forward(size)
        turtle.left(144)
    turtle.end_fill()

def polygon(n):
    turtle.Screen().colormode(255)
    a = math.sqrt((2000*4*math.tan(math.radians(180)/n))/n)
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.begin_fill()
    for _ in range(n):
        turtle.forward(a/2)
        turtle.left(360/n)
        turtle.forward(a/2)
    turtle.end_fill()

def heart(t):
    x = 128*math.sin(t)**3
    y = 8*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t) - 5)
    turtle.goto(x, y)


turtle.showturtle()

# три квадрата
turtle.left(22.5)
square(120)
turtle.left(22.5)
square(120)
turtle.left(22.5)
square(120)
turtle.clearscreen()

# 8 квадратов
turtle.speed(8)
for _ in range(8):
    square(100)
    turtle.left(45)
turtle.clearscreen()

# шестиугольник
hexagon(100)
turtle.clearscreen()

# соты
side = 50
for _ in range(6):
    turtle.forward(side)
    turtle.right(60)
    hexagon(side)
    turtle.left(120)
turtle.clearscreen()

# цветок из ромбов
for _ in range(10):
    rhombus(100, 60)
    turtle.right(36)
turtle.clearscreen()

# квадраты
turtle.speed(5)
side = 150
while side > 15:
    square(side)
    turtle.forward(10)
    side -= 10
turtle.clearscreen()

#спираль
side = 150
while side > 15:
    for _ in range(2):
        turtle.forward(side)
        turtle.left(90)
        side -= 8
turtle.clearscreen()

# пунктирная линия
turtle.shape('circle')
turtle.penup()
turtle.backward(150)
for i in range(10):
    turtle.forward(30)
    turtle.stamp()
time()
turtle.clearscreen()

# циферблат
turtle.shape('turtle')
turtle.penup()
n = int(12)
for _ in range(n):
    turtle.forward(70)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.stamp()
    turtle.backward(110)
    turtle.left(360/n)
turtle.clearscreen()

#спираль черепашки
turtle.speed(8)
turtle.shape('turtle')
turtle.penup()
n=10
turtle.shape('turtle')
for _ in range(30):
    turtle.forward(n)
    turtle.right(90)
    turtle.stamp()
    turtle.left(90)
    turtle.backward(n)
    turtle.right(20)
    n+=5
turtle.clearscreen()

turtle.Screen().colormode(255)
# цветная спираль
n = 10
for i in range(42):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.pensize((i // 3)+1)
    turtle.left(60)
    turtle.forward(n)
    n+=4
turtle.clearscreen()

#звезда Давида
side = 50
for _ in range(6):
    turtle.forward(side)
    turtle.right(60)
    triangle(side)
turtle.clearscreen()

# Елочка
turtle.pencolor('SeaGreen')
n = 100
for _ in range(10):
    turtle.goto(n, -180)
    turtle.pencolor('SteelBlue')
    turtle.dot()
    turtle.pencolor('SeaGreen')
    turtle.goto(0, 0)
    n -= 20
turtle.pencolor('tomato')
turtle.dot()
turtle.clearscreen()

# изображение символа олимпиады
turtle.penup()
turtle.goto(0, 0)
turtle.pencolor('Black')
turtle.pensize(5)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(-86, 0)
turtle.pencolor('DeepSkyBlue')
turtle.pensize(5)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(86, 0)
turtle.pencolor('Red')
turtle.pensize(5)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(-43, -50)
turtle.pencolor('Yellow')
turtle.pensize(5)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(43, -50)
turtle.pencolor('Green')
turtle.pensize(5)
turtle.pendown()
turtle.circle(40)
turtle.clearscreen()

# мишка мышка
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

turtle.circle(80)
turtle.circle(45)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(10)
turtle.goto(0, -135)

turtle.penup()
turtle.goto(35, -65)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-35, -65)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(61, -10)
turtle.pendown()
turtle.circle(30)

turtle.penup()
turtle.goto(-61, -10)
turtle.pendown()
turtle.circle(30)
turtle.clearscreen()

# снежинки
turtle.hideturtle()
turtle.speed(10)
for _ in range(3):
    snowflake(random.randint(-150, 150), random.randint(-150, 150), random.randint(20, 50))
turtle.clearscreen()

# оптическая иллюзия
turtle.Screen().bgcolor('white')
n = 150
x = []
y = []
turtle.left(90)
for i in range(6):
    turtle.penup()
    turtle.forward(n)
    if i % 2 == 1:
        turtle.dot(n/2)
    x.append(turtle.xcor())
    y.append(turtle.ycor())
    turtle.backward(n)
    turtle.left(60)
turtle.goto(x[4], y[4])
turtle.pendown()
for i in range(0,5,2):
    turtle.goto(x[i], y[i])
turtle.penup()
turtle.pencolor('white')
turtle.fillcolor('white')
turtle.goto(x[5], y[5])
turtle.begin_fill()
turtle.pendown()
for i in range(1,6,2):
    turtle.goto(x[i], y[i])
turtle.end_fill()
time()
turtle.clearscreen()

turtle.Screen().colormode(255)

# цветные круги
n = 400
while n > 20:
    turtle.pencolor('black')
    turtle.dot(n)
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    n -= 1
    turtle.dot(n)
    n -= 20
time()
turtle.clearscreen()

# звезды
turtle.speed(0)
for _ in range(30):
    random_stars()
turtle.clearscreen()

# изображение правильных многоугольников
turtle.speed(8)
for x in range(-160, 170, 75):
    for y in range(-170, 170, 75):
        turtle.penup();
        turtle.goto(x,y)
        turtle.pendown()
        polygon(random.randint(3, 7))
turtle.clearscreen()

# изображение шахматной доски
turtle.penup();
turtle.goto(-200,-200)
turtle.pendown()
turtle.speed(0)
for x in range(-200, 200, 50):
    for y in range(-200, 200, 50):
        turtle.penup();
        turtle.goto(x,y)
        turtle.pendown()
        if (x + y) % 100 == 0:
            turtle.fillcolor('black')
        else:
            turtle.fillcolor('white')
        turtle.begin_fill()
        square(50)
        turtle.end_fill()
turtle.clearscreen()

# изображение компаса
turtle.dot(60)
turtle.dot(57, 'white')
sides = [('Восток', False, 'left', ('Arial', 8, 'normal')),
         ('Север', False, 'center', ('Arial', 8, 'normal')),
         ('Запад', False, 'right', ('Arial', 8, 'normal')),
         ('Юг', False, 'center', ('Arial', 8, 'normal'))]
for side in sides:
    turtle.forward(70)
    turtle.penup()
    turtle.forward(15)
    turtle.write(*side)
    turtle.backward(85)
    turtle.left(90)
    turtle.pendown()
time()
turtle.clearscreen()

# сердце
turtle.hideturtle()
turtle.fillcolor('firebrick')
turtle.begin_fill()
for t in range(650):
    heart(t/100)
turtle.end_fill()
time()

turtle.done()
