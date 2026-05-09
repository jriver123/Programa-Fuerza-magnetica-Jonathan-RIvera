import tkinter as tk
from tkinter import ttk, messagebox
import calculos_fisica as cf

class AplicacionFisica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Fuerza Magnética")
        # Ventana un poco más ancha para mayor comodidad
        self.root.geometry("580x750") 
        
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=True, fill='both')
        
        self.tab1 = ttk.Frame(notebook)
        self.tab2 = ttk.Frame(notebook)
        
        notebook.add(self.tab1, text='Escenario 1 (Carga)')
        notebook.add(self.tab2, text='Escenario 2 (Conductor)')
        
        self.construir_escenario_1()
        self.construir_escenario_2()

    def construir_escenario_1(self):
        ttk.Label(self.tab1, text="Datos de la Carga en Movimiento", font=('Arial', 12, 'bold')).pack(pady=10)
        
        frame_inputs = ttk.Frame(self.tab1)
        frame_inputs.pack(pady=10)
        
        ttk.Label(frame_inputs, text="Carga q (μC):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_q = ttk.Entry(frame_inputs, width=10); self.entry_q.insert(0, "-10")
        self.entry_q.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_inputs, text="Velocidad v <x,y,z> (x10^3 m/s):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_vx = ttk.Entry(frame_inputs, width=5); self.entry_vx.insert(0, "2")
        self.entry_vy = ttk.Entry(frame_inputs, width=5); self.entry_vy.insert(0, "-3.0")
        self.entry_vz = ttk.Entry(frame_inputs, width=5); self.entry_vz.insert(0, "5")
        self.entry_vx.grid(row=1, column=1); self.entry_vy.grid(row=1, column=2); self.entry_vz.grid(row=1, column=3)
        
        ttk.Label(frame_inputs, text="Campo B <x,y,z> (T):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_bx1 = ttk.Entry(frame_inputs, width=5); self.entry_bx1.insert(0, "-1")
        self.entry_by1 = ttk.Entry(frame_inputs, width=5); self.entry_by1.insert(0, "0.8")
        self.entry_bz1 = ttk.Entry(frame_inputs, width=5); self.entry_bz1.insert(0, "-3")
        self.entry_bx1.grid(row=2, column=1); self.entry_by1.grid(row=2, column=2); self.entry_bz1.grid(row=2, column=3)
        
        ttk.Button(self.tab1, text="Calcular Fuerza y Procedimiento", command=self.calcular_escenario_1).pack(pady=10)
        
        self.lbl_res1 = ttk.Label(self.tab1, text="F = < ?, ?, ? > N", font=('Arial', 12, 'bold'), foreground="blue")
        self.lbl_res1.pack(pady=5)

        # Frame contenedor para la caja de texto y su barra de desplazamiento
        frame_text = ttk.Frame(self.tab1)
        frame_text.pack(pady=10, padx=20, fill="both", expand=True)

        # Agregamos wrap=tk.WORD para que no corte palabras a la mitad
        self.texto_proc1 = tk.Text(frame_text, height=14, width=60, bg="#f0f0f0", font=('Courier', 9), wrap=tk.WORD)
        self.texto_proc1.pack(side=tk.LEFT, fill="both", expand=True)

        # Scrollbar vertical por si el texto es muy largo
        scrollbar = ttk.Scrollbar(frame_text, command=self.texto_proc1.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_proc1.config(yscrollcommand=scrollbar.set)

    def construir_escenario_2(self):
        ttk.Label(self.tab2, text="Datos del Conductor Rectilíneo", font=('Arial', 12, 'bold')).pack(pady=10)
        
        frame_inputs = ttk.Frame(self.tab2)
        frame_inputs.pack(pady=10)
        
        ttk.Label(frame_inputs, text="Punto P (x,y,z):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_px = ttk.Entry(frame_inputs, width=5); self.entry_px.insert(0, "-7")
        self.entry_py = ttk.Entry(frame_inputs, width=5); self.entry_py.insert(0, "4")
        self.entry_pz = ttk.Entry(frame_inputs, width=5); self.entry_pz.insert(0, "5")
        self.entry_px.grid(row=0, column=1); self.entry_py.grid(row=0, column=2); self.entry_pz.grid(row=0, column=3)
        
        ttk.Label(frame_inputs, text="Punto Q (x,y,z):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_qx = ttk.Entry(frame_inputs, width=5); self.entry_qx.insert(0, "8")
        self.entry_qy = ttk.Entry(frame_inputs, width=5); self.entry_qy.insert(0, "0")
        self.entry_qz = ttk.Entry(frame_inputs, width=5); self.entry_qz.insert(0, "-4")
        self.entry_qx.grid(row=1, column=1); self.entry_qy.grid(row=1, column=2); self.entry_qz.grid(row=1, column=3)
        
        ttk.Label(frame_inputs, text="Corriente I (A):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_i = ttk.Entry(frame_inputs, width=10); self.entry_i.insert(0, "20")
        self.entry_i.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame_inputs, text="Campo B <x,y,z> (T):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_bx2 = ttk.Entry(frame_inputs, width=5); self.entry_bx2.insert(0, "0.8")
        self.entry_by2 = ttk.Entry(frame_inputs, width=5); self.entry_by2.insert(0, "4")
        self.entry_bz2 = ttk.Entry(frame_inputs, width=5); self.entry_bz2.insert(0, "-2")
        self.entry_bx2.grid(row=3, column=1); self.entry_by2.grid(row=3, column=2); self.entry_bz2.grid(row=3, column=3)
        
        ttk.Button(self.tab2, text="Calcular Fuerza y Procedimiento", command=self.calcular_escenario_2).pack(pady=10)
        
        self.lbl_res2 = ttk.Label(self.tab2, text="F = < ?, ?, ? > N", font=('Arial', 12, 'bold'), foreground="blue")
        self.lbl_res2.pack(pady=5)

        # Frame contenedor para la caja de texto y su barra de desplazamiento
        frame_text = ttk.Frame(self.tab2)
        frame_text.pack(pady=10, padx=20, fill="both", expand=True)

        self.texto_proc2 = tk.Text(frame_text, height=14, width=60, bg="#f0f0f0", font=('Courier', 9), wrap=tk.WORD)
        self.texto_proc2.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_text, command=self.texto_proc2.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_proc2.config(yscrollcommand=scrollbar.set)

    def calcular_escenario_1(self):
        try:
            q = float(self.entry_q.get())
            v = [float(self.entry_vx.get())*1e3, float(self.entry_vy.get())*1e3, float(self.entry_vz.get())*1e3]
            b = [float(self.entry_bx1.get()), float(self.entry_by1.get()), float(self.entry_bz1.get())]
            
            fuerza, procedimiento = cf.calcular_fuerza_carga(q, v, b)
            
            self.lbl_res1.config(text=f"F = < {fuerza[0]:.4f}, {fuerza[1]:.4f}, {fuerza[2]:.4f} > N")
            self.texto_proc1.delete(1.0, tk.END)
            self.texto_proc1.insert(tk.END, procedimiento)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")

    def calcular_escenario_2(self):
        try:
            p = [float(self.entry_px.get()), float(self.entry_py.get()), float(self.entry_pz.get())]
            q = [float(self.entry_qx.get()), float(self.entry_qy.get()), float(self.entry_qz.get())]
            i = float(self.entry_i.get())
            b = [float(self.entry_bx2.get()), float(self.entry_by2.get()), float(self.entry_bz2.get())]
            
            fuerza, procedimiento = cf.calcular_fuerza_conductor(p, q, i, b)
            
            self.lbl_res2.config(text=f"F = < {fuerza[0]:.2f}, {fuerza[1]:.2f}, {fuerza[2]:.2f} > N")
            self.texto_proc2.delete(1.0, tk.END)
            self.texto_proc2.insert(tk.END, procedimiento)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")