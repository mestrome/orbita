from app import App

from OpenGL.GL import *

from vector import Vector3d


class Cube3d:
    def __init__(self, verticies, faces):
        self.__verticies__ = verticies
        self.verticies = verticies
        self.faces = list(faces)
        self.color = (1,1,1)
        self.angle = Vector3d(0,0,0)

    def rotate(self):
        new_verticies = []

        for vertex in self.__verticies__:
            vector = Vector3d(vertex[0], vertex[1], vertex[2])
            vector.rotate(self.angle, Vector3d(0,0,0))
            new_verticies.append(vector.get())
            
        self.verticies = tuple(new_verticies)

        if abs(self.angle.x) >= 360:
            self.angle.x = 0
        if abs(self.angle.y) >= 360:
            self.angle.y = 0



    def show(self):
        glBegin(GL_QUADS)
        for face in self.faces:
            for vertex in face:
                if type(vertex) == tuple:
                    glColor3fv(vertex)
                elif type(vertex) == int:
                    glVertex3fv(self.verticies[vertex])
        glEnd()
        


    def update(self):
        self.show()
        self.rotate()



cuboVerticies = (
    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),

    (0,0,-1),
    (1,0,-1),
    (1,1,-1),
    (0,1,-1),
)

cuboFaces = (
    ((0.1,0.1,0.1),4,5,6,7),    #1
    ((1,0,0),0,1,2,3),          #3
)

cuboFacesbc= (
    ((1,0,0),0,1,2,3),          #3
    ((1,1,0),0,1,5,4),          #4
    ((1,1,1),0,4,7,3),          #5
    ((0,1,1),3,2,6,7),          #2
    ((0,0,1),1,2,6,5),          #6
    ((0.1,0.1,0.1),4,5,6,7),    #1
)

if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.screenSize = (1500,900)
        app.render.append(CartesianPlane())
        app.render.append(Cube3d(cuboVerticies, cuboFacesbc))
        app.run()
