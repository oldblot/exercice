class Chrono :

    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s
    def conversion(self):
        s = self._temps
        return (s // 3600, (s // 60) % 60, s % 60)
    def _str_(self):
        h, m, s = self._conversion()
        return (str(h) + "h " + str(m) + "m " + str(s) + "s")
    def avance(self, s):
        self.secondes += s
        self.minutes += self.secondes // 60
        self.secondes = self.secondes % 60
        self.heures += self.minutes // 60
        self.minutes = self.minutes % 60
    def _eq_(self, u):
        return (self.heures == u.heures
            and self.minutes == u.minutes
            and self.secondes == u.secondes)
    

t = Chrono(22,22,22)
#u = t.clone()
t.avance(158)
print(t)
#print(u)