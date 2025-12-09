#Importamos la libreria pertinente para poder conectar con la base datos creada en el examen de base de datos
import mysql.connector
#Nos conectamos con el usuario Manolo
conexion = mysql.connector.connect(
    host="localhost",
    user="Manolo",
    password="Portafolio123$",
    database="portafolioexamen"
)
print("Buenas dias")
cursor = conexion.cursor()
while True:
    print("Escoje una opcion: ")
    print("1.Insertar una pieza")
    print("2Listar clientes")
    print("3.Actualizar un cliente")
    print("4.Eliminar un cliente")
    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        titulitis = input("Titulo: ")    
        descripcion = input("Descripcion: ")
        fecha = input("Fecha: ")
        id_categoria = input("id de la categoria:")

        sql = "insert into piezasportafolio (titulitis, descripcion, fecha, id_categoria) VALUES (%s,%s,%s,%s)"
        VALUES = (titulitis,descripcion,fecha,id_categoria)
        cursor.execute(sql, VALUES)
        conexion.commit()

        print("pieza insertada exitosamente")
    elif opcion == 2:
        cursor.execute("Select * FROM piezasportafolio")
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
    elif opcion == 3:
        id_pieza = input("Selecciona el id de la pieza a actualizar: ")
        nuevo_titulitis = input("Nuevo Titulo: ")
        sql = "UPDATE piezasportafolio SET titulitis = %s WHERE id =%s"
        cursor.execute(sql, (nuevo_titulitis,id_pieza))
        conexion.commit()
        print("Pieza actualizada correctamente")
    elif opcion == 4:
        id_pieza = input("Elige el id de la pieza a eliminar: ")
        sql = "DELETE FROM piezasportafolio WHERE id = %s"
        cursor.execute(sql(id_pieza))
        conexion.commit
