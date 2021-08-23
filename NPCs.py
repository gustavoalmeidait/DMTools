import json
# import pickle
import jsonpickle

class NPC(object):
    # Name =""
    # Quests= []
    # Items=[]    


    def __init__(self,Name) -> None:
        self.Name= Name
        self.Quests = []
        self.Items =[]

    def AddQuest (self, questName, questType):
        quest = {"Name":questName,
                "Type":questType}

        self.Quests.append(questName)

    def AddItem(self,itemName, itemType,itemRarity):
        item = {"Name": itemName,
                "Type":itemType,
                "Rarity":itemRarity}
        self.Items.append(item)

joe = NPC("Joe")
joe.AddQuest("Zaa's revenge","Optional")
joe.AddItem("Zaa's Pride","Boots","Rare")

print(joe.Quests.pop())

NPCsList={}
NPCsList["joe"] =joe


# sal = NPC("sal")
# print(sal.Quests.pop())














# with open("NPCs.json","w") as outfile:
#     json.dump(NPCsList,outfile,default=vars)

# print (NPCsList)
# print(jsonpickle.encode(NPCsList))
# print(jsonpickle.dumps(NPCsList).encode("utf-8"))

# with open("jsonPickledFile.json","w") as f:
#     f.write(jsonpickle.dumps(NPCsList))



#save binary
# pickle.dump(NPCsList,open("pickleNPCs.p","wb"))



# def dump(obj):
#   for attr in dir(obj):
#     print("obj.%s = %r" % (attr, getattr(obj, attr)))

#read
# NewNPCsList=  pickle.load(open("pickleNPCs.p","rb"))
# dump(NewNPCsList)
# from pprint import pprint
# pprint(NewNPCsList)

