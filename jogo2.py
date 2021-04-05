def comp():
    from random import randint
    computador = []
    ppt = randint(1, 3)
    if ppt == 1:
        computador = 'pedra'
    elif ppt == 2:
        computador = 'papel'
    else:
        computador = 'tesoura'
    return computador