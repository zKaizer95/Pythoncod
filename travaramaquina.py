def Fatorial(N):
    if N < 0:
        print('0! = 1')
        return 1
    print(f"{N}! = {N} * {N + 1}!")
    return N *  Fatorial(N + 1)

#Bloco princípal
print(f"Fatorial de 5 = {Fatorial(100000)}")