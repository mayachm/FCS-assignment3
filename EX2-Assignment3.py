def comb(char, n, cc=""):
    if len(cc) == n:
        print(cc)
        return
    
    for char in characters:
        comb(characters, n, cc + char)

characters = ['a', 'b', 'c']
n = 2
comb(characters, n)
