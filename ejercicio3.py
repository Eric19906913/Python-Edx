vector = []
i=0
contador = 0
while(i<=25):
    numero = int(input('Escribi wachen: '))
    vector.append(numero)
    i = i+1
i=0
for i in vector:
    if(i>0):
        suma = sum(vector)
    else:
        contador = contador + 1
print(suma)
print(contador)
