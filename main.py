Triangle = """
                  B
                 /|
                / |
               /  |
              /   |
             /    |
            /     |
           /      |
          /       |
         /        |
        /         |
       /          |
      /           |
     /            |
    /             |
   /              |
  /               |
 /________________|
C                  A
"""

print('Tout dois etre en cm')
SideAsker = input("Combien de cotés connaissez vous ? 2/3 ")
if SideAsker == '1':
    print('Reponse non Valide')
    quit()
if SideAsker == '2':
    Hypoténuse = input("Connaissez vous l\'hypoténuse ? ")
    if Hypoténuse == "oui":
        print(Triangle)
        BC = float(input('BC = '))
        WSide = input('Quelle coté connaissez vous ? BA ou CA ? ')
        if WSide == 'BA':
            BA = float(input('BA = '))
            AC = float(BC) * float(BC) - float(BA) * float(BA)
            FirstSolve = float(AC) ** (1)
            print('AC =', FirstSolve, 'cm')
        else:
            CA = float(input('CA = '))
            BA = float(BC) * float(BC) - float(CA) * float(CA)
            SecondSolve = float(BA) ** (1)
            print('BA =', SecondSolve, 'cm')
    else:
        print(Triangle)
        BA = float(input('BA = '))
        CA = float(input('CA = '))
        BC = float(BA) * float(BA) + float(CA) * float(CA)
        ThirdSolve = float(BC) ** (1)
        print('BC =', ThirdSolve, 'cm')
if SideAsker == '3':
    AB = float(input('AB = '))
    AC = float(input('AC = '))
    CB = float(input('CB = ')) #Hypoténuse
    SolveOne = float(AB) * float(AB) + float(AC) * float(AC)
    SolveOneS = float(SolveOne) ** (1)
    print('AB² + AC² =', SolveOneS, 'cm')
    SolveTwo = float(CB) * float(CB)
    SolveTwoS = float(SolveTwo) ** (1)
    print('CB² =', SolveTwoS, 'cm')
    if SolveOneS == SolveTwoS:
        print('L\egalité est verifiée, le triangle est rectangle')
    else:
        print('L\'egalité n\'est pas verifiée, le triangle n\'est pas rectangle')
