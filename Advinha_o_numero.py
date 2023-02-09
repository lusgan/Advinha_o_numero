import random 

print("="*50)
print(" "*12 + "Bem vindo ao ADVINHA!!!")
print("="*50)

#advinha numeros entre 1 e "a".
def advinha(a): 
    x = random.randint(1,a)
    numero_escolhido = 0
    
    while (numero_escolhido != x):
        numero_escolhido = int(input(f"Advinhe o numero entre 1 e {a}:"))
        
        if(numero_escolhido>x):
            print("muito alto, tente um menor.\n")
        
        elif(numero_escolhido<x):
            print("muito baixo, tente um maior.\n")
        
    print("\n\nBoaaa, vc acertou!!")
    
advinha(100)