from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *

class CartesianPlane:
    def __init__(self):
        pass

    def show(self):
        glBegin(GL_LINES)
        # X
        glColor3f(0.3,0,0)
        glVertex3f(-1000,0,0)
        glVertex3f(1000,0,0)
        # Y
        glColor3f(0,0.3,0)
        glVertex3f(0,-1000,0)
        glVertex3f(0,1000,0)
        # Z
        glColor3f(0,0,0.3)
        glVertex3f(0,0,-1000)
        glVertex3f(0,0,1000)

        glEnd()

    def update(self):
        self.show()
        
if __name__=="__main__":
        app = App()
        app.speed = 1
        app.render.append(CartesianPlane())
        app.run()