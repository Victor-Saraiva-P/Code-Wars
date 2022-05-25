from typing import Reversible


def digitize(n):
    lista = []
    for i in reversed(str(n)):
        lista.append(int(i))
    return lista

digitize(348597)