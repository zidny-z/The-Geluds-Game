from tabulate import tabulate
import mysql.connector
import os
from classes import *

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

     def login(self):
          displayProfil()
          print('\n1. Fight\n2. Menu\n')
          try:   
               pilihan = input('Pilihan = ')
               if pilihan=="1":
                    print('hello')
               elif pilihan=="2":
                    self.menu()
               else:
                    print("salah input")
          except KeyboardInterrupt:
               print("salah Input")

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
                         print("salah input")
                         menu()
               except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    break
               except:
                    print("salah input")
                    self.menu()

     def reset(self):
          nama = str(input('\nNama = '))
          nama = nama.lower()
          print()

          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM hero")
          hasil = mycursor.fetchall()
          header = ['ID','Nama','Health','Power','Armor']
          print(tabulate(hasil, headers=header))
          pilihHero = int(input('\nPilih Hero = '))
          if pilihHero not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()

          print()
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM weapon")
          hasil = mycursor.fetchall()
          header = ['ID',"Nama","Power"]
          print(tabulate(hasil, headers=header))
          pilihSenjata = int(input('\nPilih Senjata = '))
          if pilihSenjata not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()   

          try:
               sql= "UPDATE `player` SET `PlayerName`= %s,`PlayerHealth`= 100,`PlayerLevel`= 1,`PlayerHero`=%s,`PlayerWeapon`=%s"
               val = (nama, pilihHero, pilihSenjata)
               mycursor.execute(sql, val)
               mydb.commit()
               print("Main Ulang Berhasil\nSilahkan login kembali")         
               clear() 

          except mysql.connector.Error:
               print("Salah Input")

     def menu(self):
          while True:
               try:
                    print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +
                              "\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
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