import tkinter as tk
from tkinter import ttk


def realizar_calculo():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error al calcular")


def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)


def borrar():
    entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

style = ttk.Style()
style.theme_use("clam")

entrada = ttk.Entry(ventana, font=("Segoe UI", 16))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == '=':
        boton = ttk.Button(ventana, text=texto, command=realizar_calculo)
    else:
        boton = ttk.Button(ventana, text=texto,
                           command=lambda t=texto: agregar_caracter(t))
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="news")

borrar_boton = ttk.Button(ventana, text="Borrar", command=borrar)
borrar_boton.grid(row=5, column=0, columnspan=4, padx=10, pady=5, sticky="we")

ventana.mainloop()
