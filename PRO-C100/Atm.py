import time
import os
import shutil
from unittest import case
from soupsieve import match

class Atm(object):

    def __init__(self, bank):
        self.bank = bank

    def showBank(self):
        print(self.bank)

    def start(self):
        print("Hello! Thanks for using HDFC, how may I help you?")
        choice1 = input()
        if choice1 == "balance":
            file1 = open("Balance.txt", 'r')
            print("Your balance is: ", file1.read(), "Rs.", sep='')
        elif choice1 == "deposit":
            file1 = open("Balance.txt", 'r')
            bal = int(file1.read())
            file1.close()
            file1 = open("Balance.txt", 'w')
            numToAdd = int(input("How much would you like to deposit?: "))
            sum = bal+numToAdd
            file1.write(str(sum))
            file1.close()
            print("Your balance is now: ", sum, "Rs.", sep='')
        elif choice1 == "withdraw":
            file1 = open("Balance.txt", 'r')
            bal = int(file1.read())
            file1.close()
            file1 = open("Balance.txt", 'w')
            numToSub = int(input("How much would you like to withdraw?: "))
            diff = bal-numToSub
            file1.write(str(diff))
            file1.close()
            print("Your balance is now: ", diff, "Rs.", sep='')