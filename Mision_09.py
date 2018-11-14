#Autor Claudio Mayoral Garcia
#Descripcion es un programa que contiene funciones que modifican o crean listasy regresan lo que corresponde


#Es una funcion que recibe una lista y regresa una lista con los numeros pares
def extraerPares(listaOriginal):
    nuevaLista = []
    for par in listaOriginal:
        if par %2 == 0:
            nuevaLista.append(par)
    return nuevaLista


#Es una lista que recibe una lista que contiene los elementos mayores al elemento previo
def extraerMayoresPrevio(listaOriginal):
    nuevaLista = []
    for mayores in range(1, len(listaOriginal)):
        if listaOriginal[mayores] > listaOriginal[mayores-1]:
            nuevaLista.append(listaOriginal[mayores])
    return nuevaLista


#Es una funcion que intercambia los numeros de posicion en parejas
def intercambiarParejas(listaOriginal):
    nuevaLista = []
    for parejas in range(1, len(listaOriginal), 2):
        nuevaLista.append(listaOriginal[parejas])
        nuevaLista.append(listaOriginal[parejas-1])
    if len(listaOriginal)%2 == 1:
        nuevaLista.append(listaOriginal[-1])
    return nuevaLista


#Es una funcion que intercambia las posiciones del nuero mayor y el numero menor
def intercambiarMM(listaOriginal):
    if len(listaOriginal) == 0:
        pass
    else:
        mayor = list.index(listaOriginal, max(listaOriginal))
        menor = list.index(listaOriginal, min(listaOriginal))
        listaOriginal[mayor], listaOriginal[menor] = listaOriginal[menor], listaOriginal[mayor]


#Es una funcion que promedia la lista quitando el valor mayor y el menor
def promediarCentro(listaOriginal):
    listaNueva = listaOriginal
    listaNueva.sort()
    nueva = listaNueva[1:len(listaNueva)-1]
    if len(nueva) > 0:
        promedio = int(sum(nueva)/len(nueva))
    else:
        return 0
    return promedio


#Es una funcion que recibe una lista de numeros y regresa una dupla con media y desviacion estandar
def calcularEstadistica(listaOriginal):
    acumulador = 0
    if len(listaOriginal) > 0:
        media = sum(listaOriginal) / len(listaOriginal)
    else:
        media = 0
    if len(listaOriginal) > 1:
        for n in listaOriginal:
            acumulador += (n-media)**2
        deviation = (acumulador / (len(listaOriginal) - 1)) ** 0.5
    else:
        deviation = 0
    return media, deviation


#Es una funcion que recibe como parámetro una lista y regresa la suma de los valores quitando 13 al lado de 13
def calcularSuma(listaOriginal):
    listaNueva = listaOriginal.copy()
    if 13 not in listaNueva:
        return sum(listaNueva)
    else:
        for n in range(len(listaNueva)):
            if listaNueva[n] == 13:
                if n != 0:
                    listaNueva[n-1] = 0
                if n != len(listaNueva)-1:
                    listaNueva[n+1] = 0
                listaNueva[n] = 0
    suma = sum(listaNueva)
    return suma