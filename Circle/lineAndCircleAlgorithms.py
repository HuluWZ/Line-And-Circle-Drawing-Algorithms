from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


# Draw Point on Circle Drawing Algorithms throughout 360 Degree (8 Sections 45 Degree each)
def CirclePlotPoints(x_centre, y_centre, x, y):
    glVertex2i(x_centre + x, x_centre + y)
    glVertex2i(x_centre - x, y_centre + y)
    glVertex2i(x_centre + x, y_centre - y)
    glVertex2i(x_centre - x, y_centre - y)
    glVertex2i(x_centre + y, y_centre + x)
    glVertex2i(x_centre - y, y_centre + x)
    glVertex2i(x_centre + y, y_centre - x)
    glVertex2i(x_centre - y, y_centre - x)


###################    LINE DRAWING ALGORITHMS
# Direct Use Line Of Equation Algorithm
def LineDirect(x1, y1, x2, y2):

    deltaX = x2 - x1
    deltaY = y2 - y1
    m = deltaY / deltaX
    b = y1 - m * x1

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.5)

    if abs(m) <= 1:
        for x in range(x1 + 1, x2):  # Starting with x1+1 and Excluding x2
            y = m * x + b  # Get Y from M*x+b
            glVertex2f(x, y)
    else:
        for y in range(y1 + 1, y2):
            x = (y - b) / m  # Compute X from y = mx+b  x= (y-b)/m
            glVertex2f(x, y)

    glEnd()
    glFlush()


# DDA(Digital Differential Analyzer) Algorithm
def LineDDA(x1, y1, x2, y2):

    # 1. Calculate change in X and Y.
    deltaX = x2 - x1
    deltaY = y2 - y1
    # 2. Calculate Steps.
    steps = 0
    if abs(deltaX) > abs(deltaY):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    # 3. Calculate X & Y increment.
    Xincrement = deltaX / steps
    Yincrement = deltaY / steps

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.5)

    for step in range(1, steps + 1):  # Loops from 1 to n for n steps
        glVertex2f(round(x1), round(y1))  # Plot the point at (x1,y1)
        x1 = x1 + Xincrement  # update x1 to next X cordinate
        y1 = y1 + Yincrement  # update y1 to next Y cordinate

    glEnd()
    glFlush()


# Bresenham Algorithm
def LineBresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dT = 2 * abs(dy - dx)
    dS = 2 * dy
    d = 2 * abs(dy - dx)
    y = y1

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.5)
    glPointSize(4.0)
    glBegin(GL_POINTS)

    for x in range(x1, x2 + 1):
        glVertex2f(x, y)
        d = d + dS
        if d >= 0:
            y = y + 1
            d = d + dT
    glEnd()
    glFlush()


####################  CIRCLE DRAWING ALGORITHMS
# Bresenham Circle Drawing Algorithm
def BresenhamCircleDraw(x_centre, y_centre, r):
    x = 0
    y = r

    # CirclePlotPoints(x_centre, y_centre, x, y)

    D = 3 - 2 * r

    glColor3f(0.0, 1.0, 0.5)
    glPointSize(2.0)
    glBegin(GL_POINTS)

    while x <= y:
        # A Method for rotating through 360 Degree (8 Sections)
        CirclePlotPoints(x_centre, y_centre, x, y)
        if D < 0:
            x += 1
            D = D + 4 * x + 6

        else:
            x += 1
            y -= 1
            D = D + 4 * (x - y) + 10

    glEnd()
    glFlush()


# MidPoint Circle Drawing Algorithm
def MidPointCircleDraw(x_centre, y_centre, r):
    x = 0
    y = r

    D = 1 - r

    glColor3f(0.0, 1.0, 0.5)
    glPointSize(2.0)
    glBegin(GL_POINTS)

    while x <= y:
        # A Method for rotating through 360 Degree (8 Sections)
        CirclePlotPoints(x_centre, y_centre, x, y)

        if D < 0:
            D = D + 2 * x + 1

        else:
            y -= 1
            D = D + 2 * (x - y) + 1

        x += 1

    glEnd()
    glFlush()


## Main Function
def main():
    # Ask for choice
    choice = 0
    while choice != 3:
        choice = input(
            "\n Please Choose What You Want  \n\t1. Plot A Line \n\t2. Plot A Circle \n\t3. Exit\n"
        )
        if int(choice) == 1:
            x1 = int(input("Enter X1: "))
            y1 = int(input("Enter Y1: "))
            x2 = int(input("Enter X2: "))
            y2 = int(input("Enter Y2: "))

            print("\n Choose Algorithm To Draw Line")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(0, 0)

            typeOfAlgorithm = int(
                input(
                    "\n\n 1. Direct Line Equation \n 2. DDA \n 3. Bresenham's \n \t\t"
                )
            )
            if int(typeOfAlgorithm) == 1:
                glutCreateWindow("Line using Direct use of Line Equation Algorithm")
                init()
                glutDisplayFunc(lambda: LineDirect(x1, y1, x2, y2))
                glutIdleFunc(lambda: LineDirect(x1, y1, x2, y2))
                # init()
                glutMainLoop()

            elif int(typeOfAlgorithm) == 2:
                glutCreateWindow("Line using DDA Algorithm")
                init()
                glutDisplayFunc(lambda: LineDDA(x1, y1, x2, y2))
                glutIdleFunc(lambda: LineDDA(x1, y1, x2, y2))
                glutMainLoop()

            elif int(typeOfAlgorithm) == 3:
                glutCreateWindow("Line using Bresenham's Algorithm")
                init()
                glutDisplayFunc(lambda: LineBresenham(x1, y1, x2, y2))
                glutIdleFunc(lambda: LineBresenham(x1, y1, x2, y2))
                glutMainLoop()

            else:
                print("Invalid choice /n/t Insert From 1 To 3")
                typeOfAlgorithm = 0

        elif int(choice) == 2:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\n\tRadius: "))

            print("\nChoose Algorithm To Draw Circle")

            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(0, 0)

            typeOfAlgorithm = int(input("\n\n 1. Bresenham's \n 2. Mid Point \n \t\t"))

            if int(typeOfAlgorithm) == 1:
                glutCreateWindow("Circle using Bresenham's Algorithm")
                glutDisplayFunc(lambda: BresenhamCircleDraw(x, y, r))
                glutIdleFunc(lambda: BresenhamCircleDraw(x, y, r))
                init()
                glutMainLoop()
            elif int(typeOfAlgorithm) == 2:
                glutCreateWindow("Circle using Mid Point Algorithm")
                glutDisplayFunc(lambda: MidPointCircleDraw(x, y, r))
                glutIdleFunc(lambda: MidPointCircleDraw(x, y, r))
                init()
                glutMainLoop()
            else:
                print("Invalid choice /n/t Insert From 1 To 2")
                typeOfAlgorithm = 0

        else:
            print("Invalid choice")
            choice = 0


main()
