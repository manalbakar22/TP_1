s=float(input("saisir un nombre de seconde : "))

print("votre nombre de secondes  est composer de " ,int(s/3600), "h" ,int((s%3600)/60), "minutes",(s%3600)%60 ,"secondes")