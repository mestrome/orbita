from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *
from cartesian_plane import CartesianPlane

from vector import Vector3d

import pygame
from math import *


class Circle:

    # FUNÇÃO QUALQUER PARA SER REPRESENTADA
    def f(self, x):
        return x*x

    def g(self, x,y, angle):
        return ( (y * cos((angle/180)*pi)) - (x * sin((angle/180)*pi)), (y * sin((angle/180)*pi)) + (x * cos((angle/180)*pi)))


    def parabola(self):
        tam = 10
        dx = 0.1


        glBegin(GL_LINES)
        glColor3f(0,1,0.7)

        x = -tam
        while -tam <= x <= tam:

            glVertex3f(x, self.f(x), 0)
            glVertex3f(x+dx, self.f(x+dx), 0)

            x += dx
            
        glEnd()

    def circle(self, angle_z=0):
        angle = 0
        dz = 10
        rain = 5

        glBegin(GL_LINES)
        glColor3f(0,1,0.7)

        
        while 0 <= angle < 360:

            glVertex3f(self.g(0,rain,angle)[0], self.g(0,rain,angle)[1], angle_z)
            glVertex3f(self.g(0,rain,angle+dz)[0], self.g(0,rain,angle+dz)[1], angle_z)

            angle += dz
            
        glEnd()

    def esfera(self):
        angle = 0
        dy = 10

        while 0 <= angle < 360:
            self.circle(self.g(0,5,angle)[1])
            angle += dy
        

        

    def update(self):
        self.circle()
        self.esfera()


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.render.append(CartesianPlane())
        app.render.append(Circle())
        app.run()