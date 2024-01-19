from KlassArrayQ import ArrayQ

def skapa_ordningen():
    q = ArrayQ()

    temp = input("Vilka siffror:").split(",")
    q.enqueue(int(temp[0]))
    q.enqueue(int(temp[1]))
    q.enqueue(int(temp[2]))
    q.enqueue(int(temp[3]))
    q.enqueue(int(temp[4]))
    return q

def sortera_kort(kort_hög):
    lista = []
    temp = (kort_hög.dequeue())
    kort_hög.enqueue(temp)
    lista.append(kort_hög.dequeue())

    temp = (kort_hög.dequeue())
    kort_hög.enqueue(temp)
    lista.append(kort_hög.dequeue())

    temp = (kort_hög.dequeue())
    kort_hög.enqueue(temp)
    lista.append(kort_hög.dequeue())

    temp = (kort_hög.dequeue())
    kort_hög.enqueue(temp)
    lista.append(kort_hög.dequeue())

    temp = (kort_hög.dequeue())
    kort_hög.enqueue(temp)
    lista.append(kort_hög.dequeue())

    return lista

def sorterat_rätt(sorterat):
    print(sorterat)


def main():
    j = skapa_ordningen()
    k = sortera_kort(j)
    sorterat_rätt(k)

main()
    



