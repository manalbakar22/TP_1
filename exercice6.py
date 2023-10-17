a=int(input("saisir un nombre :"))
b=int(input("saisir une autre number :"))
v= input("saisir une operation :")
T= ["+","-","*","/"]
if v =="+" :
    print(a + b)
elif v=="-":
    print(a - b)
elif v=="*":
    print(a * b)
elif v=="/":
    print(a / b)
else:
    print("veillez saisir une operation valide !")
