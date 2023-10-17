a=int(input("saisir un nombre: "))
if a%2 == 0 :
    print("this number is pair")
elif (a%2 != 0 ) and (a%3 == 0):
    print("ce nombre est impaire et multiple de 3")
else :
    print("ce nombre ni pair ni multiple de 3")