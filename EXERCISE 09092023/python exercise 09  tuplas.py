#almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su
#implementar las funciones:
#1) carga de empleados
#2) impresion de los empleados y su sueldos.
#3) nombre del empleado con sueldo mayor.
#4) cantidad de empleados con sueldo menor a 100.

def cargar():
    empleados=[]
    for x in range(5):
        nombre=input("nombre del empleado:")
        sueldo=int(input("ingrese el sueldo:"))
        empleados.append( (nombre,sueldo))
        return empleados

def imprimir(empleado):
    print("listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleado:
        print(nombre,sueldo)

def mayor_sueldo(empleados):
    empleado=empleado[0]
    for emp in empleado:
        if emp[1]>empleado[1]:
            empleado=emp
    print("empleado con mayor sueldo:",empleado[0],"su sueldo es",empleado[1])

    def sueldos_menor1000(empleados):
        cant=0
        for empleado in empleados:
            if empleado[1]<1000:
                cant=cant+1
        print("cantidad de empleados con un sueldo menor a 1000 son:",cant)


#bloque principal
empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)
sueldos_menor1000(empleados)
    
