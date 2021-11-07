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


SideAsker = input("Combien de cotés connaissez vous ? 2/3")
if SideAsker == '1':
    print('Reponse non Valide')
    quit()
if SideAsker == '2':
    Hypoténuse = input("Connaissez vous l\'hypoténuse ?")
    if Hypoténuse == "oui":
        print(Triangle)
        BC = input('BC = ')
        WSide = input('Quelle coté connaissez vous ? BA ou CA ?')
        if WSide == 'BA':
            BA = input('BA = ')
            BCcarré = BC * BC 
        else:
            CA = input('CA = ')



