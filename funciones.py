def es_primo(x):
    i = 0
    for n in range(2, x):
        if x % n == 0: 
            i += 1
    if i == 0 and x > 1: 
        return True
    return False
