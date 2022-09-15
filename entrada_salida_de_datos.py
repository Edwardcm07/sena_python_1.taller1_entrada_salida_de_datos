#TALLER 1 PYTHON
#AUTOR: EDUAR ALEJANDRO CANO MONTOYA
#FECHA: 14 DE SEPTIEMBRE DE 2022

from datetime import date
hoy=date.today() #fecha actual 

print("Hoy es el dia: ", hoy)

n1=int(input("digite el primer numero: "))
n2=int(input("digite el segundo numero: "))

suma=n1+n2
resta=n1-n2
producto=n1*n2
division=n1/n2

print("la suma es = ", suma)
print("la resta es = ", resta)
print("La multiplicación es = ", producto)
print("la división es = ", division)
print("Fin")