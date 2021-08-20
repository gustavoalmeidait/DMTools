import random

DiceRoll = lambda modifier: random.randrange(1,20) + modifier
DiceRollAdvantage = lambda modifier : max([DiceRoll(modifier),DiceRoll(modifier)])
DiceRollDisadvantage = lambda modifier : min([DiceRoll(modifier),DiceRoll(modifier)])

class Mob:
    def __init__(self,name,numberOfMobs, individualMobHp, AC, will) -> None:
        self.OriginalNumberOfMobs = numberOfMobs
        self.Name = name
        self.HP = numberOfMobs*individualMobHp+1
        self.IndividualHP = individualMobHp
        self.AC = AC
        self.Will = will
        self.Defeated = False
        print("A mob of " + self.Name + " has spawned!")
        print("It boasts " + str(self.alive()) + " strong.")

    alive= lambda self: int(self.HP/self.IndividualHP)
    def TakeDamage(self, damage):
        print("The MurderHob....players...deal " + str(damage) + " damage.")
        previousDamage = int((self.HP) / self.IndividualHP) 
        self.HP=self.HP-damage
        afterDamage = int((self.HP) / self.IndividualHP) 
        numberOfLosses = previousDamage- afterDamage
      
        if numberOfLosses==0 :
            print("By CROM!! The mob holds strong!")
        else:
            if self.alive()>0:
                print("TRAGEDY! The mob suffers " + str(numberOfLosses) + " casualties!")
                self.MoraleCheck()
            else:
                print("THE DM FORCES HAD BEEN DEFEATED AGAAAAAAAIIIIIiiiiiiinnnnnnnnn.......")
                self.Defeated=True
        
        

    def Status(self):
        #for cinematic effect, the last mob dies even if it has some HP left in the tank.
        #it faints, if you will :-P
        if self.alive()>0 and self.Defeated==False: 
            print(str(self.alive() ) +" creatures remain alive.")
            print("The mob of " + self.Name + " has " + str(self.HP) + " pints of blood remaining.")
            print ("AC: " + str(self.AC))
        else:            
            print("The DM grumbles low....vengeance...fucking dices...not fair....")

    def TakeDamageArea(self, damage, area):
        print("The maniatics cause mayhem in a " + str.upper( area) + " area.")
        if area =="small":
            #Small hits 4 creatures
            i=0
            while i<4 and self.alive()>0 and self.Defeated==False:
                self.TakeDamage(damage)
                i+=1
        
        if area=="medium":
            #Medium hits 8
            i=0
            while i<8 and self.alive()>0 and self.Defeated==False:
                self.TakeDamage(damage)
                i+=1
        
        if area=="large":
            #Large hits 16
            i=0
            while i<16 and self.alive()>0 and self.Defeated==False:
                self.TakeDamage(damage)
                i+=1
        
        if area=="huge":
            #huge hits 32
            i=0
            while i<32 and self.alive()>0 and self.Defeated==False:
                self.TakeDamage(damage)
                i+=1
    
   
    def Bloodied(self):
        #love the Bloodied condition from 4th Ed
        if (self.OriginalNumberOfMobs/2) < self.alive():
            print("Plenty of buggers to mess yo day, yippie ky yay...")
            return False
        else:
            print("This washn't shuposshed to happan to ushhhh!")
            return True

    def Rekt(self):
        if (self.OriginalNumberOfMobs/4) > self.alive():
            print("Moooooooo mmmyyyy yy yy yy y")
            return True
        else:
            return False


    def MoraleCheck(self):
        checkResult=0
        #only check when your band of merry fellas is not so merry anymore
        if self.Bloodied():            
            if self.Rekt():
                #despair in the air
                checkResult = DiceRollDisadvantage(self.Will)
            else:
                checkResult= DiceRoll(self.Will)
        
            print("The strenght of will is: " + str(checkResult))
            if checkResult <10:
                print("Noone's payin' me nuff for this crap! Fuggedaboutid! RUUUUUNNNN!!!!111!!")    
                self.Defeated=True        
            else:
                print("This' but a scratch.")
            
        
        
atacantes= Mob("kobolds",10,3,14,-2)

atacantes.TakeDamage(4)
atacantes.Status()
print()
atacantes.TakeDamageArea(1,"huge")
atacantes.Status()


