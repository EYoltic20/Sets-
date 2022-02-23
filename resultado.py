
from itertools import count
import re

def menu():
    print("""
        1.- Multiply sets
        2.- Power Sets
        3.- Exit
    """)
    option = int(input("Insert the option "))
    return option


# Funciona si se ejecuta el set normal pero faltan las validaciones 
def multiply():
    setA=str(input("Insert set A separate by , : "))
    setB=str(input("Insert set B separate by , : "))
    setAL = setA.split(",")
    setBL = setB.split(",")
    # Desarrollar logica para encontrar patrones no correctos
    newSet = [0 for x in range(len(setAL)*len(setBL))]
    #O(n) Complexity |O(n)Space
    #O(n^2)Complexity|O(n)Space
    count=0
    for i in setAL:
        for b in setBL:
            newSet[count]=[i,b]
            count+=1
 
    print(newSet)


def powerSet():
    setPower=str(input("Insert the set separete by , : "))
    setPowerL=setPower.split(",")
    newSet=[0 for x in range(pow(2,len(setPowerL)))]
    print(newSet)
    for i in range(len(newSet)-1):
        if [setPowerL[i%len(setPowerL)]] in newSet:
            count=1
            temp=[setPowerL[i%len(setPowerL)]]
            while True:
                if temp in newSet:
                    temp.append(setPowerL[(i+count)%len(setPowerL)])
                    count+=1
                else:    
                    newSet[i] = temp
                    break
        else:  
            newSet[i] = [setPowerL[i%len(setPowerL)]]
# Por regla general los sets llevan un set vacio
    print(newSet)


def main():
    while True:
        opcion = menu()
        if(opcion ==1):
            multiply()
        if (opcion == 2 ):
            powerSet()
        if(opcion == 3):
            return 
            

if __name__ == '__main__':
    main()