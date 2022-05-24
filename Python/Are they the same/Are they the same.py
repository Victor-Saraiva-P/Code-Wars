from math import sqrt


def comp(array1, array2):
    print(locals())
    lenght = 0
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == sqrt(array2[j]):
                array2.pop(j)
                lenght += 1
                break
    if len(array1) == lenght:
        return True
    else:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

comp(a1, a2)

