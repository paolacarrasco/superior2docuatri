lst = [] 
#lst será mi lista de listas que contenga todos los pares de datos, es decir todos los puntos x con sus respectivas imagenes 


n = int(input("Enter number of elements : ")) 
#En esta parte el usuario ingresará los pares de listas que se incluirán en la lista LST
for i in range(0, n):
    lista = []
    lista.append(int(input())) 
    lista.append(int(input())) 
    lst.append(lista)

#Defino una segunda lista vacía en la cual contendrá todos los L(x) calculados
l = 1 
lst2 = []
#calculo L(x)
for i in range(0,len(lst)): #Me situo en el primer elemento del dominio de la lista
    for j in range(0,len(lst)): # Recorro la lista que contiene todos mis pares nuevamente
        if i != j: # Recorro la lista es decir el siguiente elemento distinto de j hago la resta y luego se almacena el valor para post4eriormente calcularlo y guardarlo en otra lista
            l *= (lst[i][0] - lst[j][0])
    lst2.append(l)
    l=1
print(lst2)

#armado de polinomio

#Creo una nueva lista que contenga el calculo de a / l
coeficiente=[]

for i in range(0, len(lst)):
    coef = lst[i][1] / lst2[i]
    coeficiente.append(coef)

print(coeficiente) 


def armarPolinomioLagrange():
    polinomio = ""
    polinomios =""
    for i in range(0, len(lst)):
        polinomio = str(coeficiente[i])
        for j in range(0, len(lst)):
            if i != j:
                polinomio = polinomio + tuplaRaiz(lst[j][0])

                #print(polinomio)
        polinomios += polinomio + "+"
    print("P(x) = " + polinomios)

def tuplaRaiz(x): 
    tupla = "(x-"+str(x)+")"
    return tupla


armarPolinomioLagrange()