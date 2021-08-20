class Mob:
    def __init__(self,name,numberOfMobs, individualMobHp, AC) -> None:
        self.Name = name
        self.HP = numberOfMobs*individualMobHp+1
        self.AC = AC
        self.IndividualHP = individualMobHp
        self.Status()

    def TakeDamage(self, damage):
        print("The MurderHob....players...deal " + str(damage) + " damage.")
        previousDamage = int((self.HP) / self.IndividualHP) 
        self.HP=self.HP-damage
        afterDamage = int((self.HP) / self.IndividualHP) 
        numberOfLosses = previousDamage- afterDamage
        alive = int(self.HP/self.IndividualHP)
        if numberOfLosses>0 :
            print("By CROM!! The mob holds strong!")
        else:
             print("TRAGEDY! The mob suffers " + str(numberOfLosses) + " casualties!")
        print(str(alive ) +" creatures remain alive.")
        self.Status()

    def Status(self):
        print("The mob of " + self.Name + " has " + str(self.HP) + " pints of blood remaining.")
        print ("AC: " + str(self.AC))
        
atacantes= Mob("kobolds",10,3,14)

atacantes.TakeDamage(15)
