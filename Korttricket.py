from KlassArrayQ import ArrayQ

def skapa_ordningen():
    q = ArrayQ()

    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(2)
    q.enqueue(5)
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
    



