
x = int(input("Digite a um number: "))
def recursiva(n, memo={}):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in memo:
        resultado = memo[n]
    else:
        resultado = (recursiva(n-1)+2*recursiva(n-2))
        memo[n]= resultado
    return resultado


print(recursiva(x))