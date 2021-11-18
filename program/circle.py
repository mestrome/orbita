from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *
from cartesian_plane import CartesianPlane

from vector import Vector3d

from math import *


class Circle:
    def __init__(self):
        self.vectors = []
        self.var = 0

    def show(self, radius, stacks, sectors):
        
        for i in range(0,stacks+1):
            phi = -pi/2 + i*pi/stacks
            temp = radius*cos(phi)
            y = radius*sin(phi)
            for j in range(0,sectors+1):
                theta = j*2*pi/sectors
                x = temp*sin(theta)
                z = temp*cos(theta)

                self.vectors.append(Vector3d(x,y,z))
                

    def update(self):
        self.show(10,5,10)

        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glLoadIdentity()
        glTranslatef(0,0,-100)
        self.var += 1
        

        glPushMatrix()
        
        
        glColor3fv((1,0,0))
        glPointSize(5)
        glBegin(GL_POINTS)
        for point in self.vectors:
            if point.z > 0:
                glVertex3fv(point.get())
        glEnd()
        
        v = []
        for point in self.vectors:
            vt = Vector3d(point.x, point.y, point.z)
            vt.rotate(Vector3d(self.var,0,0), Vector3d(0,0,0))
            v.append(vt)
        self.vectors = v
        
        self.var += 90

        
        glPopMatrix()

        


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.render.append(Circle())
        app.run()