import sqlite3

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro, titulo, anio, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio = anio
        self.autor = autor 

    def __str__(self):
        return f"Libro: '{self.titulo}' ({self.anio}) - {self.autor}"



conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        nacionalidad TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        anio INTEGER,
        autor_id INTEGER
    );
""")
conexion.commit()



def registrar_autor(nombre, nacionalidad):
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?);", (nombre, nacionalidad))
    conexion.commit()
    return cursor.lastrowid


def registrar_libro(titulo, anio, autor_id):
    cursor.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?);", (titulo, anio, autor_id))
    conexion.commit()


def listar_libros():
    query = """
        SELECT libros.id, libros.titulo, libros.anio, autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id;
    """
    cursor.execute(query)
    filas = cursor.fetchall()
    
    lista_resultado = []
    for fila in filas:
        autor = Autor(fila[3], fila[4], fila[5])
        libro = Libro(fila[0], fila[1], fila[2], autor)
        lista_resultado.append(libro)
        
    return lista_resultado


def actualizar_libro(id_libro, nuevo_titulo):
    cursor.execute("UPDATE libros SET titulo = ? WHERE id = ?;", (nuevo_titulo, id_libro))
    conexion.commit()


def eliminar_libro(id_libro):
    cursor.execute("DELETE FROM libros WHERE id = ?;", (id_libro,))
    conexion.commit()

id_gabriel = registrar_autor("Gabriel García Márquez", "Colombiana")
id_borges = registrar_autor("Jorge Luis Borges", "Argentina")

registrar_libro("Cien años de soledad", 1967, id_gabriel)
registrar_libro("El amor en los tiempos del cólera", 1985, id_gabriel)
registrar_libro("El Aleph", 1949, id_borges)

print("--- LISTA INICIAL ---")
for libro in listar_libros():
    print(libro)

actualizar_libro(1, "Cien Años de Soledad (Edición Especial)")
eliminar_libro(2)

print("\n--- LISTA FINAL (Modificada) ---")
for libro in listar_libros():
    print(libro)

conexion.close()
