from random import sample, shuffle, choice, randint, choices

from typing import Any

class aux:
    # Esta función particiona una lista de tal forma que la izquierda de la misma
    # almacenará todos los valores menores al pivote y la parte derecha todos los
    # valores mayores. Estos dos subgrupos no estarán necesariamente ordenados.
    @staticmethod
    def partition(array: list, left: int, right: int, pivotIndex: int):
        pivotValue = array[pivotIndex]
        array[pivotIndex], array[right] = array[right], array[pivotIndex]
        sendreIndex = left
        for i in range(left, right):
            if array[i] < pivotValue:
                array[sendreIndex], array[i] = array[i], array[sendreIndex]
                sendreIndex += 1
        array[right], array[sendreIndex] = array[sendreIndex], array[right]
        return sendreIndex
    
    # Esta función mezcla dos listas ordenadas, de tal forma que la
    # lista 1 está representada por <array>[start:mid] y la lista 2
    # por <array>[mid+1:end]; ordenando así <array>.
    @staticmethod
    def merge(array: list, temp: list, start: int, mid: int, end: int):
        i = k = start
        j = mid + 1

        while i <= mid and j <= end:
            if array[i] < array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
            k += 1

        while i <= mid and i < len(array):
            temp[k] = array[i]
            k += 1
            i += 1
        
        array[start:end + 1] = temp[start:end + 1]

# <k> representa el k-ésimo menor elemento.
def quickSelect(array: list, k: int) -> Any:
    # Esta función se hizo en base a una versión recursiva;
    # <stack> representa las llamadas que se hacían almacenando
    # el input, imitando el call stack.
    stack = [(array, 0, len(array)-1, k)]
    while True:
        array, left, right, k = stack.pop()
        if left == right:
            return array[left]
        pivotIndex = (left+right)//2
        pivotIndex = aux.partition(array, left, right, pivotIndex)
        if k == pivotIndex:
            return array[k]
        elif k < pivotIndex:
            stack.append((array, left, pivotIndex-1, k))
        else:
            stack.append((array, pivotIndex+1, right, k))

def mergeSort(array: list, start: int = 0):
    # <temp> es un arreglo temporal usado cuando se mezclan las listas.
    # Es definido aquí para ser reutilizado durante las iteraciones y
    # no generar arreglos de más que luego se perderán en memoria.
    temp = array.copy()
    m = 1
    while m <= len(array) - 1 - start:
        for i in range(start, len(array) - 1, 2*m):
            end = min(i + 2*m - 1, len(array) - 1)
            aux.merge(array, temp, i, i + m - 1, end)
        m *= 2

def getInput() -> list:
    print('Presione ENTER una vez haya terminado de ingresar los datos de un experimento para ejecutar el programa.')
    data = []
    flag = True
    while flag == True:
        while True:
            if (str := input()) == '':
                flag = False
                break
            try:
                n, k = map(int, str.split(' '))
                if n < 1 or not (0 < k <= n):
                    raise Exception()
                break
            except:
                print('Los datos no fueron ingresados correctamente, intente nuevamente.')
            break
        if not flag:
            break
        
        exp = []
        while n > 0:
            try:
                valor, string = input().split(' ')
                valor = int(valor)
            except:
                print('Los datos no fueron ingresados correctamente, intente nuevamente.')
                continue
            if (len(string) <= 32) and (0 <= valor < 2**32 - 1):
                exp.append((valor, string))
                n -= 1
            else:
                print('Los datos no fueron ingresados correctamente, intente nuevamente.')
        data.append((k, exp))
    return data

if __name__ == '__main__':
    if (data := getInput()) == []:
        exit()

    for k, samples in data:
        start = len(samples) - k 
        quickSelect(samples, start)
        mergeSort(samples, start)

        i = len(samples)
        while (i := i - 1) >= start:
            print(f'{samples[i][0]} {samples[i][1]}')
        print()
    
    # (BORRAR) Generador de muestras aleatorias.
    '''
    samples = [
        (randint(0, 99), ''.join(choices(string.ascii_letters + string.digits, k=randint(1, 32))))
        for i in range(20)
    ]
    '''
