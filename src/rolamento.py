import tkinter as tk
from tkinter import messagebox

import numpy as np

#======================================
#   GLOBAIS
#======================================

#======================================
#   GUI
#======================================
class RolamentoGUI(tk.Tk):

    # Construtor padrao
    def __init__(self):
        super().__init__()

        self.diametro = 0 # (mm)
        self.rpm = 0
        self.horas = 0

        self.fh = 0 # Coeficiente de Vida (adimensional)
        self.fn = 0 # Coeficiente de Rotacao (adimensional)
        self.P = 0 # Carga Dinamica Equivalente (kN)
        self.C = 0 # Capacidade de carga dinamica (kN)

        self.x = 0 # Fator Radial (adimensional)
        self.y = 0 # Fator Axial (adimensional)
        self.Fr = 0 # CArga Radial (kN)
        self.Fa = 0 # CArga Axial (kN)

        # Capacidade de Carga Basica
        self.C0r = 0
        self.Cr = 0
        self.f0 = 0

        self.e = 0

        self.title("Dimensionador de Rolamentos")

        self.geometry("640x480+100+100")

        self.create_labels()
        self.create_inputs()
        self.create_buttons()
        self.make_grid()

    def capacidade_de_carga_dimanica(self):
        self.C = self.fh / self.fn * self.P

    def carga_dinamica_equivalente(self):
        self.P = self.x * self.Fr + self.y * self.Fa

    def carga_dinamica_equivalente_relacao(self):
        return (self.f0 * self.Fa) / self.C0r
    
    # y = y0 + (y1 - y0)*(x - x0)/(x1 - x0)
    # Nesta função abaixo, so fiz resolver em funcao
    # de "x" ( = e) para achar o valor de "e"
    def interpolacao_linear(self, y0, y1, y, x0, x1):
        return (x0 + (x1 - x0)*(y - y0)/(y1 - y0))

    # Cria as labels de texto para mostrar
    # ao usuario os campos de inputs
    def create_labels(self):
        self.label_d = tk.Label(self, text="Diametro")
        self.label_rpm = tk.Label(self, text="RPM")
        self.label_fh = tk.Label(self, text="fh")
        self.label_fn = tk.Label(self, text="fn")
        self.label_Fr = tk.Label(self, text="Fr")
        self.label_Fa = tk.Label(self, text="Fa")
        self.label_Cr = tk.Label(self, text="Cr")
        self.label_C0r = tk.Label(self, text="C0r")
        self.label_f0 = tk.Label(self, text="f0")

        self.label_e0 = tk.Label(self, text="e0")
        self.label_y0 = tk.Label(self, text="y0")
        self.label_e1 = tk.Label(self, text="e1")
        self.label_y1 = tk.Label(self, text="y1")


    # Cria os inputs para o usuario
    def create_inputs(self):
        self.entry_d = tk.Entry(self)
        self.entry_rpm = tk.Entry(self)
        self.entry_fh = tk.Entry(self)
        self.entry_fn = tk.Entry(self)
        self.entry_Fr = tk.Entry(self)
        self.entry_Fa = tk.Entry(self)
        self.entry_Cr = tk.Entry(self)
        self.entry_C0r = tk.Entry(self)
        self.entry_f0 = tk.Entry(self)
    
        self.entry_e0 = tk.Entry(self)
        self.entry_y0 = tk.Entry(self)
        self.entry_e1 = tk.Entry(self)
        self.entry_y1 = tk.Entry(self)

    # Cria os botoes
    def create_buttons(self):
        self.button = tk.Button(self, text="Calcular", command=self.rotina_calcular)

    # Organiza as grades para organizacao
    # dos componentes da janela
    def make_grid(self):

        # Vetor de grid de linhas para as
        # posicoes do grid dos elementos
        grid_rows = []
        for i in range(0, 12):
            grid_rows.append(i)

        self.label_d.grid(row=grid_rows[0], column=0, sticky='W', padx=4, pady=4)
        self.entry_d.grid(row=grid_rows[0], column=1, padx=4 ,pady=4)

        self.label_rpm.grid(row=grid_rows[1], column=0, sticky='W', padx=4, pady=4)
        self.entry_rpm.grid(row=grid_rows[1], column=1, padx=4 ,pady=4)

        self.label_Fr.grid(row=grid_rows[2], column=0, sticky='W', padx=4, pady=4)
        self.entry_Fr.grid(row=grid_rows[2], column=1, padx=4, pady=4)

        self.label_Fa.grid(row=grid_rows[3], column=0, sticky='W', padx=4, pady=4)
        self.entry_Fa.grid(row=grid_rows[3], column=1, padx=4, pady=4)

        self.label_fh.grid(row=grid_rows[4], column=0,sticky='W', padx=4, pady= 4)
        self.entry_fh.grid(row=grid_rows[4], column=1, padx=4 ,pady=4)

        self.label_fn.grid(row=grid_rows[5], column=0, sticky='W', padx=4, pady=4)
        self.entry_fn.grid(row=grid_rows[5], column=1, padx=4, pady=4)

        self.label_Cr.grid(row=grid_rows[6], column=0, sticky='W', padx=4, pady=4)
        self.entry_Cr.grid(row=grid_rows[6], column=1, padx=4, pady=4)

        self.label_C0r.grid(row=grid_rows[7], column=0, sticky='W', padx=4, pady=4)
        self.entry_C0r.grid(row=grid_rows[7], column=1, padx=4, pady=4)

        self.label_f0.grid(row=grid_rows[8], column=0, sticky='W', padx=4, pady=4)
        self.entry_f0.grid(row=grid_rows[8], column=1, padx=4, pady=4)

        self.label_e0.grid(row=grid_rows[9], column=0, sticky="W", padx=4, pady=4)
        self.entry_e0.grid(row=grid_rows[9], column=1, padx=4, pady=4)

        self.label_e1.grid(row=grid_rows[9], column=2, sticky="W", padx=4, pady=4)
        self.entry_e1.grid(row=grid_rows[9], column=3, padx=4, pady=4)
        
        self.label_y0.grid(row=grid_rows[10], column=0, sticky="W", padx=4, pady=4)
        self.entry_y0.grid(row=grid_rows[10], column=1, padx=4, pady=4)

        self.label_y1.grid(row=grid_rows[10], column=2, sticky="W", padx=4, pady=4)
        self.entry_y1.grid(row=grid_rows[10], column=3, padx=4, pady=4)

        self.button.grid(row=grid_rows[len(grid_rows)-1], column=0, padx=4, pady=4)

    def rotina_calcular(self):
        try:
            self.diametro = float(self.entry_d.get())
            self.rpm = float(self.entry_rpm.get())
            self.Fr = float(self.entry_Fr.get())
            self.Fa = float(self.entry_Fa.get())
            self.fh = float(self.entry_fh.get())
            self.fn = float(self.entry_fn.get())
            self.Cr = float(self.entry_Cr.get())
            self.C0r = float(self.entry_C0r.get())
            self.f0 = float(self.entry_f0.get())

            self.e = self.interpolacao_linear(
                                                float(self.entry_y0.get()), float(self.entry_y1.get()),
                                                self.carga_dinamica_equivalente_relacao(),
                                                float(self.entry_e0.get()), float(self.entry_e1.get())
                                            )
            

        except ValueError:
            messagebox.showerror("Error Input", "Erro em Algum Input\nVerificar Novamente")
            


#=====================================================
#   MAIN
#=====================================================
if __name__ == "__main__":
    gui = RolamentoGUI()

    gui.mainloop()