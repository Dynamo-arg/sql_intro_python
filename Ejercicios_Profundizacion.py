#!/usr/bin/env python

__author__ = "Sebastian Volpe"
__version__ = "1.1"

import sqlite3
import csv


def create_schema():

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    c.execute("""
                DROP TABLE IF EXISTS libros;
            """)

    c.execute("""
            CREATE TABLE libros(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] TEXT NOT NULL,
                [pags] INTEGER,
                [author] TEXT
            );
            """)

    conn.commit()
    conn.close()

def fill():
    with open('libreria.csv') as csvfile:
        data = list(csv.reader(csvfile))
        
    cantidad_filas = len(data)

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    for i in range(1,cantidad_filas):
        c.execute("""
                INSERT INTO libros (title, pags, author)
                VALUES (?,?,?);""", data[i])

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def fetch(opc):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    if opc == 0:
        for row in c.execute('SELECT * FROM libros'):
            print(row)
    
    else:
        try:
            sql = "SELECT * FROM libros WHERE id=?"
            c.execute(sql,opc)
            row = c.fetchone()
            print(row)
        except:
            print("ID no Valido")

def search_author(autor):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    sql = "SELECT author FROM libros WHERE title=?"
    c.execute(sql,[autor])
    row = c.fetchone()

    if row == None:
        print("Autor no encontrado")
    else:
        return print("Autor del Libro:",row)



def delete(libro):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    rowcount = c.execute("DELETE FROM libros WHERE title =?", (libro,)).rowcount

    if rowcount == 0:
        print("Libro no encontrado")
    
    else:
        print("Libro borrado exitosamente")

    conn.commit()
    conn.close()

def update_titulo(id, title):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE libros SET title =? WHERE id =?",(title, str(id))).rowcount

    if rowcount == 0:
        print("Libro no encontrado")
    else:
        print("Libro actualizado exitosamente")

    conn.commit()
    conn.close()





if __name__ == '__main__':

    create_schema()
    fill()

    valor = str(input("Ingrese ID a consultar\n"))
    fetch(valor)

    search_author('El libro de Arena')

    borrar_libro = str(input("Ingrese Titulo del libro a borrar\n"))
    delete(borrar_libro)

    update_titulo(3,"Modificar prueba")