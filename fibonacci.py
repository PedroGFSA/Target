## n é o valor que queremos verificar 

def fibonacci(n):
    
    numeros = [0, 1]
    encontrado = False
    while True:
        if numeros[-2] > n:
            break
        if numeros[-2] == n or numeros[-1] == n:
            encontrado = True
            break
        numeros.append(numeros[-1] + numeros[-2])
    return encontrado

print(fibonacci(377))