print ("CUADRO MAGICO")
tamano=int(input("Ingrese el tamaño del Cuadro impar: "))
magia=tamano*(pow(tamano,2)+1)/2 #n( n^2 + 1) / 2
print ("El numero magico es: "+str(magia))
centro=int(tamano/2)
cuadro=[[0 for i in range(tamano)] for i in range(tamano)]
cuadro[0][centro]=1

#Variables:
num=1
fila=0
columna=centro

#Proceso:
for i in range((tamano*tamano)-1):    
    num=num+1
    ubifila=fila
    fila=fila-1
    ubicolumna=columna
    columna=columna-1
    #Logica de ubicacion
    if fila<0:        
        fila=tamano-1
    if columna<0:        
        columna=tamano-1
    #Logica de llenado
    if cuadro[fila][columna]==0:
        cuadro[fila][columna]=num       
    elif cuadro[fila][columna]!=0:
        fila=fila+1
        if fila>0:        
            fila=ubifila+1
        columna=ubicolumna
        cuadro[fila][columna]=num


#Impresion:
for n in range(tamano):    
    print (str(cuadro[0:tamano][n]))
   
input("Press Enter to continue...")
