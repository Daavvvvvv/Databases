import pyodbc as podbc

try:
    conexion = podbc.connect(
        DRIVER= '{SQL Server}',
        Server= 'DESKTOP-SDEUJ3C\SQLEXPRESS',
        Database= 'Proyecto',
        Trusted_Connection= 'Yes'
    )
except Exception:
    print("No se pudo conectar al sistema")

while True:

    print("**********************************************\n"
    "**********************************************\n"
    "**********************************************\n"
    "**********************************************\n"
    "**********************************************\n"
    "**********************************************\n"
    "\n"
    "Bienvenido/a a la base de datos\n"
    "PULSE 1 PARA INSERTAR LOS DATOS DE UN NUEVO ESTUDIANTE\n"
    "PULSE 2 PARA ACTUALIZAR UN ESTUDIANTE\n"
    "PULSE 3 PARA ELIMINAR UN ESTUDIANTE\n"
    "PULSE 0 PARA SALIR DEL PROGRAMA")
    opcion= int(input("Digite una opcion= "))


    



    if opcion ==1:
        cursorInsert = conexion.cursor()

        id_Lector= int(input("digite el id del estudiante= "))
        CI= input("Digite el documento de identidad del estudiante= ")
        Nombre= input("Digite el nombre del estudiante= ")
        Direccion= input("Digite la direccion del estudiante= ")
        Carrera= int(input("Digite la carrera del estudiante= "))
        Edad= int(input("Digite la edad del estudiante= "))
        cantPrest= int(input("Digite la cantidad de libros prestados al estudiante= "))


        consulta= "Insert into Estudiante(id_Lector, CI, Nombre, Direccion, Carrera, Edad, cantPrest) values ("+id_Lector+",'"+CI+"'"+",'"+Nombre+"'"+",'"+Direccion+"'"+","+Carrera+","+Edad+","+cantPrest+");"

        
        cursorInsert.execute(consulta)

        cursorInsert.commit()
        print("Se agrego este usuario con Exito")
        cursorInsert.close()


    if opcion == 2:

        cursorVerificacion= conexion.cursor()
        id_Lector= input("Insertar la id del estudiante= ")

        consultaVerificacion= ("Select id_Lector from Estudiante where id_Lector= ?")
        cursorVerificacion.execute(consultaVerificacion,(id_Lector))
        resultado= cursorVerificacion.fetchone()

        if resultado:

            while True:

                print("Elija la opcion de lo que quiere actualizar\n"
                "1 SE ACTUALIZA CI\n"
                "2 SE ACTUALIZA NOMBRE\n"
                "3 SE ACTUALIZA DIRECCION\n"
                "4 SE ACTUALIZA CARRERA\n"
                "5 SE ACTUALIZA EDAD\n"
                "6 SE ACTUALIZA LA CANTIDAD PRESTADA\n"
                "0 PARA SALIR")
                opcion1= int(input("Escoja la opcion= "))
                
                if opcion1 == 0:
                    break

                if opcion1 == 1:
                    try:
                        CINueva= input("Insertar cual es la nueva CI= ")
                        cursorUpdate= conexion.cursor()
                        consulta = "Update Estudiante set CI = ? where id_Lector = ?"
                        
                        
                        

                        cursorUpdate.execute(consulta, (CINueva, id_Lector))
                        
                        cursorUpdate.commit()
                        print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente el CI\n")
                        cursorUpdate.close()
                    except Exception:
                        print("No se pudo actualizar la base de datos")
                
                if opcion1 ==2:
                    cursorUpdate= conexion.cursor()
                    consulta = "Update Estudiante set Nombre = ? where id_Lector = ?"
                    
                    Nombre= input("Insertar el nuevo nombre= ")
                    


                    cursorUpdate.execute(consulta, (Nombre, id_Lector))
                    
                    cursorUpdate.commit()
                    print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente el NOMBRE\n")
                    cursorUpdate.close()
                
                if opcion1==3:
                    cursorUpdate= conexion.cursor()
                    consulta = "Update Estudiante set Direccion = ? where id_Lector = ?"
                    
                    Direccion= input("Insertar cual es la nueva Direccion= ")
                    


                    cursorUpdate.execute(consulta,(Direccion,id_Lector))
                    
                    cursorUpdate.commit()
                    print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente la DIRECCION\n")
                    cursorUpdate.close()

                if opcion1==4:
                    cursorUpdate= conexion.cursor()
                    consulta = "Update Estudiante set Carrera = ? where id_Lector = ?"
                    
                    Carrera= input("Insertar cual es la nueva Carrera= ")
                    


                    cursorUpdate.execute(consulta,(Carrera,id_Lector))
                    
                    cursorUpdate.commit()
                    print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente la CARRERA\n")
                    cursorUpdate.close()
                
                if opcion1==5:
                    cursorUpdate= conexion.cursor()
                    consulta = "Update Estudiante set Edad = ? where id_Lector = ?"
                    
                    Edad= input("Insertar cual es la nueva Edad= ")
                    


                    cursorUpdate.execute(consulta,(Edad,id_Lector))
                    
                    cursorUpdate.commit()
                    print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente la EDAD\n")
                    cursorUpdate.close()

                if opcion1==6:
                    cursorUpdate= conexion.cursor()
                    consulta = "Update Estudiante set cantPrest = ? where id_Lector = ?"
                    
                    cantPrest= input("Insertar cual es la nueva cantidad prestada= ")
                    


                    cursorUpdate.execute(consulta,(cantPrest,id_Lector))
                    
                    cursorUpdate.commit()
                    print(
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "**********************************************\n"
                        "Se actualizo correctamente la CANTIDAD PRESTADA\n")
                    cursorUpdate.close()

        else:
            print("No hay ningun usuario con ese id")
            break


    if opcion == 3:

        cursorVerificacion= conexion.cursor()
        print("Cual estudiante quiere eliminar?")
        id_Lector= input("Insertar la id del estudiante= ")

        consultaVerificacion= ("Select id_Lector from Estudiante where id_Lector= ?")
        cursorVerificacion.execute(consultaVerificacion,(id_Lector))
        resultado= cursorVerificacion.fetchone()

        if resultado:
            cursorEliminar= conexion.cursor()

            consulta= "delete from Estudiante where id_Lector = ?"
            


            cursorEliminar.execute(consulta,id_Lector)

            cursorEliminar.commit()
            print("Se ha borrado con exito al estudiante identificado con= " + id_Lector )
            cursorEliminar.close()
        else:
            print("No existe este numero de identificacion")
            break

    if opcion == 0:
        break