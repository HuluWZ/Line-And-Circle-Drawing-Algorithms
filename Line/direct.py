# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def LineDirect(x1, y1, x2, y2):

    deltaX = x2 - x1
    deltaY = y2 - y1
    m = deltaY / deltaX
    b = y1 - m * x1

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)

    if abs(m) <= 1:
        for x in range(x1 + 1, x2):
            y = m * x + b  # Get Y from M*x+b
            glVertex2f(x, y)
    else:
        for y in range(y1 + 1, y2):
            x = (y - b) / m  # Compute X from y = mx+b  x= (y-b)/m
            glVertex2f(x, y)

    glEnd()
    glFlush()


def main():
    # Ask for choice
    choice = 0
    while choice != 2:
        choice = input(
            "Please Choose \n\t1. Plot a Line Using Direct Use Algorithm \n\t2. Exit\n"
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
            glutCreateWindow("Plot Line using Direct Algorithm")
            glutDisplayFunc(lambda: LineDirect(x1, y1, x2, y2))
            glutIdleFunc(lambda: LineDirect(x1, y1, x2, y2))
            init()
            glutMainLoop()
        else:
            print("Invalid choice")
            choice = 0


main()
