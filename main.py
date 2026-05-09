import tkinter as tk
from interfaz import AplicacionFisica

def main():
    root = tk.Tk()
    app = AplicacionFisica(root)
    root.mainloop()

if __name__ == "__main__":
    main()