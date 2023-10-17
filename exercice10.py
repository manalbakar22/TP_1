n=int(input("saisir votre taille : "))
m=float(input("SAISIR VOTRE POIDS : "))
mvc=m / n
print (mvc)
if mvc >= 40:
    print("obésité morbide ou massive")
elif mvc<40 and mvc>35:
    print("obésité sévère")
elif mvc<35 and mvc>30:
    print("obésité modérée")
elif mvc<30 and mvc>25:
    print("Surpoids")
elif mvc<25 and mvc>18.5:
    print("corpulence normale")
elif mvc<18.5 and mvc>16.5:
    print("Maigreur")
elif mvc<16 :
    print("Famine")