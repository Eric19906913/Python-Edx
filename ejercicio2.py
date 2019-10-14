vector = []
def carga():
    i=1
    while(i<=20):
        numero = float(input('Ingrese un numero:'))
        vector.append(numero)
        i=i+1
carga()
suma = sum(vector)
print(suma)
print(vector)
