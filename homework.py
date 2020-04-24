# coding=utf-8

vehicleType = input('Elija el tipo de vehiculo, "carro", "camión 2 ejes", "camión 4 ejes", "taxi", "bus": ')

hour= int(input('Ingrese la hora en su forma militar: '))

passengers = int(input('Ingrese la cantidad de pasajeros que viajan en el vehículo: '))

preference = input('Desea pagar el porcentaje adicional, "sí", ("no"): ')

discRate = 0
addiPerc = 0

if vehicleType == "carro":
    rate = 200

elif vehicleType == "camión 2 ejes":
    rate = 500

elif vehicleType == "camión 4 ejes":
    rate = 600

elif vehicleType == "taxi":
    rate = 1000

elif vehicleType == "bus":
    rate = 1000

else:
    rate = 200

if (hour >= 7 and hour <= 9) or (hour >= 17 and hour <= 19):
    discRate = 0.2
    
    if (vehicleType == "carro" or vehicleType == "taxi" and passengers >=4) or (vehicleType == "bus" and passengers >= 20):
        discRate = 1

else: 
    discRate = 0

if preference == "sí":
    addiPerc = 0.15
else:
    addiPerc = 0

subtotal = rate

discount = subtotal * discRate

additional = subtotal * addiPerc

total = subtotal - discount + additional

print ('Total a pagar: ', total)
