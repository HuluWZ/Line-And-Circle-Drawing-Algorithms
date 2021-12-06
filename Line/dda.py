# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


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
    glColor3f(1.0, 0.0, 0.0)

    for step in range(1, steps + 1):  # Loops from 1 to n for n steps
        glVertex2f(round(x1), round(y1))  # Plot the point at (x1,y1)
        x1 = x1 + Xincrement  # update x1 to next X cordinate
        y1 = y1 + Yincrement  # update y1 to next Y cordinate

    glEnd()
    glFlush()


def main():
    # Ask for choice
    choice = 0
    while choice != 2:
        choice = input(
            "Please Choose \n\t1. Plot a Line using DDA ALgorithm\n\t2. Exit\n"
        )
        if int(choice) == 1:
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(0, 0)
            glutCreateWindow("Plot Line using DDA Algorithm")
            glutDisplayFunc(lambda: LineDDA(x1, y1, x2, y2))
            glutIdleFunc(lambda: LineDDA(x1, y1, x2, y2))
            init()
            glutMainLoop()
        else:
            print("Invalid choice")
            choice = 0


main()
