def is_valid_walk(walk):
    # determine if walk is valid
    if len(walk) == 10:
        v = 0
        h = 0

        for i in walk:
            if i == 'n':
                v += 1
            elif i == 's':
                v += -1
            elif i == 'e':
                h += 1
            elif i == 'w':
                h += -1

        if v == 0 and h == 0:
            return True
        else:
            return False

    else:
        return False



print(is_valid_walk(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))
