import random
import sys
import os
battlechance = (random.randint(1,100))

class Location:
        def __init__(self,location,time):
                self.location = location
                self.time = time
class Role:
	def __init__(self,name,health,damage,defence,mana,bmagik,wmagik,level):
		self.name = name
		self.health = health
		self.damage = damage
		self.defence = defence
		self.mana = mana
		self.BMagik = bmagik
		self.WMagik = wmagik
class Monster:
	def __init__(self,monstername,monsterhealth,monsterdamage,monsterdefence,monstermana,monsterbmagik,monsterwmagik,monsterlevel):
		self.name = monstername
		self.health = monsterhealth
		self.damage = monsterdamage
		self.defence = monsterdefence
		self.mana = monstermana
		self.BMagik = monsterbmagik
		self.WMagik = monsterwmagik
class Player:
	def __init__(self,role,name):
		self.name = name
		self.role = role
class Choice:
        def __init__(self,options,choice):
                self.options = options
                self.choice = choice
p = Player(None,None)
def linput(text = None):
        return input(text).lower()

                                
                                
#Role Options
sorcerer = Role("Sorcerer",70,5,5,15,50,15,5)
knight = Role("Knight",100,10,10,15,0,5,5)
summoner = Role("Summoner",70,8,8,10,50,15,5)
ranger = Role("Ranger",80,10,8,10,5,10,5)
rouge = Role("Rouge",90,15,5,5,5,5,5)
#Monsters
fallenAngel = Monster("Fallen Angel",10,5,0,20,10,5,1)
warlock = Monster("Warlock",8,10,0,0,5,0,1)
mindFlayer = Monster("Mind Flayer",10,8,0,15,15,0,1)
lostSoul = Monster("Lost Soul",1,1,0,1,1,1,1)
goblin = Monster("Goblin",5,5,25,5,0,10,1)
miniDragon = Monster("Mini Dragon",8,10,0,25,15,5,1)
randmonster = [fallenAngel, warlock, mindFlayer, lostSoul, goblin, miniDragon]
m = Monster (None,None,None,None,None,None,None,None)
#choice options
options = ["grab the torch", "grab the moss", "find a way out"]
#locations
insidethecave = Location("Inside The Cave", "Inside The Cave")
outsidethecave = Location("Outside The Cave", "Outside The Cave")
#os.system("dragon.jpg ")

print ("Welcome to the world of Thornblood")
print ("What is your name brave explorer")



name = input()




roles = [sorcerer,knight,summoner,ranger,rouge]
while p.role == None:
        print ("Now " + name + " What role would you like to play in this glorious tale?")
        for role in roles:
                print(role.name)
        choice = linput("Selection ")
        for role in roles:
                if role.name.lower() == choice:
                        p.role = role

print("You have selected",p.role.name)

def ChoiceInput ():
        choice = input(">> ")
        if battlechance < 99:
                rcm = (random.choice(randmonster))
                print ("You encounter " + rcm.name)
                print ("What will you do?")
                print ("You can Attack, Defend, and currently in progress WMagik or BMagik")
                action = input()
                while rcm.health > 0:
                        if action == "attack":
                                rcm.health -= p.role.damage
                                p.role.health -= rcm.damage
                                print()
                                print()
                        if action == "defend":
                                rcm.damage -=  p.role.defence
                                        
                                if rcm.damage <= 0:
                                        rcm.damage == 0
                                else:
                                                
                                         p.role.health -= rcm.damage
                                        
                                if rcm.health <= 0:
                                        print ("You killed the " + rcm.name)
#Start of Game
loc = insidethecave
print(loc.location)
while  loc == insidethecave:
        print ("Now young " + p.role.name + " you have awoken in a deep dark cave and all you can hear is the sound of water dripping of the stalactites off the cealing")
        print ("You are alone and you have to make a choice")
        print ("All you can see is some moss and a torch")
        print ("You can " + " ".join(options) + " What will you do?")

        choice = linput(">> ")

        if choice == "find a way out":
                print ("You find a way out")
                loc= outsidethecave
        else:
                if choice == "grab the torch" or "grab torch":
                        print ("You grab the torch")
                        print ("With the light from the torch you notice that the moss is actually a goblin")
                        while goblin.health > 0:
                                print("Goblin has",goblin.health,"health.")
                                print("You have",p.role.health,"health.")
                        
                                print ("You can Attack,Defend,And currently in progress(WMagik,BMagik)")
                                
                                action = linput("What do you do? ")
                                if action == "attack":
                                        goblin.health -= p.role.damage
                                        p.role.health -= goblin.damage
                                if action == "defend":
                                        goblin.damage -=  p.role.defence
                                        
                                if goblin.damage <= 0:
                                        goblin.damage == 0
                                else:
                                                
                                        p.role.health -= goblin.damage
                                        
                                if goblin.health <= 0:
                                        print ("You killed the goblin")
                                        print ("With nothing left to do you leave the cave")
                                        loc = outsidethecave
                else:
                        if choice == "grab the moss" or "grab moss":
                                print ("You find the moss is a goblin")
                                while goblin.health > 0:
                                        print("Goblin has",goblin.health,"health.")
                                        print("You have",p.role.health,"health.")
                                        print ("You can Attack,Defend,And currently in progress(WMagik,BMagik)")
                                        action = linput("What do you do? ")
                                        print ()
                                        if action == "attack":
                                                goblin.health -= p.role.damage
                                                p.role.health -= goblin.damage
                                        if action == "defend":
                                                goblin.damage -=  p.role.defence
                                        
                                                if goblin.damage <= 0:
                                                        goblin.damage == 0
                                                else:
                                                
                                                        p.role.health -= goblin.damage
                                        
                                if goblin.health <= 0:
                                        print ("You killed the goblin")
                                        print ("With nothing left to do you leave the cave")
                                        loc = outsidethecave
                                        
while loc == outsidethecave:
        print ("you are outside the cave!")
        print ("You can go north, go east, go south, go west")
        ChoiceInput()
        if choice == "go north":
                print("You go North")
        else:
                if choice == "go east":
                        print("You go East")
                else:
                        if choice == "go south":
                                print("You go South")
                        else:
                                if choice == "go west":
                                        print("You go West")

