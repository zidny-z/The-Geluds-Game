from tabulate import tabulate
import mysql.connector
import random
import os
# import fight

clear = lambda: os.system('cls')
pagar = str(48 * '#')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="the geluds game"
)

class Hero:
     def __init__(self, idnya, nama, health, power, armor):
          self.id = idnya
          self.nama = nama
          self.health = health
          self.power = power
          self.armor = armor

class Weapon:
     def __init__(self, idnya , nama, power, critRate, critDamage):
          self.id = idnya
          self.nama = nama
          self.power = power
          self.critRate = critRate
          self.critDamage = critDamage

class Player:
     def __init__(self, idnya, nama, health, level, hero, weapon):
          self.id = idnya
          self.nama = nama
          self.health = health
          self.level = level
          self.hero = hero
          self.weapon = weapon
     
class Enemy:
     def __init__(self, idnya, nama, power, armor, level, health):
          self.id = idnya
          self.nama = nama
          self.power = power
          self.armor = armor
          self.level = level
          self.health = health


#--- Declare Player ---#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM player")
hasil = mycursor.fetchall()
myplayer = Player(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])



def mulai():
     while True:
          print('1. Melanjutkan\n2. Mengulangi Kembali')
          pilihan= input('pilihan = ')
          try:
               if pilihan=="1":
                    login()
                    break
               elif pilihan=="2":
                    reset()
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

def displayProfil():
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
     header = ['ID',"Nama Senjata","Power","CritRate", "CritDamage"]
     print()
     print(tabulate(hasil, headers=header))

def login():
     displayProfil()
     print('\n1. Fight\n2. Menu\n')
     try:   
          pilihan = input('Pilihan = ')
          if pilihan=="1":
               level = myplayer.level
               hpPlayer = myplayer.health

# UNTUK MEMANGGIL POWER HERO,PLAYER,WEAPON
               mycursor = mydb.cursor()
               mycursor.execute("SELECT * FROM hero Where heroID={}".format(myplayer.hero))
               hasil = mycursor.fetchall()
               damageHero = hasil[0][3]
               armorHero = hasil[0][4]

               mycursor = mydb.cursor()
               mycursor.execute("SELECT * FROM weapon Where weaponID={}".format(myplayer.weapon))
               hasil = mycursor.fetchall()
               damageWeapon = hasil[0][2]
               critRate = hasil[0][3]
               critDamage = hasil[0][4]

               totalDamage = damageHero + damageWeapon + random.randint(0, critRate) + random.randint(0, critDamage)

# UNTUK MEMANGGIL HEALTHY HERO DAN PLAYER
               mycursor = mydb.cursor()
               mycursor.execute("SELECT * FROM hero Where heroID={}".format(myplayer.hero))
               hasil = mycursor.fetchall()
               hpHero = hasil[0][2]

               totalHP = hpHero+hpPlayer

#  UNTUK MEMANGGIL HEALTH ENEMY, ARMOR ENEMY
               mycursor = mydb.cursor()
               mycursor.execute("SELECT * FROM enemy Where enemyLevel={}".format(level))
               hasil = mycursor.fetchall()
               enemy = Enemy(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])
               hpEnemy = enemy.health
               

               status = None
     
               while totalHP > 0 and hpEnemy > 0:
                    # player menyerang enemy
                    hasilSerang = totalDamage - enemy.armor
                    if hasilSerang>=31:
                         print('\nAnda memberikan Critical Hit sebesar', hasilSerang)
                    elif hasilSerang<=7:
                         print('\nImmune')
                    else:
                         print("\n",hasilSerang,'Hit')
                    hpEnemy = hpEnemy - hasilSerang
                    print('HP musuh = ', hpEnemy)

                    # player diserang enemy
                    enemypower = random.randint(5,enemy.power)
                    hasilSerangMusuh = enemypower - armorHero
                    if hasilSerangMusuh <= 0:
                         hasilSerangMusuh = 0
                    print('Musuh memberikan',enemypower,'hit')
                    totalHP = totalHP - hasilSerangMusuh
                    print('HP Anda = ', totalHP)
                    

                    if hpEnemy<=0:
                         status = "Win"
                         print("\nSelamat Anda Menang")
                         level += 1
                         if level>=10 and status=="Win":
                              level = 1
                              print(pagar+"\nSelamat Anda telah Menyelesaikan Game ini\n"+pagar)
                         mycursor = mydb.cursor()
                         mycursor.execute("UPDATE `player` SET `PlayerLevel`={} WHERE PlayerID=1".format(level))
                         mydb.commit()

                    else:
                         print("Anda Kalah\nJangan putus Semangat!")
          
                    
                    break
          elif pilihan=="2":
               menu()
               
          else:
               print("salah input")
     except KeyboardInterrupt:
          print("salah Input")

def reset():
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
          menu()

     print()
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM weapon")
     hasil = mycursor.fetchall()
     header = ['ID',"Nama","Power","CritRate", "CritDamage"]
     print(tabulate(hasil, headers=header))
     pilihSenjata = int(input('\nPilih Senjata = '))
     if pilihSenjata not in range(1,len(hasil)+1):
          print('salah input')
          menu()   

     try:
          sql= "UPDATE `player` SET `PlayerName`= %s,`PlayerHealth`= 100,`PlayerLevel`= 1,`PlayerHero`=%s,`PlayerWeapon`=%s"
          val = (nama, pilihHero, pilihSenjata)
          mycursor.execute(sql, val)
          mydb.commit()
          print("Main Ulang Berhasil\nSilahkan login kembali")         
          clear()

          

     except mysql.connector.Error:
          print("Salah Input")

def menu():
     while True:
          try:
               print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +
                         "\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
               pilihan = input("Pilihan = ")
               
               if pilihan == "1":
                    clear()
                    mulai()
                    break
               elif pilihan == "2":
                    clear()
                    print(pagar + "\n\t\tCara Main\n" + pagar+"\nCara Memainkan Game ini ialah dengan cara menekan pilihan sesuai yang ada.")
                    kembali = input('\nTekan enter untuk kembali')
                    clear()
                    menu()
                    break
               elif pilihan == "3":
                    clear()
                    print(pagar + "\n\t\tThe Geluds Game\n" + pagar+ "\nGame ini dikembangankan menggunakan bahasa pemograman Python 3 selangkapnya bisa dilihat di www.github.com/zidny-z")
                    kembali = input('\nTekan enter untuk kembali')
                    clear()
                    menu()
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
menu()

