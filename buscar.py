from db_biblioteca import obtener_libros_iniciales

class Buscador:
    """Servicio de búsqueda de libros en la biblioteca"""

    def buscar_por_titulo(self,libros:list[dict],titulo:str)->str:
        libros_ordenados = sorted(libros, key=lambda x: x["titulo"])
        inicio = 0
        fin = len(libros_ordenados)-1
        while inicio <= fin:
            medio = (inicio+fin)//2
            if libros_ordenados[medio]["titulo"] == titulo:
                return libros_ordenados[medio]
            elif libros_ordenados[medio]["titulo"] < titulo:
                inicio = medio + 1
            else:
                fin = medio - 1


    def buscar_por_isbn(self,libros:list[dict],isbn)->dict:
        libros_ordenados = sorted(libros, key=lambda x: x["isbn"])
        inicio = 0
        fin = len(libros_ordenados)-1
        while inicio <= fin:
            medio = (inicio+fin)//2
            if libros_ordenados[medio]["isbn"] == isbn:
                return libros_ordenados[medio]
            elif libros_ordenados[medio]["isbn"] < isbn:
                inicio = medio + 1
            else:
                fin = medio - 1
                
if __name__ == "__main__":
    mis_libros = obtener_libros_iniciales()
    buscador = Buscador()
    resultado_titulo = buscador.buscar_por_titulo(mis_libros, "Dune")
    resultado_isbn = buscador.buscar_por_isbn(mis_libros, "978-0441172719")
    print("Resultado por título:", resultado_titulo)
    print("Resultado por ISBN:", resultado_isbn)