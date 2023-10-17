notes=[]
coefficients=[]
for i in range(1,5):
    note=int(input(f"saisir la note {i}: "))
    coefficient=int(input(f"saisir le coefficient {i}: "))
    notes.append(note)
    coefficients.append(coefficient)
   

sommea = sum(note * coef for note, coef in zip(notes, coefficients))
sommec= sum(coefficients)
moyenne = sommea / sommec


print("la moyenne de ses quatres points est : ",moyenne)
if moyenne >10:
    print("valide")
elif moyenne<7:
    print("non  valide")
elif moyenne<10 and moyenne>7:
    print("rattrapage")