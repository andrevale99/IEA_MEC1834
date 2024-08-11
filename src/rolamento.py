import tkinter as tk

class RolamentoGUI(tk.Tk):

    # Construtor padrao
    def __init__(self):
        super().__init__()

        self.diametro = 0 # (mm)
        self.rpm = 0

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

        self.title("Dimensionador de Rolamentos")

        self.geometry("640x480+100+100")

    def capacidade_de_carga_dimanica(self):
        self.C = self.fh / self.fn

    def carga_dinamica_equivalente(self):
        self.P = self.x * self.Fr + self.y * self.Fa
    
    def interpolacao_linear(self, y0, y1, x0, x1, x):
        return (y0 + (y1 - y0)*(x - x0)/(x1 - x0))

    # Cria as grades para organizacao
    # dos componentes da janela
    def create_grid(self):
        pass
    
    # Cria as labels de texto para mostrar
    # ao usuario os campos de inputs
    def create_labels(self):
        pass

    # Cria os inputs para o usuario
    def create_inputs(self):
        pass

    # Cria os botoes
    def create_buttons(self):
        pass
    
if __name__ == "__main__":
    gui = RolamentoGUI()

    # gui.mainloop()