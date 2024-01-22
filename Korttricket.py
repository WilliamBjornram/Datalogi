from linkedQFile import *

import sys

def skapa_ordningen():
    q = LinkedQ()

    temp = sys.stdin.readline()

    indata = input("Vilka siffror:").split(" ")
    
    for i in range(len(temp)):
        q.enqueue((temp[i]))
    return q

def sortera_kort(kort_hög):
    lista = []
    for i in range(kort_hög.size()):
        temp = (kort_hög.dequeue())
        kort_hög.enqueue(temp)
        lista.append(kort_hög.dequeue())

    return lista

def sorterat_rätt(sorterat):
    for i in range(len(sorterat)):
        print(str(sorterat[i]) + " ", end="")

def main():
    sorterat_rätt(sortera_kort(skapa_ordningen()))

main()
    



