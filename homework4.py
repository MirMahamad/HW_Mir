class SeverusSnape:
    def __init__(self, name):
        self.name = name



class BellatrixLestrange:
    def __init__(self, age):
        self.age = age



class DracoMalfoy(SeverusSnape):
    def fear_draco(self):
        print('Fear Draco: Dark, Harry Pother')



class LuciusMalfoy(BellatrixLestrange):
    def fear_lucius(self):
        print('Fear Lucius: Voldemort, Harry Pother')



class Voldemort(DracoMalfoy, LuciusMalfoy):
    def __init__(self, name, age):
        DracoMalfoy.__init__(self, name)
        LuciusMalfoy.__init__(self, age)

    def __str__(self):
        return f' {self.name} {self.age}'

v = Voldemort('Ralph Fiennes', 400)
v.fear_draco()
v.fear_lucius()
print(v)


