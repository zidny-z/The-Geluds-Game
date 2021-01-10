from tabulate import tabulate
import mysql.connector
import os
from classes import *
# from fight import *

clear = lambda: os.system('cls')
pagar = str(48 * '#')

class start:
     def __init__(self):
          try:
               self.mydb = mysql.connector.connect(
               host="localhost",
               user="root",
               database="the geluds game"
               )
               self.cursor = self.mydb.cursor()          
          except mysql.connector.Error as e:
               print(e)
          #mulai
          self.menu()

     def displayProfil(self):
          print("\n" + pagar + "\n\t\tSelamat Datang!\n" + pagar+"\n\nProfil Anda")
          self.cursor.execute("SELECT * FROM player")
          hasil = self.cursor.fetchall()
          header = ['ID', 'Nama Anda', 'Health', 'Level','HeroID', 'WeaponID']
          myplayer = Player(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])
          print("\n"+tabulate(hasil, headers=header))


          self.cursor.execute("SELECT * FROM Hero Where HeroID={}".format(myplayer.hero))
          hasil = self.cursor.fetchall()
          header = ['ID','Nama Hero','Health','Power','Armor']
          myhero = Hero(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4])
          print("\n"+tabulate(hasil, headers=header))

          self.cursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama Senjata","Power"]
          myweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
          print("\n"+tabulate(hasil, headers=header))

     def displayMusuh(self):
          self.cursor.execute("SELECT * FROM Enemy Where EnemyID={}".format(myplayer.level))
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama Musuh","Health","Level","Power","Armor", "Weapon"]
          myenemy = Enemy(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5],hasil[0][6])
          print("\n\nProfil Musuh\n")
          print(tabulate(hasil, headers=header))

          #senjata musuh
          self.cursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama Senjata Musuh","Power"]
          myenemyweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
          print("\n"+tabulate(hasil, headers=header))

     def fight(self):
          self.displayMusuh()

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
    

     def login(self):
          self.displayProfil()
          print('\n1. Fight\n2. Menu\n')
          try:   
               pilihan = input('Pilihan = ')
               if pilihan=="1":
                    self.fight()
               elif pilihan=="2":
                    self.menu()
               else:
                    print("salah input")
          except KeyboardInterrupt:
               print("salah Input\nKembali ke Menu")
               self.menu()

     def mulai(self):
          while True:
               print('1. Melanjutkan\n2. Mengulangi Kembali')
               pilihan = input('pilihan = ')
               try:
                    if pilihan == "1":
                         self.login()
                         break
                    elif pilihan == "2":
                         self.reset()
                         break
                    else:
                         print("salah input menu")
                         self.menu()
               except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    self.menu()
                    break
               except:
                    print("salah input except")
                    self.menu()
                    break

     def reset(self):
          nama = str(input('\nNama = '))
          nama = nama.lower()
          print()

          self.cursor.execute("SELECT * FROM hero")
          hasil = self.cursor.fetchall()
          header = ['ID','Nama','Health','Power','Armor']
          print(tabulate(hasil, headers=header))
          pilihHero = int(input('\nPilih Hero = '))
          if pilihHero not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()

          print()
          self.cursor.execute("SELECT * FROM weapon")
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama","Power"]
          print(tabulate(hasil, headers=header))
          pilihSenjata = int(input('\nPilih Senjata = '))
          if pilihSenjata not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()   

          try:
               sql= "UPDATE `player` SET `PlayerName`= %s,`PlayerHealth`= 100,`PlayerLevel`= 1,`PlayerHero`=%s,`PlayerWeapon`=%s"
               val = (nama, pilihHero, pilihSenjata)
               self.cursor.execute(sql, val)
               self.mydb.commit()
               print("Main Ulang Berhasil\nSilahkan login kembali")         
               clear() 

          except mysql.connector.Error:
               print("Salah Input")

     def menu(self):
          while True:
               try:
                    print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +"\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
                    pilihan = input("Pilihan = ")
                    
                    if pilihan == "1":
                         clear()
                         self.mulai()
                         break
                    elif pilihan == "2":
                         clear()
                         print(pagar + "\n\t\tCara Main\n" + pagar+"\nCara Memainkan Game ini ialah dengan cara menekan pilihan sesuai yang ada.")
                         kembali = input('\nTekan enter untuk kembali')
                         clear()
                         self.menu()
                         break
                    elif pilihan == "3":
                         clear()
                         print(pagar + "\n\t\tThe Geluds Game\n" + pagar+ "\nGame ini dikembangankan menggunakan bahasa pemograman Python 3 selangkapnya bisa dilihat di www.github.com/zidny-z")
                         kembali = input('\nTekan enter untuk kembali')
                         clear()
                         self.menu()
                         break
                    elif pilihan == "4":
                         clear()
                         exit()
                         break
                    else:
                         print("salah Input")
               except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    break
               except:
                    break
     
     

start()