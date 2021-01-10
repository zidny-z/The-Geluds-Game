from tabulate import tabulate
import mysql.connector
import os
from classes import *

clear = lambda: os.system('cls')
pagar = str(48 * '#')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="the geluds game"
)

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
     
     # def diserang(self, serangan):
     #      return self.health + serangan

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


print("\n" + pagar + "\n\t\tSelamat Datang!\n" + pagar+"\n\nProfil Anda")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM player")
hasil = mycursor.fetchall()
header = ['ID', 'Nama Anda', 'Health', 'Level','HeroID', 'WeaponID']
myplayer = Player(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])
print()
print(tabulate(hasil, headers=header))


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Hero Where HeroID={}".format(myplayer.hero))
hasil = mycursor.fetchall()
header = ['ID','Nama Hero','Health','Power','Armor']
myhero = Hero(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4])
print()
print(tabulate(hasil, headers=header))

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
hasil = mycursor.fetchall()
header = ['ID',"Nama Senjata","Power"]
myweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
print()
print(tabulate(hasil, headers=header))

#lawan musuh
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Enemy Where EnemyID={}".format(myplayer.level))
hasil = mycursor.fetchall()
header = ['ID',"Nama Musuh","Health","Level","Power","Armor", "Weapon"]
myenemy = Enemy(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5],hasil[0][6])
print("\n\nProfil Musuh\n")
print(tabulate(hasil, headers=header))

#senjata musuh
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
hasil = mycursor.fetchall()
header = ['ID',"Nama Senjata Musuh","Power"]
myenemyweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
print()
print(tabulate(hasil, headers=header))

#tengkare
myMainDamage = myhero.getPower() + myweapon.getPower()
myMainHealth = myplayer.getHealth() + myhero.getHealth()
myMainArmor = myhero.getArmor()

eMainDamage = myenemyweapon.getPower() + myenemy.getPower()
eMainHealth = myenemy.getHealth()
eMainArmor = myenemy.getArmor()


while myMainHealth>0 and eMainHealth>0:

     eMainHealth = eMainHealth - (myMainDamage - myenemy.armor)
     if myMainHealth <= 0:
          myMainHealth = 0
     elif eMainHealth <= 0:
          eMainHealth = 0
     print("HP Musuh :",eMainHealth)

     myMainHealth = myMainHealth - (eMainDamage - myMainArmor)
     if myMainHealth <= 0:
          myMainHealth = 0
     elif eMainHealth <= 0:
          eMainHealth = 0
     print("HP Anda :",myMainHealth)

     if myMainHealth <= 0:
          myMainHealth = 0
          print("\n" + pagar + "\n\t\tAnda Kalah :(\n" + pagar)
     elif eMainHealth <= 0:
          eMainHealth = 0
          print("\n" + pagar + "\n\t\tAnda Menang!\n" + pagar)
     