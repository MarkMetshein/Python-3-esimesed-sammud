#IT20
#Mark Metshein
#Harjutus 8
#09.12.2020
class auto:
    #atribuudid
    automark = "teadmata"
    aasta = 0
    hind = 0

    #meetodid
    def __init__(self,x,y):
        self.automark = x
        self.aasta = y

    def kuva(self):
        print('Automark: {} \nAasta: {}'.format(self.automark, self.aasta))

    def lisaHind(self,x):
        self.hind = x

    def kuvaHind(self):
        print('Hind: {}'.format(self.hind))

uusObjekt = auto("Audi", 2004)
uusObjekt.lisaHind('2000€')
uusObjekt.kuva()
uusObjekt.kuvaHind()