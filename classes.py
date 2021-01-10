from tabulate import tabulate
import mysql.connector
import os

clear = lambda: os.system('cls')
pagar = str(48 * '#')

class Pemain:
     def __init__(self,idnya,nama,health,level,weapon):
          self.__id = idnya
          self.nama = nama
          self.health = health
          self.level = level
          self.weapon = weapon
     
     def getId(self):
          return self.__id
     
     def getLevel(self):
          return self.level
     
     def getHealth(self):
          return self.health
     
     def getNama(self):
          return self.nama
     
     def diserang(self, serangan):
          return self.health + serangan

class Player(Pemain):
     def __init__(self,idnya,nama,health,level,hero,weapon):
          super().__init__(idnya,nama,health,level,weapon)
          self.hero = hero
     
     
class Enemy(Pemain):
     def __init__(self,idnya,nama,health,level,power,armor,weapon):
          super().__init__(idnya,nama,health,level,weapon)
          self.power = power
          self.armor = armor
     
     def getArmor(self):
          return self.armor

     def getPower(self):
          return self.power
     

class Weapon:
     def __init__(self, idnya , nama, power):
          self.id = idnya
          self.nama = nama
          self.power = power
     
     def getPower(self):
          return self.power

     def getId(self):
          return self.__id

class Hero:
     def __init__(self, idnya, nama, health, power, armor):
          self.id = idnya
          self.nama = nama
          self.health = health
          self.power = power
          self.armor = armor
     
     def getNama(self):
          return self.nama
     
     def getHealth(self):
          return self.health
          
     def getPower(self):
          return self.power
     
     def getArmor(self):
          return self.armor


a = Player(1,'aku',100,1,1,1)
print(a.getId())

