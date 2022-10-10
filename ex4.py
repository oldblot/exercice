from math import*


class Angle :

    def __init__(self, angle):
        self.angle = angle
        if self.angle < 0 and self.angle > 360 :
            raise ValueError("Angle doit être compris entre 0 et 360 inclu")

    def __str__(self):
        str(self.angle), " degrés"

    def ajoute(self, autre):
        if autre.angle >= 0 and autre.angle <= 360 :
            self.angle += autre.angle
        else :
            raise ValueError("Angle doit être compris entre 0 et 360 inclu")

    def __convertir__(self):
        self.angle = self.angle * (pi/180)
    
    def cos(self):
        self.cos = cos(self.angle)

    def sin(self):
        self.sin = sin(self.angle)

    

    


    
