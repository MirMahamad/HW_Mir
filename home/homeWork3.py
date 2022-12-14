class SuperHero:
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def realname(self):
         return f'{self.name}'
    def hpx2(self):
        return f'{self.health_points*2}'
    def __str__(self):
        return  f'{self.nickname, self.superpower, self.health_points}'
    def __int__(self):
        return len(self.catchphrase)
Hero=SuperHero('Ben', 'Batman','деньги',200,'все хотят от меня шоу')
Hero.realname()
Hero.hpx2()

print(Hero.realname())
print(Hero.hpx2())

class Earth(SuperHero):
    sign = True
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hpx2(self):
        return f'{self.health_points ** 2}'
    def fly_h(self):
        self.fly=True

    def phrase(self):
        print('fly in the True_phrase')


Earth_h = Earth('Bob', 'Stebel', 'laser', 100, 'babushka boi', 100, True)
Earth_h.hpx2()
Earth_h.phrase()
print(Earth_h.hpx2())


class Air(SuperHero):
    cape = True
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        SuperHero.__init__(self,name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hpx2(self):
        return  f'{self.health_points **2}'
    def fly_h(self):
        self.fly=True

    def phrase(self):
         print('fly in the True_phrase')

Air_h = Air('carl','invisy', 'invisible', 30, 'where am i', 100, True)
Air_h.hpx2()
Air_h.phrase()
print(Air_h.hpx2())


class Villain(Air):
    people = 'monster'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase,damage,fly)
    def gen_x(selfs):
        pass
    def crit(self):
        print(f'{self.damage**2}')
evil = Villain('Ivan','kuvalda','strength',300,'я бью 2 раза', 100, True)
print(Villain.crit(Air_h))

class Bank:
    def __init__(self, name, balanse):
        self.__name = name
        self.__balanse = balanse

    def setbalanse(self, balanse):
        self.__balanse = balanse

    def getbalanse(self):
        return self.__balanse
    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def moneyX(self):
        user = input('Введите сумму, на которую хотите пополнить баланс: ')
        return f'Ваш счет успешно пополнен, баланс: {self.__balanse + int(user)}'

    def __str__(self):
        return f'Имя {self.__name} \n' \
               f'Баланс {self.__balanse}'

    def __kill(self):
        a = input('если хотите обналичить деньги введите <kill> ')
        if a == "kill":
            return f'ваш баланс обналичился - {self.__balanse * 0}'

    def _jackpot(self):
        return f'{self.__balanse * 10}'

    def _protected_join(self, other):
        self.__balanse += other.balance

class Mir:

    def __init__(self, balance):
        self.balance = balance

h1 = Bank('10', 100)
print(h1.moneyX())
print(h1._jackpot())
print(h1._Bank__kill())
almaz = Bank('almaz', 100)
ismar = Mir(100)
almaz._protected_join(ismar)