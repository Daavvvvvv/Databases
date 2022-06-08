--ESTUDIANTES CON MAYOR CANTIDAD DE PRESTAMOS--

SELECT id_Lector, Lib_Prestados
FROM Estudiante
ORDER BY Lib_Prestados DESC

--FECHAS EN LAS QUE DEBE SER DEVUELTO UN LIBRO--

SELECT FechaDevolucion, id_Libro
FROM Prestamo AS P
GROUP BY id_Libro, FechaDevolucion

--AREAS DE CONOCIMIENTO QUE REQUIEREN COMPRA DE LIBROS--

SELECT Area, count(*) AS Cantidad_Libros
FROM Libro
GROUP BY Area 
ORDER BY count(*) ASC

--DATOS DE LAS EDITORIALES--

SELECT * 
FROM Editorial

--CARRERA A LA QUE PERTENECEN LOS ESTUDIANTES--

SELECT id_Lector, Nombre, Carrera
FROM Estudiante

--CANTIDAD DE MULTAS--

SELECT Count(M.valorMulta) as Cantidad_Multas
FROM MultEst as M
HAVING count(M.valorMulta) > 0

--CARRERAS--

SELECT E.Carrera
FROM Estudiante as E
GROUP BY E.Carrera
