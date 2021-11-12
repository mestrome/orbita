import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class App:
    def __init__(self):
        self.rot = 0
        self.render = []
        self.speed = 3
        self.sum_rot_updown = 0
        self.current_mv_mat = (GLfloat * 16)()
        self.screenSize = (500, 500)

    def run(self):
        pygame.init()

        
        pygame.display.set_mode(self.screenSize, DOUBLEBUF | OPENGL)

        clock = pygame.time.Clock()

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.screenSize[0] / self.screenSize[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)   
        glEnable(GL_DEPTH_TEST)
        glTranslate(0, 0, -50 / self.speed)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            glGetFloatv(GL_MODELVIEW_MATRIX, self.current_mv_mat)
            glLoadIdentity()

            # Rotation Right and Left
            if pressed[pygame.K_LEFT]:
                glRotatef(self.speed / 2, 0, -1, 0)
                self.rot += 1

            if pressed[pygame.K_RIGHT]:
                glRotatef(self.speed / 2, 0, 1, 0)
                self.rot -= 1

            

            # Walk with WASD
            if pressed[pygame.K_w]:
                glTranslate(0, 0, 1 / self.speed)
            if pressed[pygame.K_s]:
                glTranslate(0, 0, -1 / self.speed)
                
            if pressed[pygame.K_a]:
                glTranslate(1 / self.speed, 0, 0)
            if pressed[pygame.K_d]:
                glTranslate(-1 / self.speed, 0, 0)

            # Walk Up and Down With ESPACE and SHIFT
            if pressed[pygame.K_SPACE]:
                glTranslate(0, -1 / self.speed, 0)
            if pressed[pygame.K_LSHIFT]:
                glTranslate(0, 1 / self.speed, 0)

            glMultMatrixf(self.current_mv_mat)

            # Rotation Up and Down
            if pressed[pygame.K_UP]:
                self.sum_rot_updown -= self.speed / 2
            if pressed[pygame.K_DOWN]:
                self.sum_rot_updown += self.speed / 2

            # Rotation with Mouse
            mouse_rel = pygame.mouse.get_rel()

            # Rotation Up and Down with Mouse
            if pygame.mouse.get_pressed()[0]:
                if mouse_rel[1] > 0:
                    self.sum_rot_updown += self.speed / 2
                elif mouse_rel[1] < 0:
                    self.sum_rot_updown -= self.speed / 2


            # Rotation Right and Left with Mouse
            if pygame.mouse.get_pressed()[0]:
                if mouse_rel[0] < 0:
                    glRotatef(self.speed / 2, 0, -1, 0)
                    self.rot += 1
                elif mouse_rel[0] > 0:
                    glRotatef(self.speed / 2, 0, 1, 0)
                    self.rot -= 1
            

            glPushMatrix()

            glGetFloatv(GL_MODELVIEW_MATRIX, self.current_mv_mat)
            glLoadIdentity()
            glRotatef(self.sum_rot_updown, 1, 0, 0)
            glMultMatrixf(self.current_mv_mat)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            for render in self.render:
                render.update()

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)