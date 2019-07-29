import math as m

def moduloC(a,b,c):
    modulo = m.sqrt((a**2) + (b**2) + (c**2))
    return modulo
def cosAng(coseno):
    aux = m.acos(coseno)
    angulo = m.degrees(aux)
    return angulo

a1 = float(input('Ingrese la componente "a" del vector 1: '))
b1 = float(input('Ingrese la componente "b" del vector 1: '))
c1 = float(input('Ingrese la componente "c" del vector 1: '))
a2 = float(input('Ingrese la componente "a" del vector 2: '))
b2 = float(input('Ingrese la componente "b" del vector 2: '))
c2 = float(input('Ingrese la componente "c" del vector 2: '))
print('-------------------------------------------------------------')
vector1 = [a1,b1,c1]
vector2 = [a2,b2,c2]
prodE = ((a1*a2) + (b1*b2) + (c1*c2))
modulo1 = moduloC(a1,b1,c1)
modulo2 = moduloC(a2,b2,c2)
print('Los vectores ingresados son: \n')
print('Vector 1:', vector1,'\n')
print('Vector 2:', vector2,'\n')
print('-------------------------------------------------------------')
print('Sus modulos son: \n')
print('Modulo del vector 1:',modulo1,'\n')
print('Modulo del vector 2:',modulo2,'\n')

coseno = prodE / (modulo1*modulo2)
angulo = cosAng(coseno)
print('El coseno del angulo formado por los vectores es:',round(coseno, 2))
print('El angulo formado por los vectores es de:',round(angulo, 2),'grados')
producto = modulo1 * modulo2 * coseno
print('El producto entre los dos vectores es:',round(producto, 2))
