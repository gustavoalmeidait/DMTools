class Mob:
    def __init__(self,name,numberOfMobs, individualMobHp, AC) -> None:
        self.Name = name
        self.HP = numberOfMobs*individualMobHp+1
        self.AC = AC
        self.IndividualHP = individualMobHp
        print("A mob of " + self.Name + " has spawned!")
        print("It boasts " + str(self.alive()) + " strong.")

    alive= lambda self: int(self.HP/self.IndividualHP)
    def TakeDamage(self, damage):
        print("The MurderHob....players...deal " + str(damage) + " damage.")
        previousDamage = int((self.HP) / self.IndividualHP) 
        self.HP=self.HP-damage
        afterDamage = int((self.HP) / self.IndividualHP) 
        numberOfLosses = previousDamage- afterDamage
        #alive = int(self.HP/self.IndividualHP)
        if numberOfLosses==0 :
            print("By CROM!! The mob holds strong!")
        else:
             print("TRAGEDY! The mob suffers " + str(numberOfLosses) + " casualties!")
        
        

    def Status(self):
        print("The mob of " + self.Name + " has " + str(self.HP) + " pints of blood remaining.")
        print(str(self.alive() ) +" creatures remain alive.")
        print ("AC: " + str(self.AC))

    def TakeDamageArea(self, damage, area):
        print("The maniatics cause mayhem in a " + str.upper( area) + " area.")
        if area =="small":
            #Small hits 4 creatures
            i=0
            while i<4:
                self.TakeDamage(damage)
                i+=1
        
        if area=="medium":
            #Medium hits 8
            i=0
            while i<8:
                self.TakeDamage(damage)
                i+=1
        
        if area=="large":
        #Large hits 16
            i=0
            while i<16:
                self.TakeDamage(damage)
                i+=1
        
        if area=="huge":
            i=0
            while i<32:
                self.TakeDamage(damage)
                i+=1
            
        
        
atacantes= Mob("kobolds",10,3,14)

atacantes.TakeDamage(4)
atacantes.Status()
print()
atacantes.TakeDamageArea(1,"small")
atacantes.Status()


