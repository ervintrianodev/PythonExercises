# Manejo de archivos

from os import path
import os

file_path='/home/evans/Cursos/PythonGemini/files/'

def create_file(filename):
    try:
        if file_exists(filename):mode="w"
        else: mode="x"
        with open(file_path+filename, mode) as f:
            f.write("Hola mundo desde Python")
    except (IOError, FileNotFoundError) as e:
        print("No se pudo crear o abrir el archivo")
    else:
        print("El archivo se ha creado.")


def file_exists(filename):
    return path.exists(file_path+filename)

def read_file(filename):
    try:
        if not file_exists(filename):
            raise FileNotFoundError(f"EL archivo {filename} no existe")
        with open(file_path + filename, "r") as file:
            print(file.readlines())
    except (IOError, FileNotFoundError) as e:
        print(f"Error al leer el archivo {filename}: {e}")



def delete_file(filename):
    if file_exists(filename):
        os.remove(file_path+filename)
        print(f"El archivo {filename} se ha eliminado!")
    else:
        print(f"No se puedo eliminar porque el archivo {filename} no existe")

def count_words(filename):
    if file_exists(filename):
        try:
            with open(file_path+filename, "r") as file:
                word_count=0
                for line in file:
                    word_count += len(line.split())
                print(f"El archio {filename} tiene {word_count} palabras")
        except (FileNotFoundError, IOError) as e:
            print(f"Error al leer el archivo {filename} : {e}")

    else:
        print(f"EL archivo {filename} no existe!")

if __name__=="__main__":
    filename="example.txt"
    #create_file(filename)
    #read_file(filename)
    #count_words(filename)
    delete_file(filename)

