import datetime
fecha_nac = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = map(int, fecha_nac.split("/"))
fecha_act = datetime.date.today()
anio_hoy = fecha_act.year
mes_hoy = fecha_act.month
dia_hoy = fecha_act.day
edad =  anio_hoy - anio

if(mes > mes_hoy): 
    print("Tu edad actual es de:", edad, "anios" )
elif((mes == mes_hoy) and (dia == dia_hoy)):
    print ("feliz cumple numero", edad, "!" )
elif((mes == mes_hoy) and (dia < dia_hoy)):
    print ("feliz cumple numero" , edad , "atrasado" )
elif((mes == mes_hoy) and (dia <= dia_hoy + 3)):
    print ("falta poco para tu cumple numero", edad )
else: 
    print("Tu edad es de:", edad)