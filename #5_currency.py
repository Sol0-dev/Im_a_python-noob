# this python scripts ask the user of how many money in 
# different currency user had and total it up to USD equivalent 
# of the sum

in_pesos = int(input("What do you have left in pesos? "))
pesos = in_pesos * 0.00027


in_soles = int(input("What do you have left in soles? "))
soles = in_soles * 0.29


in_reals = int(input("What do you have left in reals? "))
reals = in_reals * 0.20
print (int(pesos + soles + reals))
