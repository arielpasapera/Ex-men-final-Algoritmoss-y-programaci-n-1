import csv
def leer_csv(ruta_archivo: str) -> list:
    datos: list = []
    try:
        with open (ruta_archivo, newline='', encoding="UTF-8") as archivo_csv:
            csv_reader = csv.reader(archivo_csv, delimiter = ';')
            for fila in csv_reader:
                datos.append(fila)
    
    except IOError: 
        print("No se encontró el archivo") 
    
    return datos


def antiguedad_promedio(integrantes:list) -> None:
    anio_actual:int = 2023
    lista_de_anios:list = []
    for anio in integrantes:
        anio_de_ingreso:int = int(anio[1][:4])
        diferencia:int = ((anio_actual - anio_de_ingreso) * 12)
        lista_de_anios.append(diferencia)

    total:int = len(lista_de_anios)   
    suma:int = 0
    for mes in lista_de_anios:
        suma += mes

    promedio:float = round((suma/total),2)
    print(f"La antiguedad promedio es {promedio} meses.") 


def promedio_global(integrantes:list) -> None:
    lista_promedios:list = []
    for preferido in integrantes:
        if(preferido[6] == "Recursividad"):
            lista_promedios.append(preferido)
        elif (len(preferido) > 7) and (preferido not in lista_promedios):
            if("Recursividad" in preferido):
                lista_promedios.append(preferido)
    
    
    valor:int = 0
    suma:int = 0
    for n in lista_promedios:
        valor += (int(n[4]) * int(n[5]))
        suma += int(n[4])
    
    promedio_global:float = round(valor/suma,2)
    print("El promedio global de los parciales es {}".format(promedio_global))
    print(f"La cantidad de parciales corregidos fué de {suma}")


def ranking_materias(integrantes:list) -> None:
    dicc_materias:dict = {}
    for elegidas in integrantes:
        materia:str = elegidas[6]
        if (materia not in dicc_materias.keys()):
            dicc_materias[materia] = 1
        else:
            dicc_materias[materia] += 1
        
        if (len(elegidas) > 7):
            for n in range(7, len(elegidas)):
                materia = elegidas[n]
                
                if (materia not in dicc_materias.keys()):
                    dicc_materias[materia] = 1
                else:
                    dicc_materias[materia] += 1

    lista_de_materias:list = []  
    for x in sorted(dicc_materias, key=lambda x:dicc_materias[x], reverse=True):
        lista_de_materias.append([x, dicc_materias[x]])

    try:
        with open('ranking.csv', 'w', newline='', encoding="UTF-8") as archivo_csv:
            csv_writer = csv.writer(archivo_csv, delimiter=',')
            csv_writer.writerows(lista_de_materias)

    except IOError:
            print("No se ha encontrado la ruta.")



def integrantes_ingresados(integrantes:list) -> None:
    contador_primer_semestre: int = 0
    aprobados_primer_semestre:int = 0

    contador_segundo_semestre:int = 0
    aprobados_segundo_semestre:int = 0
    
    for semestre in integrantes:
        promedio_tp:int = int(semestre[3])
        promedio_parcial:int = int(semestre[5])
        print(contador_primer_semestre,contador_segundo_semestre)

        if(int(semestre[1][4:]) >= 1) and ((int(semestre[1][4:]) <= 6)):
            #primer semestre:
            contador_primer_semestre += 1
            if (promedio_tp > 6) and (promedio_parcial > 6):
                aprobados_primer_semestre += 1
        
        elif((int(semestre[1][4:]) >= 7) and ((int(semestre[1][4:]) <= 12))):
            #segundo semestre
            contador_segundo_semestre += 1
            if (promedio_tp > 6) and (promedio_parcial > 6):
                aprobados_segundo_semestre += 1
    
    
    aprobados_primer_semestre = round(((aprobados_primer_semestre*100)/contador_primer_semestre),2)
    aprobados_segundo_semestre = round(((aprobados_segundo_semestre*100)/contador_segundo_semestre),2)
    
    print(f"{contador_primer_semestre} fueron alumnos del primer semestre.")
    print(f"{aprobados_primer_semestre}% de los alumnos tienen promedio mayor a 6 del primer semestre")

    print(f"{contador_segundo_semestre} fueron alumnos del segundo semestre.")
    print(f"{aprobados_segundo_semestre}% de los alumnos tienen promedio mayor a 6 del segundo semestre")
    

def menu() -> None:
    opciones: list = [
        "1- Determinar la antigüedad promedio en meses del equipo",
        "2- indicar el promedio global de los parciales con recursividad como tema preferido",
        "3- Armar el ranking de temas favoritos",
        "4- Comparar los integrantes ingresados en primer semestre contra los del segundo semestre)",

    ]

    for opcion in opciones:
        print (opcion)

    opcion: int = int(input("\n Ingrese una opción:  ->  "))
    while (opcion  < 1 or opcion > 4):
       opcion: int = int(input("\n Ingrese una opción:  ->  "))
    return opcion

def main() -> None:

    integrantes:list = leer_csv("integrantes.csv")
    opcion: int= 1

    while (opcion != 0):   
        opcion = menu()
        if (opcion == 1):

            antiguedad_promedio(integrantes)              
        
        elif (opcion == 2):

            promedio_global(integrantes)

        elif(opcion == 3):

            ranking_materias(integrantes)

        elif(opcion == 4):

            integrantes_ingresados(integrantes)
        
        pregunta:str = input("desea hacer otra consulta(s/n): ")
        if (pregunta == 'n'):
            opcion:int = 0
        else:
            opcion = 1


    print("Gracias por usar nuestro programa!!!")

main()

