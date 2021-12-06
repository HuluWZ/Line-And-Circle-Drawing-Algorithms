# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def LineBresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dT = 2 * abs(dy - dx)
    dS = 2 * dy
    d = 2 * abs(dy - dx)
    y = y1

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
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


def main():
    # Ask for choice
    choice = 0
    while choice != 2:
        choice = input(
            "Please Choose \n\t1. Plot a Line using Bresenham's Algorithm\n\t2. Exit\n"
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
            glutCreateWindow("Plot Line using Bresenham Algorithm")
            glutDisplayFunc(lambda: LineBresenham(x1, y1, x2, y2))
            glutIdleFunc(lambda: LineBresenham(x1, y1, x2, y2))
            init()
            glutMainLoop()
        else:
            print("Invalid choice")
            choice = 0


main()
