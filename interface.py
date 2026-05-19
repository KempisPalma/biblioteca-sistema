import tkinter as tk
from  db_biblioteca import obtener_libros_iniciales
from buscar import Buscador

ventana = tk.Tk()
ventana.title("Biblioteca")

alto_ventana = ventana.winfo_screenheight()
ancho_ventana = ventana.winfo_screenwidth()
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido a la Biblioteca!", font=("Arial", 24))
caja_busqueda = tk.Entry(ventana, font=("Arial", 16))
boton_buscar = tk.Button(ventana, text="Buscar", font=("Arial", 16))
mostrar_resultados = tk.Text(ventana, font=("Arial", 14), width=80, height=20)

def buscar_libro():
    titulo = caja_busqueda.get()
    libros = obtener_libros_iniciales()
    buscar = Buscador()
    resultado = buscar.buscar_por_titulo(libros, titulo)
    mostrar_resultados.delete("1.0", tk.END) # limpia los mensajes para que no se acumulen
    if resultado:
        mostrar_resultados.insert(tk.END, f"Título: {resultado['titulo']}\n")
        mostrar_resultados.insert(tk.END, f"Autor: {resultado['autor']}\n")
        mostrar_resultados.insert(tk.END, f"ISBN: {resultado['isbn']}\n")
        mostrar_resultados.insert(tk.END, f"Año: {resultado['año']}\n")
        mostrar_resultados.insert(tk.END, f"Categoría: {resultado['categoria']}\n")
    else:
        mostrar_resultados.insert(tk.END, "Libro no encontrado.")           

 


if __name__ == "__main__":
    etiqueta_bienvenida.pack(pady=20)
    caja_busqueda.pack(pady=10)
    boton_buscar.pack(pady=10)
    mostrar_resultados.pack(pady=10)
    boton_buscar.config(command=buscar_libro)
    ventana.mainloop()






