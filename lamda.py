
import random
def dmgTarget(str:int = 10) -> int:
	'''This is the basic formulate for calculating dmg

	It gets initiated with the base strenght and then gets called using a roll and base modifier
		hit(roll,buffMod)
	'''
	return lambda roll,mods : roll *  mods * (str / 10)

help(dmgTarget)
print(dmgTarget.__annotations__)
hit = dmgTarget(412)
roll = random.randint(0,20)
print(roll)
buffMod = 0.11 
dmg = hit(roll,buffMod)
print(dmg)