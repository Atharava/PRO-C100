#Setup
from Atm import Atm

atm1 = Atm('HDFC')

#Display
for i in range(1, 2):
    print("\n")

    atm1.showBank()
    print('\n')
    atm1.start()

for i in range(1, 2):
    print("\n")