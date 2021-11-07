import time
import random

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
    Hypoténuse = input("Connaissez vous l\'hypoténuse ?")
    if Hypoténuse == "oui":
        print(Triangle)
        BC = input('BC = ')
        WSide = input('Quelle coté connaissez vous ? BA ou CA ? ')
        if WSide == 'BA':
            BA = input('BA = ')
            AC = str(BC) * BC - BA * BA 
            SecondSolve = AC ** (0.5)
            print('AC = ', SecondSolve, 'cm')
        else:
            CA = input('CA = ')
