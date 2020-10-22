def remove_palindroms(spells):
    i = 0
    while i != len(spells):
        x = spells[i].upper().split()
        a = ''.join(x)
        if a == a[::-1]:
            spells.pop(i)
        else:
            i += 1
