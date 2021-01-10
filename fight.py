from tabulate import tabulate
import mysql.connector
import os
from classes import *
from startGame import *

class Pertarungan:
    def __init__(self):
        myMainDamage = myhero.getPower() + myweapon.getPower()
        myMainHealth = myplayer.getHealth() + myhero.getHealth()
        myMainArmor = myhero.getArmor()

        eMainDamage = myenemyweapon.getPower() + myenemy.getPower()
        eMainHealth = myenemy.getHealth()
        eMainArmor = myenemy.getArmor()

        self.fight()

    def fight(self):
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
    

