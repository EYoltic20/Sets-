# Emilio Yoltic Martinez Gutierrez 
import re

# Desplegamos las opciones del menu
def menu():
    print("""
        1.- Multiply sets
        2.- Power Sets
        3.- Determine Relation
        4.- Exit
    """)
    option = input("Insert the option ")
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

def getNewSet(set):
    newSet=[]
    A=[]
    B=[]
    for i in range(len(set)):
        if(i%6== 1 ):
            newSet.append((set[i],set[i+2]))
            A.append(set[i])
            B.append(set[i+2])
    return newSet,A,B

def check_if_it_is_transitive(set):
    newSet,A,B = getNewSet(set)
    print(A,"   ",B)
    # Todo es falso hasta que se demuestre lo contrario
    res=False
    print(newSet)
    if newSet == [(1,1)]:
        return True
    # formula (a,b) and (a,c) 
    for i in range(0,len(A),2):
        if ((A[-2],B[-1]) in newSet):
            res=True
        elif ((A[i%len(A)],B[(i+1)%len(B)])in newSet):
            if ((A[i%len(A)],B[(i+2)%len(B)])in newSet):
                res = True
        else:
            return False
    print(newSet)
    return res


def check_if_it_is_reflexiv(set):
    newSet,A,B = getNewSet(set)
    res= False
    for i in range(len(A)):
        if(A[i]==B[i]):
            res=True
        else:
            return False
    return res

def simplyfy(A,B): 
    Asimple=[0 for  x in range(len(A))]
    Bsimple=[0 for  x in range(len(B))]
    for i in range(len(A)):
        if(A[i]not in Asimple):
            Asimple[i]=A[i]
    for i in range(len(B)):
        if(B[i]not in Bsimple):
            Bsimple[i]=B[i]
    for i in range(len(Asimple)):
        if 0 in Asimple:
            Asimple.remove(0)
        else:
            break
    for i in range(len(Bsimple)):
        if 0 in Bsimple:
            Bsimple.remove(0)
        else:
            break
    return Asimple,Bsimple
            


def check_if_it_is_symetric(set):
    newSet,A,B = getNewSet(set)
    res= False
    Asimple,Bsimple=simplyfy(A,B)
    print(Asimple,"   ",Bsimple)
    for i in range(0,len(Asimple),2):
        if ((Asimple[i%len(Asimple)],Bsimple[i+1%len(Bsimple)])in newSet and (Asimple[i+1%len(Bsimple)],Bsimple[i%len(Bsimple)]) in newSet):
            return True

    return res


def determinate():
    set= str(input("Write set:"))
    transitive=check_if_it_is_transitive(set)
    reflexiv=check_if_it_is_reflexiv(set)
    symetric=check_if_it_is_symetric(set)
    print("transitive:",transitive,"Reflexiv:",reflexiv,"Symetric:",symetric)


def main():
    while True:
        opcion = menu()
        if(opcion =="1"):
            multiply()
        if (opcion == "2"):
            powerSet()
        if(opcion == "3"):
            determinate() 
        if (opcion =="4"):
            return 
        else:
            print("Opcion no valida ")
            

if __name__ == '__main__':
    main()