# programa que muestra la distancia entre dos puntos por medio de formula:
# D = ­┴ (y2-y1)^^2 + (x2-x1)^^2
import math

cor=int(input('cuantas distancias vas a necesitar: '))
for x in range (cor):
	X1=int(input('introduce el valor de X1= '))
	Y1=int(input('introduce el valor de Y1= '))
	X2=int(input('introduce el valor de X2= '))
	Y2=int(input('introduce el valor de Y2= '))
	Perentesis_de_equis=(X2-X1)
	Perentesis_de_yes=(Y2-Y1)
	equis_Elevado=(Perentesis_de_equis)**2
	yes_Elevado=(Perentesis_de_yes)**2
	Raiz=equis_Elevado+yes_Elevado
	Distancia=math.sqrt(Raiz)
	print(f'La distancia entre los dos puntos es de {Distancia}')
	print('     |-         2           2')
	print(f'D =  |({Y2} - {Y1}) + ({X2} - {X1})       ')
	print("    _/                                      ")
	print(' ')
	print('     |-     2        2')
	print(f'D =  |({Perentesis_de_yes}) + ({Perentesis_de_equis})       ')
	print("    _/                                      ")
	print(' ')
	print('     |-     ')
	print(f'D =  |{yes_Elevado} + {equis_Elevado}      ')
	print("    _/                                      ")
	print(' ')
	print('     |-     ')
	print(f'D =  |{Raiz}      ')
	print("    _/                                      ")
	print(' ')
	print('       ')
	print(f'D =   {Distancia}  ')
	print("                                       ")


# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line





























