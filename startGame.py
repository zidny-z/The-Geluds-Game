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
          print()
          print(tabulate(hasil, headers=header))

          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM Hero Where HeroID={}".format(myplayer.hero))
          hasil = mycursor.fetchall()
          header = ['ID','Nama Hero','Health','Power','Armor']
          print()
          print(tabulate(hasil, headers=header))

          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
          hasil = mycursor.fetchall()
          header = ['ID',"Nama Senjata","Power"]
          print()
          print(tabulate(hasil, headers=header))

     def mulai(self):
          while True:
               print('1. Melanjutkan\n2. Mengulangi Kembali')
               pilihan= input('pilihan = ')
               try:
                    if pilihan=="1":
                         self.login()
                         break
                    elif pilihan=="2":
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
                    menu()

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