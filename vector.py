import math

class Vector3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def rotate(self, angle, center):
        new_vector = Vector3d()

        
        if abs(angle.x) > 0:
            new_vector.z = ((self.y-center.y) * math.cos((angle.x/180)*math.pi)) - ((self.z-center.z) * math.sin((angle.x/180)*math.pi))
            new_vector.y = ((self.y-center.y)* math.sin((angle.x/180)*math.pi)) + ((self.z-center.z) * math.cos((angle.x/180)*math.pi))
            self.z = center.z + new_vector.z
            self.y = center.y + new_vector.y


        if abs(angle.y) > 0:
            new_vector.x = ((self.z-center.z) * math.cos((angle.y/180)*math.pi)) - ((self.x-center.x) * math.sin((angle.y/180)*math.pi))
            new_vector.z = ((self.z-center.z)* math.sin((angle.y/180)*math.pi)) + ((self.x-center.x) * math.cos((angle.y/180)*math.pi))
            self.x = center.x + new_vector.x
            self.z = center.z + new_vector.z
            

        if abs(angle.z) > 0:
            new_vector.x = ((self.y-center.y) * math.cos((angle.z/180)*math.pi)) - ((self.x-center.x) * math.sin((angle.z/180)*math.pi))
            new_vector.y = ((self.y-center.y)* math.sin((angle.z/180)*math.pi)) + ((self.x-center.x) * math.cos((angle.z/180)*math.pi))
            self.x = center.x + new_vector.x
            self.y = center.y + new_vector.y
        
        


    def get(self):
        return (self.x, self.y, self.z)
