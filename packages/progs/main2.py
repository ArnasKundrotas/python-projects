from sys import path

# path.append('..\\packages\\extrapack.zip') <-- NOT SOLVED <-- Not working with a zipped file
path.append('..\\packages')

import extra.iota
import extra.good.best.sigma as sigma
import extra.good.alpha as alfa
from extra.good.best.tau import FunT


print(extra.iota.FunI())

print (extra.good.best.sigma.FunS())
print(FunT())

print(sigma.FunS())
print(alfa.FunA())
