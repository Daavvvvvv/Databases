import pyodbc as podbc

try:
    conexion = podbc.connect(
        DRIVER= '{SQL Server}',
        Server= 'DESKTOP-SDEUJ3C\SQLEXPRESS',
        Database= 'Proyectoo',
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
    "PULSE 4 PARA PONERLE MULTA A UN ESTUDIANTE\n"
    "PULSE 5 PARA HACER UNA CONSULTA\n"
    "PULSE 0 PARA SALIR DEL PROGRAMA")
    opcion= int(input("Digite una opcion= "))


    



    if opcion ==1:
        cursorInsert = conexion.cursor()

        id_Lector= input("digite el id del estudiante= ")
        CI= input("Digite el documento de identidad del estudiante= ")
        Nombre= input("Digite el nombre del estudiante= ")
        Direccion= input("Digite la direccion del estudiante= ")
        Carrera= input("Digite la carrera del estudiante= ")
        Edad= input("Digite la edad del estudiante= ")
        cantPrest= input("Digite la cantidad de libros prestados al estudiante= ")


        consulta= "Insert into Estudiante(id_Lector, CI, Nombre, Direccion, Carrera, Edad, cantPrest) values ("+id_Lector+",'"+CI+"'"+",'"+Nombre+"'"+",'"+Direccion+"'"+","+Carrera+","+Edad+","+cantPrest+");"
        consulta1= "Insert into MultEst(id_Lector, Devolucion) values ("+id_Lector+",'0')"

        
        cursorInsert.execute(consulta)
        cursorInsert.execute(consulta1)

        cursorInsert.commit()
        print("Se agrego este usuario con Exito")
        cursorInsert.close()


    elif opcion == 2:

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
                "6 SE ACTUALIZA LOS LIBROS PRESTADOS\n"
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
                    try:
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
                    except Exception:
                        print("No se pudo actualizar la base de datos")
                
                if opcion1==3:
                    try:
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
                    except Exception:
                        print("No se pudo actualizar la base de datos")

                if opcion1==4:
                    try:
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
                    except Exception:
                        print("No se pudo actualizar la base de datos")
                if opcion1==5:
                    try:
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
                    except Exception:
                        print("No se pudo actualizar la base de datos")

                if opcion1==6:
                    try:
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
                    except Exception:
                        print("No se pudo actualizar la base de datos")

        else:
            print("No hay ningun usuario con ese id")
            break


    elif opcion == 3:



        cursorVerificacion= conexion.cursor()
        id_Lector= input("Insertar la id del estudiante= ")

        consultaVerificacion= ("Select id_Lector from Estudiante where id_Lector= ?")
        cursorVerificacion.execute(consultaVerificacion,(id_Lector))
        resultado= cursorVerificacion.fetchone()

        

        if resultado:
            cursorEliminar= conexion.cursor()

            consulta= "delete from Estudiante where id_Lector = ?"
            consula1= "delete from MultEst where id_Lector = ?"
            

            cursorEliminar.execute(consula1,id_Lector)
            cursorEliminar.execute(consulta,id_Lector)

            cursorEliminar.commit()
            print("Se ha borrado con exito al estudiante identificado con= " + id_Lector )
            cursorEliminar.close()
        else:
            print("No existe este numero de identificacion")
            break 


    elif opcion ==4:
        cursorVerificacion= conexion.cursor()
        id_Lector= input("Insertar la id del estudiante= ")

        consultaVerificacion= ("Select id_Lector from Estudiante where id_Lector= ?")
        cursorVerificacion.execute(consultaVerificacion,(id_Lector))
        resultado= cursorVerificacion.fetchone()

        if resultado:
            try:
                
                cursormulta= conexion.cursor()
                si= 's'
                no= 'n'

                multa= input("¿El estudiante entrego el libro dentro del plazo?\n"
                "s para si\n"
                "n para no\n")
                
                if multa == si:
                    consulta= "Update MultEst set Devolucion = ?, valorMulta=? where id_Lector = ?"

                    cursormulta.execute(consulta,('1','0',id_Lector))
                    cursormulta.commit()
                    print("El estudiante " + id_Lector + " Ya devolvio el libro" )
                    cursormulta.close()
                elif multa == no:
                    consulta= "Update MultEst set Devolucion = ?, valorMulta =? where id_Lector = ?"
                    multaa= input("Valor de la multa? ")
                    cursormulta.execute(consulta,('0',multaa,id_Lector))
                    cursormulta.commit()
                    print("El estudiante " + id_Lector + " No ha devuelto el libro y tiene = "+multaa+" de multa")
                    cursormulta.close()
            except Exception as e:
                print("No se pudo actualizar la base de datos")

    
    elif opcion == 5:

        print("**********************************************\n"
        "**********************************************\n"
        "**********************************************\n"
        "**********************************************\n"
        "**********************************************\n"
        "**********************************************\n"
        "\n"
        "QUE CONSULTA DESEA REALIZAR\n?"
        "PULSE 1 PARA VER LOS ESTUDIANTES CON MAYOR CANTIDAD DE PRESTAMOS\n"
        "PULSE 2 PARA VER LAS FECHAS EN LAS QUE DEBE SER DEVUELTO UN LIBRO\n"
        "PULSE 3 PARA VER LAS AREAS DE CONOCIMIENTO QUE REQUIEREN COMPRA DE LIBROS\n"
        "PULSE 4 PARA VER LA CARRERA A LA QUE PERTENECEN LOS ESTUDIANTES\n"
        "PULSE 5 PARA VER LA CANTIDAD DE MULTAS\n"
        "PULSE 6 PARA VER LAS CARRERAS\n"
        "PULSE 0 PARA SALIR DEL PROGRAMA")
        consult= int(input("Digite una opcion= "))

        if consult == 1:
            mayorPrestamo= conexion.cursor()
            mayorPrestamo.execute("SELECT id_Lector, Lib_Prestados FROM Estudiante ORDER BY Lib_Prestados DESC")

            persona= mayorPrestamo.fetchone()
            print("ESTUDIANTES CON MAYOR CANTIDAD DE PRESTAMOS\n")
            while persona:

                print("ID_LECTOR, LIBROS PRESTADOS \n",(persona))
                persona= mayorPrestamo.fetchone()
            
            mayorPrestamo.close()
            conexion.close()
            break

        elif consult == 2:
            Devolucion= conexion.cursor()
            Devolucion.execute("SELECT FechaDevolucion, id_Libro FROM Prestamo AS P GROUP BY id_Libro, FechaDevolucion")

            prestamo= Devolucion.fetchone()
            print("FECHAS EN LAS QUE DEBE SER DEVUELTO UN LIBRO\n")
            while prestamo:
                print("FechaDevolucion, IDLIBRO\n",(prestamo))
                prestamo= Devolucion.fetchone()

            Devolucion.close()
            conexion.close()
            break

        elif consult == 3:
            areas= conexion.cursor()
            areas.execute("SELECT Area, count(*) AS Cantidad_Libros FROM Libro GROUP BY Area  ORDER BY count(*) ASC")

            areass= areas.fetchone()
            print("AREAS DE CONOCIMIENTO QUE REQUIEREN COMPRA DE LIBROS\n")
            while areass:
                print("AREA, CANTIDAD LIBROS\n", (areass))
                areass = areas.fetchone()
            
            areas.close()
            conexion.close()
            break

        elif consult == 4:
            datos= conexion.cursor()
            datos.execute("SELECT * FROM Editorial")

            datoss= datos.fetchone()
            while datoss:
                print("IDLIBRO, EDITORIAL, NOMBRE EDITORIAL\n",(datoss))
                datoss= datos.fetchone()
            
            datos.close()
            conexion.close()
            break

        elif consult == 5:
            carrera= conexion.cursor()
            carrera.execute("SELECT id_Lector, Nombre, Carrera FROM Estudiante")

            carreraa= carrera.fetchone()
            while carreraa:
                print("IDLECTOR, NOMBRE, CARRERA\n",(carreraa))
                carreraa= carrera.fetchone()
            
            carrera.close()
            conexion.close()
            break

        elif consult == 6:
            cantmult= conexion.cursor()
            cantmult.execute("SELECT id_Lector, Count(M.valorMulta) as Cantidad_Multas FROM MultEst as M WHERE(M.valorMulta) > 0 GROUP BY M.id_Lector, M.valorMulta")

            cantmultt= cantmult.fetchone()
            while cantmultt:
                print("ID LECTOR, CANTIDAD MULTAS\n",(cantmultt))
                cantmultt= cantmult.fetchone()

            cantmult.close()
            conexion.close()
            break

        elif consult== 7:
            asd= conexion.cursor()
            asd.execute("SELECT E.Carrera FROM Estudiante as E GROUP BY E.Carrera")

            asdd= asd.fetchone()
            while asdd:
                print("CARRERA",(asdd))
                asdd= asd.fetchone()

            asd.close()
            conexion.close()
            break
        
        elif consult==0:
            break
        

    elif opcion == 0:
        break