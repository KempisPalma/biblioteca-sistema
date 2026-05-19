
"""
Datos iniciales (semilla) para la biblioteca.
Contiene 50 libros de prueba con diferentes categorías.
"""

def obtener_libros_iniciales():
    """
    Retorna una lista de diccionarios con datos de libros.
    Cada diccionario tiene: titulo, autor, isbn, año, categoria
    """
    return [
        # Ficción (10 libros)
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "isbn": "978-0307474728", "año": 1967, "categoria": "Ficción"},
        {"titulo": "1984", "autor": "George Orwell", "isbn": "978-0451524935", "año": 1949, "categoria": "Ficción"},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "isbn": "978-0060934347", "año": 1605, "categoria": "Ficción"},
        {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "isbn": "978-0156012195", "año": 1943, "categoria": "Ficción"},
        {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "isbn": "978-0446310789", "año": 1960, "categoria": "Ficción"},
        {"titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "isbn": "978-0743273565", "año": 1925, "categoria": "Ficción"},
        {"titulo": "Crimen y castigo", "autor": "Fiódor Dostoyevski", "isbn": "978-0486415871", "año": 1866, "categoria": "Ficción"},
        {"titulo": "La Odisea", "autor": "Homero", "isbn": "978-0140268867", "año": -800, "categoria": "Ficción"},
        {"titulo": "Ulises", "autor": "James Joyce", "isbn": "978-0199535675", "año": 1922, "categoria": "Ficción"},
        {"titulo": "En busca del tiempo perdido", "autor": "Marcel Proust", "isbn": "978-0141180311", "año": 1913, "categoria": "Ficción"},
        
        # Ciencia Ficción (10 libros)
        {"titulo": "Dune", "autor": "Frank Herbert", "isbn": "978-0441172719", "año": 1965, "categoria": "Ciencia Ficción"},
        {"titulo": "Fundación", "autor": "Isaac Asimov", "isbn": "978-0553293357", "año": 1951, "categoria": "Ciencia Ficción"},
        {"titulo": "Neuromante", "autor": "William Gibson", "isbn": "978-0441569595", "año": 1984, "categoria": "Ciencia Ficción"},
        {"titulo": "El juego de Ender", "autor": "Orson Scott Card", "isbn": "978-0812550702", "año": 1985, "categoria": "Ciencia Ficción"},
        {"titulo": "Guía del autoestopista galáctico", "autor": "Douglas Adams", "isbn": "978-0345391803", "año": 1979, "categoria": "Ciencia Ficción"},
        {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "isbn": "978-1451673319", "año": 1953, "categoria": "Ciencia Ficción"},
        {"titulo": "Un mundo feliz", "autor": "Aldous Huxley", "isbn": "978-0060850524", "año": 1932, "categoria": "Ciencia Ficción"},
        {"titulo": "¿Sueñan los androides con ovejas eléctricas?", "autor": "Philip K. Dick", "isbn": "978-0345404473", "año": 1968, "categoria": "Ciencia Ficción"},
        {"titulo": "La guerra de los mundos", "autor": "H.G. Wells", "isbn": "978-0451530653", "año": 1898, "categoria": "Ciencia Ficción"},
        {"titulo": "Snow Crash", "autor": "Neal Stephenson", "isbn": "978-0553380958", "año": 1992, "categoria": "Ciencia Ficción"},
        
        # Terror (10 libros)
        {"titulo": "Drácula", "autor": "Bram Stoker", "isbn": "978-0486411095", "año": 1897, "categoria": "Terror"},
        {"titulo": "Frankenstein", "autor": "Mary Shelley", "isbn": "978-0486282114", "año": 1818, "categoria": "Terror"},
        {"titulo": "It (Eso)", "autor": "Stephen King", "isbn": "978-1501142970", "año": 1986, "categoria": "Terror"},
        {"titulo": "El resplandor", "autor": "Stephen King", "isbn": "978-0307743657", "año": 1977, "categoria": "Terror"},
        {"titulo": "El exorcista", "autor": "William Peter Blatty", "isbn": "978-0061007224", "año": 1971, "categoria": "Terror"},
        {"titulo": "Psicosis", "autor": "Robert Bloch", "isbn": "978-1590200186", "año": 1959, "categoria": "Terror"},
        {"titulo": "La llamada de Cthulhu", "autor": "H.P. Lovecraft", "isbn": "978-0143129455", "año": 1928, "categoria": "Terror"},
        {"titulo": "Cementerio de animales", "autor": "Stephen King", "isbn": "978-1501156700", "año": 1983, "categoria": "Terror"},
        {"titulo": "El extraño caso del Dr. Jekyll y Mr. Hyde", "autor": "Robert Louis Stevenson", "isbn": "978-0486266886", "año": 1886, "categoria": "Terror"},
        {"titulo": "Soy leyenda", "autor": "Richard Matheson", "isbn": "978-0765357151", "año": 1954, "categoria": "Terror"},
        
        # Historia (10 libros)
        {"titulo": "Sapiens: De animales a dioses", "autor": "Yuval Noah Harari", "isbn": "978-0062316097", "año": 2011, "categoria": "Historia"},
        {"titulo": "El diario de Ana Frank", "autor": "Ana Frank", "isbn": "978-0553577129", "año": 1947, "categoria": "Historia"},
        {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking", "isbn": "978-0553380163", "año": 1988, "categoria": "Historia"},
        {"titulo": "Armas, gérmenes y acero", "autor": "Jared Diamond", "isbn": "978-0393354324", "año": 1997, "categoria": "Historia"},
        {"titulo": "Historia del siglo XX", "autor": "Eric Hobsbawm", "isbn": "978-0679740742", "año": 1994, "categoria": "Historia"},
        {"titulo": "Los cañones de agosto", "autor": "Barbara Tuchman", "isbn": "978-0345476098", "año": 1962, "categoria": "Historia"},
        {"titulo": "Churchill", "autor": "Andrew Roberts", "isbn": "978-1101980996", "año": 2018, "categoria": "Historia"},
        {"titulo": "SPQR: Una historia de la antigua Roma", "autor": "Mary Beard", "isbn": "978-1631492228", "año": 2015, "categoria": "Historia"},
        {"titulo": "Guerra y paz", "autor": "León Tolstói", "isbn": "978-1400079988", "año": 1869, "categoria": "Historia"},
        {"titulo": "La segunda guerra mundial", "autor": "Winston Churchill", "isbn": "978-0395416853", "año": 1948, "categoria": "Historia"},
        
        # Ciencia (10 libros)
        {"titulo": "Cosmos", "autor": "Carl Sagan", "isbn": "978-0345539434", "año": 1980, "categoria": "Ciencia"},
        {"titulo": "El origen de las especies", "autor": "Charles Darwin", "isbn": "978-0451529060", "año": 1859, "categoria": "Ciencia"},
        {"titulo": "Una breve historia de casi todo", "autor": "Bill Bryson", "isbn": "978-0767908184", "año": 2003, "categoria": "Ciencia"},
        {"titulo": "El gen egoísta", "autor": "Richard Dawkins", "isbn": "978-0199291151", "año": 1976, "categoria": "Ciencia"},
        {"titulo": "Astrofísica para gente con prisa", "autor": "Neil deGrasse Tyson", "isbn": "978-0393609394", "año": 2017, "categoria": "Ciencia"},
        {"titulo": "La estructura de las revoluciones científicas", "autor": "Thomas Kuhn", "isbn": "978-0226458083", "año": 1962, "categoria": "Ciencia"},
        {"titulo": "El universo en una cáscara de nuez", "autor": "Stephen Hawking", "isbn": "978-0553802023", "año": 2001, "categoria": "Ciencia"},
        {"titulo": "Los dragones del Edén", "autor": "Carl Sagan", "isbn": "978-0345346292", "año": 1977, "categoria": "Ciencia"},
        {"titulo": "¿Qué es la vida?", "autor": "Erwin Schrödinger", "isbn": "978-1107604667", "año": 1944, "categoria": "Ciencia"},
        {"titulo": "Pensar rápido, pensar despacio", "autor": "Daniel Kahneman", "isbn": "978-0374533557", "año": 2011, "categoria": "Ciencia"},
    ]
