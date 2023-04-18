print("esto es un archivo de prueba meramente para experimentar su funcionamiento ")
print ("Oh!, una personita nueva :D...no te habia visto por aqui  ")
namee = input("Cual es tu nombre ?")
print ("eh?" ) 
print ("perdona no te entendi, lo puedes repetir? owo")
name = input ("cual es tu nombre?")
print(f"hola , {name} es un placer tenerte aqui :D")

print ("practica :")

susu = input ("cual es tu nombre : ")
matematicas = int(input (susu + " cual es tu calificacion en matematicas : "))
quimica= int (input (susu + " cual es tu calificacion de quimica : "))
biologia = int (input (susu + " cual es tu calificacion de biologia  : "))
calificacion = (matematicas + quimica + biologia ) / 3 
calificacion = int( calificacion )

if calificacion >= 6 : 
    print('felicidades :D ' +  susu + "  aprovaste UWU con un promedio de : " , calificacion )
    print('felicidades :D ' +  susu + "  aprovaste UWU con un promedio de : " , round ( calificacion , 2))
else: 
    print(" :I ummm..." +  susu + " lo sentiento'reprobaste :/'  con un promedio de : "   , calificacion )
    print(" :I ummm..." +  susu + " lo sentiento 'reprobaste :/'  con un promedio de : "   , round ( calificacion , 1 ))
print ("fin :O . ")
