class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def name_hero(self):
        return (f'Имя нашего героя {self.name}')
    def hp(self):
        print(f'Здоровье нашего героя {self.health_points * 2}')
    def __str__(self):
        return (f'Его прозвище {self.nickname} \n'
               f'Его суперспособность {self.superpower} \n'
               f'Его количество здоровья {self.health_points}')
    def __len__(self):
        print('Количество букв в коронной фразе ', len(self.catchphrase))

a = SuperHero("Anthony Edward Stark", "Iron man", "Immortality", 1000, "I'll take it apart, drown the motherboard and make a hanger out of you")
print(a)
print(a.name_hero())
print(a.hp())
print(a.__len__())

class FlyHero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_point, catchphrase, fly, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.fly = fly
        self.fly = False
        self.damage = damage

    def hp(self):
        self.fly = True
        return (f'Здоровье нашего героя {self.health_points ** 2}')
    def __str__(self):
        return 'fly in the True_phrase'

a = FlyHero('Clark Joseph Kent','SuperMan','speed',100, "Loving another is hard, but hating is easy", "in the True_phrase", 100)
print(a)
print(a.name_hero())
print(a.hp())
print(a.__len__())
print(a.__str__())



class SpaceHero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_point, catchphrase, fly, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.fly = fly
        self.fly = False
        self.damage = damage

    def hp(self):
        self.fly = True
        return (f'Здоровье нашего героя {self.nickname} {self.health_points ** 2}')

b = SpaceHero('Peter Jason Quill', 'Star Lord', 'dexterity', 200, "Don`t choke on your ambitions", "in the True_phrase", damage= 1000)
print(b)
print(b.name_hero())
print(b.hp())
print(b.__len__())
print(b.damage)

class Villiain(SpaceHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, fly, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, fly, damage)
    def gen_x(self):
        pass
    def crit(self):
        return (f"Критический урон героя {self.nickname} {self.damage **2}")

c = Villiain('Anakin Skywalker', 'Darth Vader', 'anger', 50, "Luke, I'm your father!", "in the True_phrase", 190)
print(c)
print(c.name_hero())
print(c.hp())
print(c.__len__())
print(c.__str__())
print(c.crit())
print(Villiain.crit(b))
print(Villiain.crit(a))