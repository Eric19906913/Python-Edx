vector = []
i=0
while(i<=5):
    caracter = str(input('ingresa algo: '))
    vector.append(caracter)
    i = i+1
posicion = []
for elemento in vector:
    if(elemento == '*'):
        posicion.append(vector.index(elemento))

print('Los asteriscos estan en las posiciones: ')
print(posicion)
