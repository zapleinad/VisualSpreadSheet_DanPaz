"""
visual_spreadsheets_completo_pt.py
-----------------------------------
Visual Spreadsheets para Eletrônica - Edição Completa em Português
com desenhos de circuitos, formas de onda e fórmulas exibidas
"""

import tkinter as tk
from tkinter import ttk, messagebox, Canvas
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math


class VisualSpreadsheetsCompleto:
    """Aplicação principal do Visual Spreadsheets completo em português."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Visual Spreadsheets para Eletrônica - Edição Completa")
        self.root.geometry("1400x900")
        self.root.configure(bg="black")

        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Criar barra de menu
        self.create_menu()
        
        # Frame principal
        self.workspace = tk.Frame(self.root, bg="black")
        self.workspace.pack(fill="both", expand=True)
        
        # Mostrar tela de boas-vindas
        self.show_welcome()

    def create_menu(self) -> None:
        """Cria a barra de menu completa em português."""
        menu_bar = tk.Menu(self.root, bg="#2b2b2b", fg="white")
        self.root.config(menu=menu_bar)

        # Menu Arquivo
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="#2b2b2b", fg="white")
        file_menu.add_command(label="Resetar", command=self.show_welcome)
        file_menu.add_command(label="Salvar Configuração", command=self.not_implemented)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Menu Circuitos
        circuits_menu = tk.Menu(menu_bar, tearoff=0, bg="#2b2b2b", fg="white")
        
        # Submenu AC/DC
        acdc_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        acdc_menu.add_command(label="Lei de Ohm", command=self.show_ohms_law)
        acdc_menu.add_command(label="Divisor de Tensão", command=self.show_voltage_divider)
        acdc_menu.add_command(label="Divisor de Corrente", command=self.show_current_divider)
        acdc_menu.add_command(label="Circuito RC", command=self.show_rc_circuit)
        acdc_menu.add_command(label="Circuito RLC", command=self.show_rlc_circuit)
        circuits_menu.add_cascade(label="AC/DC", menu=acdc_menu)
        
        # Submenu Amplificadores
        amp_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        amp_menu.add_command(label="Emissor Comum", command=self.show_common_emitter)
        amp_menu.add_command(label="Coletor Comum", command=self.show_common_collector)
        amp_menu.add_command(label="Op-Amp Inversor", command=self.show_opamp_inverting)
        amp_menu.add_command(label="Op-Amp Não-Inversor", command=self.show_opamp_noninverting)
        circuits_menu.add_cascade(label="Amplificadores", menu=amp_menu)
        
        # Submenu Osciladores
        osc_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        osc_menu.add_command(label="Timer 555 Astável", command=self.show_555_astable)
        osc_menu.add_command(label="Timer 555 Monoestável", command=self.show_555_monostable)
        osc_menu.add_command(label="Oscilador Wien Bridge", command=self.show_wien_bridge)
        circuits_menu.add_cascade(label="Osciladores", menu=osc_menu)
        
        # Submenu Fontes de Alimentação
        ps_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        ps_menu.add_command(label="Retificador Meia Onda", command=self.show_half_wave)
        ps_menu.add_command(label="Retificador Onda Completa", command=self.show_full_wave)
        ps_menu.add_command(label="Regulador de Tensão 7805", command=self.show_regulator_7805)
        circuits_menu.add_cascade(label="Fontes de Alimentação", menu=ps_menu)
        
        # Submenu Eletrônica de Potência
        pe_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        pe_menu.add_command(label="Conversor Buck (Abaixador)", command=self.show_buck_converter)
        pe_menu.add_command(label="Conversor Boost (Elevador)", command=self.show_boost_converter)
        pe_menu.add_command(label="Conversor Buck-Boost", command=self.show_buck_boost)
        pe_menu.add_command(label="Inversor Trifásico", command=self.show_three_phase_inverter)
        pe_menu.add_command(label="Análise PWM", command=self.show_pwm_analysis)
        circuits_menu.add_cascade(label="Eletrônica de Potência", menu=pe_menu)
        
        # Submenu Sistemas Elétricos
        es_menu = tk.Menu(circuits_menu, tearoff=0, bg="#2b2b2b", fg="white")
        es_menu.add_command(label="Resposta RL", command=self.show_rl_response)
        es_menu.add_command(label="Resposta RC", command=self.show_rc_response)
        es_menu.add_command(label="Transitório RLC", command=self.show_rlc_transient)
        es_menu.add_command(label="Sistema Trifásico", command=self.show_three_phase)
        es_menu.add_command(label="Correção Fator de Potência", command=self.show_power_factor)
        es_menu.add_command(label="Transformador", command=self.show_transformer)
        circuits_menu.add_cascade(label="Sistemas Elétricos", menu=es_menu)
        
        menu_bar.add_cascade(label="Circuitos", menu=circuits_menu)

        # Menu Resistores Padrão
        menu_bar.add_command(label="Resistores Padrão", command=self.show_standard_resistors)
        
        # Menu Tolerância
        menu_bar.add_command(label="Tolerância", command=self.show_tolerance)
        
        # Menu Ajuda
        help_menu = tk.Menu(menu_bar, tearoff=0, bg="#2b2b2b", fg="white")
        help_menu.add_command(label="Rótulos Vermelhos e Azuis", command=self.tutorial_labels)
        help_menu.add_command(label="Análise Rápida", command=self.tutorial_quick)
        help_menu.add_separator()
        help_menu.add_command(label="Sobre", command=self.show_about)
        menu_bar.add_cascade(label="Ajuda", menu=help_menu)

    def clear_workspace(self) -> None:
        """Limpa o workspace."""
        for widget in self.workspace.winfo_children():
            widget.destroy()

    def not_implemented(self) -> None:
        """Avisa que função não implementada."""
        messagebox.showinfo("Não Implementado", "Esta funcionalidade está em desenvolvimento.")

    def show_welcome(self) -> None:
        """Tela de boas-vindas."""
        self.clear_workspace()
        
        canvas = Canvas(self.workspace, bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Título
        canvas.create_text(
            700, 200,
            text="VISUAL SPREADSHEETS PARA ELETRÔNICA",
            fill="cyan",
            font=("Arial", 26, "bold")
        )
        
        canvas.create_text(
            700, 250,
            text="Edição Completa em Português",
            fill="white",
            font=("Arial", 18)
        )
        
        canvas.create_text(
            700, 320,
            text="Ferramenta Educacional para Análise de Circuitos",
            fill="lightgray",
            font=("Arial", 14)
        )
        
        canvas.create_text(
            700, 380,
            text="Selecione uma categoria de circuitos no menu para começar",
            fill="lightgray",
            font=("Arial", 13)
        )
        
        canvas.create_text(
            700, 480,
            text="Rótulos VERMELHOS = Valores de entrada (você insere)",
            fill="red",
            font=("Arial", 13, "bold")
        )
        
        canvas.create_text(
            700, 520,
            text="Rótulos AZUIS = Resultados calculados",
            fill="cyan",
            font=("Arial", 13, "bold")
        )
        
        canvas.create_text(
            700, 600,
            text="• Desenhos de Circuitos • Formas de Onda • Fórmulas Exibidas •",
            fill="yellow",
            font=("Arial", 12)
        )

    # ==================== FUNÇÕES UTILITÁRIAS ====================
    
    def create_input_field(self, parent, label_text, default_value, row):
        """Cria um campo de entrada padronizado."""
        tk.Label(
            parent, text=label_text, fg="red", bg="black", 
            font=("Arial", 11, "bold")
        ).grid(row=row, column=0, sticky="e", padx=5, pady=3)
        
        entry = tk.Entry(parent, width=12, font=("Arial", 11))
        entry.insert(0, str(default_value))
        entry.grid(row=row, column=1, padx=5, pady=3)
        
        return entry

    def create_output_label(self, parent, row):
        """Cria um label de saída padronizado."""
        label = tk.Label(
            parent, text="", fg="cyan", bg="black", 
            font=("Arial", 11, "bold"), anchor="w"
        )
        label.grid(row=row, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        return label

    def draw_resistor(self, canvas, x1, y1, x2, y2, vertical=False):
        """Desenha um resistor."""
        if vertical:
            # Resistor vertical
            mid = (y1 + y2) / 2
            height = abs(y2 - y1)
            width = height * 0.3
            canvas.create_rectangle(
                x1 - width/2, mid - height*0.3,
                x1 + width/2, mid + height*0.3,
                outline="white", width=2
            )
            canvas.create_line(x1, y1, x1, mid - height*0.3, fill="white", width=2)
            canvas.create_line(x1, mid + height*0.3, x1, y2, fill="white", width=2)
        else:
            # Resistor horizontal
            mid = (x1 + x2) / 2
            length = abs(x2 - x1)
            height = length * 0.15
            canvas.create_rectangle(
                mid - length*0.25, y1 - height,
                mid + length*0.25, y1 + height,
                outline="white", width=2
            )
            canvas.create_line(x1, y1, mid - length*0.25, y1, fill="white", width=2)
            canvas.create_line(mid + length*0.25, y1, x2, y1, fill="white", width=2)

    def draw_capacitor(self, canvas, x, y, vertical=False):
        """Desenha um capacitor."""
        if vertical:
            canvas.create_line(x-15, y, x+15, y, fill="white", width=3)
            canvas.create_line(x-15, y+5, x+15, y+5, fill="white", width=3)
        else:
            canvas.create_line(x, y-15, x, y+15, fill="white", width=3)
            canvas.create_line(x+5, y-15, x+5, y+15, fill="white", width=3)

    def draw_inductor(self, canvas, x1, y1, x2, y2):
        """Desenha um indutor (bobina)."""
        n_loops = 4
        dx = (x2 - x1) / (n_loops * 2)
        for i in range(n_loops):
            x_start = x1 + i * 2 * dx
            canvas.create_arc(
                x_start, y1 - 10,
                x_start + 2*dx, y1 + 10,
                start=180, extent=180,
                outline="white", width=2, style="arc"
            )

    def draw_diode(self, canvas, x, y, direction="right"):
        """Desenha um diodo."""
        if direction == "right":
            # Triângulo apontando para direita
            canvas.create_polygon(
                x-8, y-8, x-8, y+8, x+8, y,
                outline="white", fill="black", width=2
            )
            # Barra catodo
            canvas.create_line(x+8, y-8, x+8, y+8, fill="white", width=2)
        elif direction == "down":
            canvas.create_polygon(
                x-8, y-8, x+8, y-8, x, y+8,
                outline="white", fill="black", width=2
            )
            canvas.create_line(x-8, y+8, x+8, y+8, fill="white", width=2)

    def draw_ground(self, canvas, x, y):
        """Desenha símbolo terra."""
        canvas.create_line(x, y, x, y+10, fill="white", width=2)
        canvas.create_line(x-15, y+10, x+15, y+10, fill="white", width=3)
        canvas.create_line(x-10, y+15, x+10, y+15, fill="white", width=2)
        canvas.create_line(x-5, y+20, x+5, y+20, fill="white", width=1)

    def draw_voltage_source(self, canvas, x, y, label="V"):
        """Desenha fonte de tensão."""
        canvas.create_oval(x-20, y-20, x+20, y+20, outline="white", width=2)
        canvas.create_text(x, y-5, text="+", fill="white", font=("Arial", 14, "bold"))
        canvas.create_text(x, y+8, text="−", fill="white", font=("Arial", 14, "bold"))
        canvas.create_text(x+35, y, text=label, fill="red", font=("Arial", 11, "bold"))

    # ==================== LEI DE OHM ====================
    
    def show_ohms_law(self) -> None:
        """Lei de Ohm com circuito e fórmulas."""
        self.clear_workspace()
        
        # Título
        title = tk.Label(
            self.workspace, text="LEI DE OHM",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        # Frame principal
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack(pady=10)
        
        # Canvas para circuito (esquerda)
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=20)
        
        canvas = Canvas(canvas_frame, width=400, height=350, bg="black", 
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito
        # Fonte de tensão
        self.draw_voltage_source(canvas, 80, 150, "VCC")
        canvas.create_line(80, 130, 80, 80, fill="white", width=2)  # Fio superior
        canvas.create_line(80, 170, 80, 220, fill="white", width=2)  # Fio inferior
        
        # Fio superior horizontal
        canvas.create_line(80, 80, 320, 80, fill="white", width=2)
        
        # Resistor
        self.draw_resistor(canvas, 200, 80, 320, 80)
        canvas.create_text(260, 60, text="R", fill="red", font=("Arial", 14, "bold"))
        
        # Fio direito
        canvas.create_line(320, 80, 320, 220, fill="white", width=2)
        
        # Fio inferior
        canvas.create_line(80, 220, 320, 220, fill="white", width=2)
        
        # Terra
        self.draw_ground(canvas, 200, 220)
        
        # Seta de corrente
        canvas.create_line(340, 150, 360, 150, fill="yellow", width=2, arrow=tk.LAST)
        canvas.create_text(380, 150, text="I", fill="cyan", font=("Arial", 13, "bold"))
        
        # Frame de entrada/saída (meio)
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=20, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:", 
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        v_entry = self.create_input_field(io_frame, "Tensão V (V):", "12", 1)
        r_entry = self.create_input_field(io_frame, "Resistência R (Ω):", "1000", 2)
        
        tk.Label(io_frame, text="", bg="black").grid(row=3, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:", 
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=4, column=0, columnspan=2, pady=5)
        
        i_label = self.create_output_label(io_frame, 5)
        p_label = self.create_output_label(io_frame, 6)
        
        # Frame de fórmulas (direita)
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=20, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 13, "bold")
        ).pack(pady=5)
        
        formulas_text = """
I = V / R

P = V × I

P = V² / R

P = I² × R

Onde:
V = Tensão (Volts)
I = Corrente (Ampères)
R = Resistência (Ohms)
P = Potência (Watts)
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 10), justify="left"
        ).pack(padx=10, pady=5)
        
        def calculate():
            try:
                V = float(v_entry.get())
                R = float(r_entry.get())
                
                if R == 0:
                    messagebox.showerror("Erro", "Resistência não pode ser zero!")
                    return
                
                I = V / R
                P = V * I
                
                i_label.config(text=f"Corrente I = {I:.6f} A = {I*1000:.3f} mA")
                p_label.config(text=f"Potência P = {P:.6f} W = {P*1000:.3f} mW")
                
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")
        
        tk.Button(
            io_frame, text="CALCULAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 13, "bold"),
            padx=30, pady=8
        ).grid(row=7, column=0, columnspan=2, pady=20)

    # ==================== DIVISOR DE TENSÃO ====================
    
    def show_voltage_divider(self) -> None:
        """Divisor de tensão com circuito."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="DIVISOR DE TENSÃO",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack(pady=10)
        
        # Canvas para circuito
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=20)
        
        canvas = Canvas(canvas_frame, width=400, height=450, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito divisor de tensão
        # Fonte
        self.draw_voltage_source(canvas, 80, 180, "Vin")
        canvas.create_line(80, 160, 80, 80, fill="white", width=2)
        canvas.create_line(80, 200, 80, 280, fill="white", width=2)
        
        # Fio superior
        canvas.create_line(80, 80, 200, 80, fill="white", width=2)
        
        # R1
        self.draw_resistor(canvas, 200, 80, 200, 160, vertical=True)
        canvas.create_text(230, 120, text="R1", fill="red", font=("Arial", 13, "bold"))
        
        # Ponto médio
        canvas.create_line(200, 160, 200, 180, fill="white", width=2)
        canvas.create_oval(195, 175, 205, 185, fill="white", outline="white")
        canvas.create_line(200, 180, 300, 180, fill="white", width=2)
        canvas.create_text(340, 180, text="Vout", fill="cyan", font=("Arial", 13, "bold"))
        
        # R2
        self.draw_resistor(canvas, 200, 200, 200, 280, vertical=True)
        canvas.create_text(230, 240, text="R2", fill="red", font=("Arial", 13, "bold"))
        
        # Fio inferior e terra
        canvas.create_line(80, 280, 200, 280, fill="white", width=2)
        canvas.create_line(200, 280, 200, 300, fill="white", width=2)
        self.draw_ground(canvas, 200, 300)
        
        # Frame IO
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=20, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        vin_entry = self.create_input_field(io_frame, "Tensão Entrada Vin (V):", "12", 1)
        r1_entry = self.create_input_field(io_frame, "Resistor R1 (Ω):", "10000", 2)
        r2_entry = self.create_input_field(io_frame, "Resistor R2 (Ω):", "10000", 3)
        
        tk.Label(io_frame, text="", bg="black").grid(row=4, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=5, column=0, columnspan=2, pady=5)
        
        vout_label = self.create_output_label(io_frame, 6)
        ratio_label = self.create_output_label(io_frame, 7)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=20, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 13, "bold")
        ).pack(pady=5)
        
        formulas_text = """
        R2
Vout = ───── × Vin
       R1+R2


Razão = Vout/Vin


A tensão de saída é
uma fração da tensão
de entrada determinada
pela razão dos
resistores.
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 10), justify="left"
        ).pack(padx=10, pady=5)
        
        def calculate():
            try:
                Vin = float(vin_entry.get())
                R1 = float(r1_entry.get())
                R2 = float(r2_entry.get())
                
                Vout = Vin * R2 / (R1 + R2)
                ratio = Vout / Vin if Vin != 0 else 0
                
                vout_label.config(text=f"Vout = {Vout:.4f} V")
                ratio_label.config(text=f"Razão = {ratio:.4f} ({ratio*100:.2f}%)")
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
        
        tk.Button(
            io_frame, text="CALCULAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 13, "bold"),
            padx=30, pady=8
        ).grid(row=8, column=0, columnspan=2, pady=20)

    # ==================== CIRCUITO RC ====================
    
    def show_rc_circuit(self) -> None:
        """Circuito RC com resposta."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="CIRCUITO RC - CONSTANTE DE TEMPO",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack()
        
        # Canvas circuito
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=20)
        
        canvas = Canvas(canvas_frame, width=400, height=350, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito RC
        # Fonte
        self.draw_voltage_source(canvas, 80, 150, "V")
        canvas.create_line(80, 130, 80, 80, fill="white", width=2)
        canvas.create_line(80, 170, 80, 220, fill="white", width=2)
        
        # Resistor
        canvas.create_line(80, 80, 150, 80, fill="white", width=2)
        self.draw_resistor(canvas, 150, 80, 250, 80)
        canvas.create_text(200, 60, text="R", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(250, 80, 320, 80, fill="white", width=2)
        
        # Capacitor
        canvas.create_line(320, 80, 320, 140, fill="white", width=2)
        self.draw_capacitor(canvas, 320, 150, vertical=True)
        canvas.create_text(350, 150, text="C", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(320, 160, 320, 220, fill="white", width=2)
        
        # Terra
        canvas.create_line(80, 220, 320, 220, fill="white", width=2)
        self.draw_ground(canvas, 200, 220)
        
        # IO Frame
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=20, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        r_entry = self.create_input_field(io_frame, "Resistência R (Ω):", "10000", 1)
        c_entry = self.create_input_field(io_frame, "Capacitância C (F):", "0.0001", 2)
        
        tk.Label(io_frame, text="", bg="black").grid(row=3, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=4, column=0, columnspan=2, pady=5)
        
        tau_label = self.create_output_label(io_frame, 5)
        fc_label = self.create_output_label(io_frame, 6)
        t5tau_label = self.create_output_label(io_frame, 7)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=20, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 13, "bold")
        ).pack(pady=5)
        
        formulas_text = """
τ = R × C

      1
fc = ─────
     2πRC

Em t = τ:
  Vc = 63.2% × Vfinal

Em t = 5τ:
  Vc ≈ 99% × Vfinal
  (circuito estabilizado)

τ = Constante de tempo
fc = Frequência de corte
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 9), justify="left"
        ).pack(padx=10, pady=5)
        
        def calculate():
            try:
                R = float(r_entry.get())
                C = float(c_entry.get())
                
                tau = R * C
                fc = 1 / (2 * math.pi * R * C)
                t5tau = 5 * tau
                
                tau_label.config(text=f"Constante de Tempo τ = {tau:.6f} s = {tau*1000:.3f} ms")
                fc_label.config(text=f"Frequência de Corte fc = {fc:.3f} Hz")
                t5tau_label.config(text=f"Tempo de Estabilização (5τ) = {t5tau*1000:.3f} ms")
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
        
        tk.Button(
            io_frame, text="CALCULAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 13, "bold"),
            padx=30, pady=8
        ).grid(row=8, column=0, columnspan=2, pady=20)

    # ==================== TIMER 555 ASTÁVEL ====================
    
    def show_555_astable(self) -> None:
        """Timer 555 astável com forma de onda."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="TIMER 555 - MULTIVIBRADOR ASTÁVEL",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack()
        
        # Canvas circuito
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=10)
        
        canvas = Canvas(canvas_frame, width=450, height=400, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito 555
        # VCC no topo
        canvas.create_text(80, 30, text="VCC", fill="red", font=("Arial", 12, "bold"))
        canvas.create_line(80, 40, 80, 60, fill="white", width=2)
        
        # R1
        self.draw_resistor(canvas, 80, 60, 80, 120, vertical=True)
        canvas.create_text(110, 90, text="R1", fill="red", font=("Arial", 12, "bold"))
        
        # Ponto A
        canvas.create_oval(75, 115, 85, 125, fill="white", outline="white")
        canvas.create_line(80, 120, 200, 120, fill="white", width=2)
        
        # R2
        canvas.create_line(80, 120, 80, 140, fill="white", width=2)
        self.draw_resistor(canvas, 80, 140, 80, 200, vertical=True)
        canvas.create_text(110, 170, text="R2", fill="red", font=("Arial", 12, "bold"))
        
        # Ponto B e C
        canvas.create_oval(75, 195, 85, 205, fill="white", outline="white")
        canvas.create_line(80, 200, 200, 200, fill="white", width=2)
        canvas.create_line(80, 200, 80, 220, fill="white", width=2)
        
        # Capacitor
        self.draw_capacitor(canvas, 80, 230, vertical=True)
        canvas.create_text(110, 230, text="C", fill="red", font=("Arial", 12, "bold"))
        canvas.create_line(80, 240, 80, 280, fill="white", width=2)
        
        # Terra
        self.draw_ground(canvas, 80, 280)
        canvas.create_line(200, 280, 80, 280, fill="white", width=2)
        
        # CI 555
        canvas.create_rectangle(200, 100, 320, 300, outline="white", width=2, fill="#1a1a1a")
        canvas.create_text(260, 120, text="555", fill="cyan", font=("Arial", 16, "bold"))
        canvas.create_text(260, 140, text="TIMER", fill="white", font=("Arial", 10))
        
        # Pinos
        canvas.create_text(180, 120, text="7", fill="yellow", font=("Arial", 9))
        canvas.create_text(180, 160, text="6", fill="yellow", font=("Arial", 9))
        canvas.create_text(180, 200, text="2", fill="yellow", font=("Arial", 9))
        canvas.create_text(180, 240, text="1", fill="yellow", font=("Arial", 9))
        
        # Saída
        canvas.create_line(320, 180, 370, 180, fill="white", width=2)
        canvas.create_text(340, 165, text="3", fill="yellow", font=("Arial", 9))
        canvas.create_text(395, 180, text="vout", fill="cyan", font=("Arial", 12, "bold"))
        
        # Pino 1 (GND)
        canvas.create_line(200, 240, 180, 240, fill="white", width=2)
        canvas.create_line(180, 240, 180, 280, fill="white", width=2)
        
        # Pino 4 e 8 (VCC e Reset)
        canvas.create_line(260, 100, 260, 60, fill="white", width=2)
        canvas.create_line(260, 60, 80, 60, fill="white", width=2)
        
        # IO Frame
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=10, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        r1_entry = self.create_input_field(io_frame, "R1 (Ω):", "75000", 1)
        r2_entry = self.create_input_field(io_frame, "R2 (Ω):", "30000", 2)
        c_entry = self.create_input_field(io_frame, "C (F):", "0.000000047", 3)
        vcc_entry = self.create_input_field(io_frame, "VCC (V):", "12", 4)
        
        tk.Label(io_frame, text="", bg="black").grid(row=5, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=6, column=0, columnspan=2, pady=5)
        
        f_label = self.create_output_label(io_frame, 7)
        t_label = self.create_output_label(io_frame, 8)
        th_label = self.create_output_label(io_frame, 9)
        tl_label = self.create_output_label(io_frame, 10)
        duty_label = self.create_output_label(io_frame, 11)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=10, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 12, "bold")
        ).pack(pady=5)
        
        formulas_text = """
TH = 0.693×(R1+R2)×C

TL = 0.693×R2×C

T = TH + TL

f = 1/T

         TH
D = ─────── × 100%
     TH+TL


Vout: 0V a VCC
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 9), justify="left"
        ).pack(padx=5, pady=5)
        
        # Gráfico forma de onda
        graph_frame = tk.Frame(self.workspace, bg="black")
        graph_frame.pack(pady=10)
        
        fig = Figure(figsize=(10, 3), facecolor='black')
        ax = fig.add_subplot(111)
        ax.set_facecolor("black")
        ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_title("Forma de Onda de Saída", color="cyan", fontsize=13)
        ax.set_xlabel("Tempo (ms)", color="white", fontsize=11)
        ax.set_ylabel("Tensão (V)", color="white", fontsize=11)
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('gray')
        
        canvas_plot = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas_plot.get_tk_widget()
        canvas_widget.pack()
        
        def calculate():
            try:
                R1 = float(r1_entry.get())
                R2 = float(r2_entry.get())
                C = float(c_entry.get())
                VCC = float(vcc_entry.get())
                
                T_high = 0.693 * (R1 + R2) * C
                T_low = 0.693 * R2 * C
                T_total = T_high + T_low
                frequency = 1 / T_total
                duty_cycle = (T_high / T_total) * 100
                
                f_label.config(text=f"Frequência f = {frequency:.2f} Hz")
                t_label.config(text=f"Período T = {T_total*1000:.3f} ms")
                th_label.config(text=f"Tempo Alto TH = {T_high*1000:.3f} ms")
                tl_label.config(text=f"Tempo Baixo TL = {T_low*1000:.3f} ms")
                duty_label.config(text=f"Ciclo de Trabalho D = {duty_cycle:.1f}%")
                
                # Plotar forma de onda (3 ciclos)
                cycles = 3
                t = np.array([])
                v = np.array([])
                
                for cycle in range(cycles):
                    t_start = cycle * T_total
                    # Período HIGH
                    t = np.append(t, [t_start, t_start, t_start + T_high, t_start + T_high])
                    v = np.append(v, [0, VCC, VCC, 0])
                    # Período LOW
                    t = np.append(t, [t_start + T_high, t_start + T_total])
                    v = np.append(v, [0, 0])
                
                ax.cla()
                ax.set_facecolor("black")
                ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
                ax.plot(t * 1000, v, color="lime", linewidth=2.5)
                ax.fill_between(t * 1000, 0, v, alpha=0.3, color="lime")
                ax.axhline(VCC/2, color="yellow", linestyle=":", linewidth=1, alpha=0.5)
                ax.set_title("Forma de Onda de Saída (3 ciclos)", color="cyan", fontsize=13)
                ax.set_xlabel("Tempo (ms)", color="white", fontsize=11)
                ax.set_ylabel("Tensão (V)", color="white", fontsize=11)
                ax.set_ylim(-0.5, VCC + 0.5)
                ax.tick_params(colors='white')
                for spine in ax.spines.values():
                    spine.set_color('gray')
                canvas_plot.draw()
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
            except ZeroDivisionError:
                messagebox.showerror("Erro", "Período não pode ser zero!")
        
        tk.Button(
            io_frame, text="CALCULAR E PLOTAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 12, "bold"),
            padx=20, pady=8
        ).grid(row=12, column=0, columnspan=2, pady=15)

    # ==================== CONVERSOR BUCK ====================
    
    def show_buck_converter(self) -> None:
        """Conversor Buck com forma de onda."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="CONVERSOR BUCK (ABAIXADOR DC-DC)",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack()
        
        # Canvas circuito
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=10)
        
        canvas = Canvas(canvas_frame, width=500, height=350, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito Buck
        # Fonte Vin
        self.draw_voltage_source(canvas, 60, 150, "Vin")
        canvas.create_line(60, 130, 60, 80, fill="white", width=2)
        canvas.create_line(60, 170, 60, 220, fill="white", width=2)
        
        # Chave (MOSFET/Switch)
        canvas.create_line(60, 80, 140, 80, fill="white", width=2)
        canvas.create_rectangle(140, 60, 180, 100, outline="cyan", width=2, fill="#003333")
        canvas.create_text(160, 80, text="S", fill="white", font=("Arial", 14, "bold"))
        canvas.create_text(160, 45, text="PWM", fill="yellow", font=("Arial", 10, "bold"))
        
        # Diodo de roda livre
        canvas.create_line(180, 80, 200, 80, fill="white", width=2)
        canvas.create_oval(195, 75, 205, 85, fill="white", outline="white")
        canvas.create_line(200, 80, 200, 160, fill="white", width=2)
        self.draw_diode(canvas, 140, 160, direction="right")
        canvas.create_line(120, 160, 60, 160, fill="white", width=2)
        canvas.create_text(105, 145, text="D", fill="white", font=("Arial", 11))
        
        # Indutor
        canvas.create_line(200, 80, 220, 80, fill="white", width=2)
        self.draw_inductor(canvas, 220, 80, 300, 80)
        canvas.create_text(260, 60, text="L", fill="red", font=("Arial", 13, "bold"))
        
        # Capacitor de saída
        canvas.create_line(300, 80, 350, 80, fill="white", width=2)
        canvas.create_line(350, 80, 350, 130, fill="white", width=2)
        self.draw_capacitor(canvas, 350, 140, vertical=True)
        canvas.create_text(380, 140, text="C", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(350, 150, 350, 220, fill="white", width=2)
        
        # Carga R
        canvas.create_line(350, 80, 420, 80, fill="white", width=2)
        self.draw_resistor(canvas, 420, 80, 420, 160, vertical=True)
        canvas.create_text(450, 120, text="R", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(420, 160, 420, 220, fill="white", width=2)
        
        # Vout
        canvas.create_text(460, 80, text="Vout", fill="cyan", font=("Arial", 12, "bold"))
        
        # Terra
        canvas.create_line(60, 220, 420, 220, fill="white", width=2)
        self.draw_ground(canvas, 240, 220)
        
        # IO Frame
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=10, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        vin_entry = self.create_input_field(io_frame, "Tensão Entrada Vin (V):", "12", 1)
        d_entry = self.create_input_field(io_frame, "Ciclo de Trabalho D (0-1):", "0.5", 2)
        fsw_entry = self.create_input_field(io_frame, "Freq. Chaveamento f (Hz):", "50000", 3)
        l_entry = self.create_input_field(io_frame, "Indutância L (H):", "0.0001", 4)
        c_entry = self.create_input_field(io_frame, "Capacitância C (F):", "0.00001", 5)
        r_entry = self.create_input_field(io_frame, "Resistência Carga R (Ω):", "10", 6)
        
        tk.Label(io_frame, text="", bg="black").grid(row=7, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=8, column=0, columnspan=2, pady=5)
        
        vout_label = self.create_output_label(io_frame, 9)
        iout_label = self.create_output_label(io_frame, 10)
        delta_il_label = self.create_output_label(io_frame, 11)
        delta_vc_label = self.create_output_label(io_frame, 12)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=10, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 12, "bold")
        ).pack(pady=5)
        
        formulas_text = """
Vout = D × Vin

       Vout
Iout = ────
        R

        (Vin-Vout)×D
ΔIL = ─────────────
          L×f

         ΔIL
ΔVC ≈ ──────
       8×f×C

Para CCM:
  Iout > ΔIL/2
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 9), justify="left"
        ).pack(padx=5, pady=5)
        
        # Gráfico
        graph_frame = tk.Frame(self.workspace, bg="black")
        graph_frame.pack(pady=10)
        
        fig = Figure(figsize=(10, 3.5), facecolor='black')
        ax = fig.add_subplot(111)
        ax.set_facecolor("black")
        ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_title("Corrente no Indutor (Um Ciclo de Chaveamento)", color="cyan", fontsize=13)
        ax.set_xlabel("Tempo (μs)", color="white", fontsize=11)
        ax.set_ylabel("Corrente no Indutor (A)", color="white", fontsize=11)
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('gray')
        
        canvas_plot = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas_plot.get_tk_widget()
        canvas_widget.pack()
        
        def calculate():
            try:
                Vin = float(vin_entry.get())
                D = float(d_entry.get())
                f = float(fsw_entry.get())
                L = float(l_entry.get())
                C = float(c_entry.get())
                R = float(r_entry.get())
                
                if not (0 <= D <= 1):
                    messagebox.showerror("Erro", "Ciclo de trabalho deve estar entre 0 e 1!")
                    return
                
                Vout = D * Vin
                Iout = Vout / R
                delta_IL = (Vin - Vout) * D / (L * f)
                delta_VC = delta_IL / (8 * f * C)
                
                vout_label.config(text=f"Tensão Saída Vout = {Vout:.3f} V")
                iout_label.config(text=f"Corrente Saída Iout = {Iout:.3f} A")
                delta_il_label.config(text=f"Ondulação Indutor ΔIL = {delta_IL:.4f} A (pp)")
                delta_vc_label.config(text=f"Ondulação Capacitor ΔVC = {delta_VC*1000:.2f} mV (pp)")
                
                # Plotar corrente indutor
                T = 1 / f
                t_on = D * T
                
                t1 = np.linspace(0, t_on, 200)
                i1 = Iout - delta_IL/2 + (Vin - Vout) / L * t1
                
                t2 = np.linspace(t_on, T, 200)
                i2 = Iout + delta_IL/2 - Vout / L * (t2 - t_on)
                
                t = np.concatenate([t1, t2])
                i = np.concatenate([i1, i2])
                
                ax.cla()
                ax.set_facecolor("black")
                ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
                ax.plot(t * 1e6, i, color="magenta", linewidth=2.5)
                ax.fill_between(t * 1e6, 0, i, alpha=0.2, color="magenta")
                ax.axhline(Iout, color="cyan", linestyle="--", linewidth=1.5, label=f"Iavg = {Iout:.3f}A")
                ax.axhline(Iout + delta_IL/2, color="yellow", linestyle=":", linewidth=1, alpha=0.7)
                ax.axhline(Iout - delta_IL/2, color="yellow", linestyle=":", linewidth=1, alpha=0.7)
                ax.axvline(t_on * 1e6, color="red", linestyle="--", linewidth=1, alpha=0.5, label=f"D×T")
                ax.set_title("Corrente no Indutor (Um Ciclo de Chaveamento)", color="cyan", fontsize=13)
                ax.set_xlabel("Tempo (μs)", color="white", fontsize=11)
                ax.set_ylabel("Corrente no Indutor (A)", color="white", fontsize=11)
                ax.tick_params(colors='white')
                ax.legend(facecolor='black', edgecolor='gray', labelcolor='white', fontsize=9)
                for spine in ax.spines.values():
                    spine.set_color('gray')
                canvas_plot.draw()
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
            except ZeroDivisionError:
                messagebox.showerror("Erro", "Divisão por zero!")
        
        tk.Button(
            io_frame, text="CALCULAR E PLOTAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 12, "bold"),
            padx=15, pady=8
        ).grid(row=13, column=0, columnspan=2, pady=15)

    # ==================== RESPOSTA RL ====================
    
    def show_rl_response(self) -> None:
        """Resposta RL ao degrau com forma de onda."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="CIRCUITO RL - RESPOSTA AO DEGRAU",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack()
        
        # Canvas circuito
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=10)
        
        canvas = Canvas(canvas_frame, width=400, height=350, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito RL
        self.draw_voltage_source(canvas, 80, 150, "V")
        canvas.create_line(80, 130, 80, 80, fill="white", width=2)
        canvas.create_line(80, 170, 80, 220, fill="white", width=2)
        
        # Resistor
        canvas.create_line(80, 80, 150, 80, fill="white", width=2)
        self.draw_resistor(canvas, 150, 80, 250, 80)
        canvas.create_text(200, 60, text="R", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(250, 80, 320, 80, fill="white", width=2)
        
        # Indutor
        canvas.create_line(320, 80, 320, 100, fill="white", width=2)
        self.draw_inductor(canvas, 310, 110, 330, 190)
        canvas.create_text(350, 150, text="L", fill="red", font=("Arial", 13, "bold"))
        canvas.create_line(320, 190, 320, 220, fill="white", width=2)
        
        # Terra
        canvas.create_line(80, 220, 320, 220, fill="white", width=2)
        self.draw_ground(canvas, 200, 220)
        
        # IO
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=10, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        v_entry = self.create_input_field(io_frame, "Tensão Fonte V (V):", "10", 1)
        r_entry = self.create_input_field(io_frame, "Resistência R (Ω):", "100", 2)
        l_entry = self.create_input_field(io_frame, "Indutância L (H):", "0.5", 3)
        
        tk.Label(io_frame, text="", bg="black").grid(row=4, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 11, "bold")
        ).grid(row=5, column=0, columnspan=2, pady=5)
        
        tau_label = self.create_output_label(io_frame, 6)
        ifinal_label = self.create_output_label(io_frame, 7)
        t5tau_label = self.create_output_label(io_frame, 8)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=10, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 12, "bold")
        ).pack(pady=5)
        
        formulas_text = """
    L
τ = ─
    R

      V          -t/τ
i(t)= ─ × (1 - e    )
      R

I(∞) = V/R

Em t = τ:
  i = 63.2% × I(∞)

Em t = 5τ:
  i ≈ 99.3% × I(∞)
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 9), justify="left"
        ).pack(padx=5, pady=5)
        
        # Gráfico
        graph_frame = tk.Frame(self.workspace, bg="black")
        graph_frame.pack(pady=10)
        
        fig = Figure(figsize=(10, 3.5), facecolor='black')
        ax = fig.add_subplot(111)
        ax.set_facecolor("black")
        ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_title("Corrente vs Tempo", color="cyan", fontsize=13)
        ax.set_xlabel("Tempo (s)", color="white", fontsize=11)
        ax.set_ylabel("Corrente (A)", color="white", fontsize=11)
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('gray')
        
        canvas_plot = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas_plot.get_tk_widget()
        canvas_widget.pack()
        
        def calculate():
            try:
                V = float(v_entry.get())
                R = float(r_entry.get())
                L = float(l_entry.get())
                
                if R <= 0 or L <= 0:
                    messagebox.showerror("Erro", "R e L devem ser positivos!")
                    return
                
                tau = L / R
                I_final = V / R
                t5tau = 5 * tau
                
                tau_label.config(text=f"Constante de Tempo τ = {tau:.4f} s = {tau*1000:.2f} ms")
                ifinal_label.config(text=f"Corrente Final I(∞) = {I_final:.4f} A")
                t5tau_label.config(text=f"Tempo Estabilização (5τ) = {t5tau:.4f} s")
                
                # Plotar
                t_end = 5 * tau
                t = np.linspace(0, t_end, 500)
                i = I_final * (1 - np.exp(-t / tau))
                
                ax.cla()
                ax.set_facecolor("black")
                ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
                ax.plot(t, i, color="cyan", linewidth=2.5)
                ax.fill_between(t, 0, i, alpha=0.2, color="cyan")
                ax.axhline(I_final, color="yellow", linestyle="--", linewidth=1.5, 
                          label=f"I(∞) = {I_final:.3f}A")
                ax.axhline(I_final * 0.632, color="orange", linestyle=":", linewidth=1, 
                          label="63.2% de I(∞)")
                ax.axvline(tau, color="red", linestyle="--", linewidth=1.5, 
                          label=f"τ = {tau:.3f}s")
                ax.set_title("Corrente vs Tempo (Resposta ao Degrau)", color="cyan", fontsize=13)
                ax.set_xlabel("Tempo (s)", color="white", fontsize=11)
                ax.set_ylabel("Corrente (A)", color="white", fontsize=11)
                ax.tick_params(colors='white')
                ax.legend(facecolor='black', edgecolor='gray', labelcolor='white', fontsize=9)
                for spine in ax.spines.values():
                    spine.set_color('gray')
                canvas_plot.draw()
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
        
        tk.Button(
            io_frame, text="CALCULAR E PLOTAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 12, "bold"),
            padx=15, pady=8
        ).grid(row=9, column=0, columnspan=2, pady=15)

    # ==================== PWM ====================
    
    def show_pwm_analysis(self) -> None:
        """Análise de sinal PWM."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="ANÁLISE DE SINAL PWM",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack()
        
        # IO
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=0, padx=20, sticky="n")
        
        tk.Label(
            io_frame, text="ENTRADAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=5)
        
        vhigh_entry = self.create_input_field(io_frame, "Nível Alto Vhigh (V):", "5", 1)
        vlow_entry = self.create_input_field(io_frame, "Nível Baixo Vlow (V):", "0", 2)
        duty_entry = self.create_input_field(io_frame, "Ciclo Trabalho D (%):", "50", 3)
        freq_entry = self.create_input_field(io_frame, "Frequência f (Hz):", "1000", 4)
        
        tk.Label(io_frame, text="", bg="black").grid(row=5, column=0)
        
        tk.Label(
            io_frame, text="SAÍDAS:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=6, column=0, columnspan=2, pady=5)
        
        vavg_label = self.create_output_label(io_frame, 7)
        ton_label = self.create_output_label(io_frame, 8)
        toff_label = self.create_output_label(io_frame, 9)
        period_label = self.create_output_label(io_frame, 10)
        
        # Fórmulas
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=1, padx=20, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS",
            fg="yellow", bg="black", font=("Arial", 13, "bold")
        ).pack(pady=5)
        
        formulas_text = """
Vavg = D×Vhigh + (1-D)×Vlow

Ton = D × T

Toff = (1-D) × T

T = 1/f

D = Ciclo de trabalho
    (0 a 1 ou 0% a 100%)
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 10), justify="left"
        ).pack(padx=10, pady=5)
        
        # Gráfico
        graph_frame = tk.Frame(self.workspace, bg="black")
        graph_frame.pack(pady=10)
        
        fig = Figure(figsize=(11, 4), facecolor='black')
        ax = fig.add_subplot(111)
        ax.set_facecolor("black")
        ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_title("Forma de Onda PWM", color="cyan", fontsize=14)
        ax.set_xlabel("Tempo (ms)", color="white", fontsize=12)
        ax.set_ylabel("Tensão (V)", color="white", fontsize=12)
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('gray')
        
        canvas_plot = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas_plot.get_tk_widget()
        canvas_widget.pack()
        
        def calculate():
            try:
                Vhigh = float(vhigh_entry.get())
                Vlow = float(vlow_entry.get())
                D = float(duty_entry.get()) / 100
                f = float(freq_entry.get())
                
                if not (0 <= D <= 1):
                    messagebox.showerror("Erro", "Ciclo de trabalho deve estar entre 0 e 100%!")
                    return
                
                T = 1 / f
                Ton = D * T
                Toff = (1 - D) * T
                Vavg = D * Vhigh + (1 - D) * Vlow
                
                vavg_label.config(text=f"Tensão Média Vavg = {Vavg:.3f} V")
                ton_label.config(text=f"Tempo Ligado Ton = {Ton*1000:.3f} ms")
                toff_label.config(text=f"Tempo Desligado Toff = {Toff*1000:.3f} ms")
                period_label.config(text=f"Período T = {T*1000:.3f} ms")
                
                # Plotar PWM (3 ciclos)
                cycles = 3
                t = np.array([])
                v = np.array([])
                
                for cycle in range(cycles):
                    t_start = cycle * T
                    # Período alto
                    t = np.append(t, [t_start, t_start, t_start + Ton, t_start + Ton])
                    v = np.append(v, [Vlow, Vhigh, Vhigh, Vlow])
                    # Período baixo
                    if Toff > 0:
                        t = np.append(t, [t_start + Ton, t_start + T])
                        v = np.append(v, [Vlow, Vlow])
                
                ax.cla()
                ax.set_facecolor("black")
                ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
                ax.plot(t * 1000, v, color="lime", linewidth=3)
                ax.fill_between(t * 1000, Vlow, v, alpha=0.3, color="lime")
                ax.axhline(Vavg, color="yellow", linestyle="--", linewidth=2, 
                          label=f"Vavg = {Vavg:.2f}V")
                ax.axhline(Vhigh, color="red", linestyle=":", linewidth=1, alpha=0.5)
                ax.axhline(Vlow, color="blue", linestyle=":", linewidth=1, alpha=0.5)
                ax.set_title(f"Forma de Onda PWM (3 ciclos) - Duty Cycle = {D*100:.1f}%", 
                           color="cyan", fontsize=14)
                ax.set_xlabel("Tempo (ms)", color="white", fontsize=12)
                ax.set_ylabel("Tensão (V)", color="white", fontsize=12)
                ax.set_ylim(Vlow - 0.5, Vhigh + 0.5)
                ax.tick_params(colors='white')
                ax.legend(facecolor='black', edgecolor='gray', labelcolor='white', fontsize=10)
                for spine in ax.spines.values():
                    spine.set_color('gray')
                canvas_plot.draw()
                
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida!")
            except ZeroDivisionError:
                messagebox.showerror("Erro", "Frequência não pode ser zero!")
        
        tk.Button(
            io_frame, text="CALCULAR E PLOTAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 13, "bold"),
            padx=20, pady=8
        ).grid(row=11, column=0, columnspan=2, pady=20)

    # Implementar os demais circuitos seguindo o mesmo padrão...
    # (Vou adicionar versões simplificadas para os restantes)
    
    def show_current_divider(self): self.not_implemented()
    def show_rlc_circuit(self): self.not_implemented()
    def show_common_emitter(self) -> None:
        """Amplificador Emissor Comum com circuito e reta de carga."""
        self.clear_workspace()
        
        title = tk.Label(
            self.workspace, text="AMPLIFICADOR EMISSOR COMUM",
            fg="cyan", bg="black", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)
        
        main_frame = tk.Frame(self.workspace, bg="black")
        main_frame.pack(pady=10)
        
        # ========== CANVAS PARA CIRCUITO (ESQUERDA) ==========
        canvas_frame = tk.Frame(main_frame, bg="black")
        canvas_frame.grid(row=0, column=0, padx=15)
        
        canvas = Canvas(canvas_frame, width=450, height=500, bg="black",
                       highlightthickness=1, highlightbackground="gray")
        canvas.pack()
        
        # Desenhar circuito amplificador emissor comum
        # VCC no topo
        canvas.create_text(225, 25, text="VCC = 12V", fill="red", 
                          font=("Arial", 13, "bold"))
        canvas.create_line(225, 35, 225, 50, fill="white", width=2)
        
        # RC (resistor de coletor)
        self.draw_resistor(canvas, 225, 50, 225, 120, vertical=True)
        canvas.create_text(255, 85, text="RC", fill="red", font=("Arial", 12, "bold"))
        
        # Linha do coletor ao transistor
        canvas.create_line(225, 120, 225, 160, fill="white", width=2)
        
        # Ponto de saída (coletor)
        canvas.create_oval(220, 155, 230, 165, fill="white", outline="white")
        canvas.create_line(225, 160, 320, 160, fill="white", width=2)
        canvas.create_text(360, 160, text="Vout", fill="cyan", 
                          font=("Arial", 13, "bold"))
        
        # Capacitor de saída
        self.draw_capacitor(canvas, 340, 160, vertical=False)
        canvas.create_text(340, 140, text="Co", fill="white", font=("Arial", 10))
        
        # Transistor (símbolo simplificado)
        # Círculo do transistor
        canvas.create_oval(195, 160, 255, 220, outline="white", width=2)
        canvas.create_text(225, 190, text="Q1", fill="yellow", font=("Arial", 11, "bold"))
        
        # Terminal Coletor (C)
        canvas.create_line(225, 160, 225, 175, fill="white", width=2)
        canvas.create_text(210, 165, text="C", fill="lightblue", font=("Arial", 9))
        
        # Terminal Base (B)
        canvas.create_line(195, 190, 210, 190, fill="white", width=2)
        canvas.create_text(185, 190, text="B", fill="lightblue", font=("Arial", 9))
        
        # Terminal Emissor (E) com seta
        canvas.create_line(225, 205, 225, 220, fill="white", width=2)
        canvas.create_line(225, 220, 225, 240, fill="white", width=3)
        # Seta do emissor
        canvas.create_polygon(225, 235, 220, 225, 230, 225, 
                             fill="white", outline="white")
        canvas.create_text(210, 225, text="E", fill="lightblue", font=("Arial", 9))
        
        # Divisor de tensão da base (R1 e R2)
        # R1 (superior)
        canvas.create_line(100, 50, 100, 70, fill="white", width=2)
        self.draw_resistor(canvas, 100, 70, 100, 140, vertical=True)
        canvas.create_text(75, 105, text="R1", fill="red", font=("Arial", 12, "bold"))
        
        # Ponto da base
        canvas.create_line(100, 140, 100, 190, fill="white", width=2)
        canvas.create_oval(95, 185, 105, 195, fill="white", outline="white")
        canvas.create_line(100, 190, 150, 190, fill="white", width=2)
        
        # Capacitor de entrada
        self.draw_capacitor(canvas, 130, 190, vertical=False)
        canvas.create_text(130, 170, text="Ci", fill="white", font=("Arial", 10))
        canvas.create_line(150, 190, 195, 190, fill="white", width=2)
        
        # Entrada Vin
        canvas.create_line(100, 190, 50, 190, fill="white", width=2)
        canvas.create_text(25, 190, text="Vin", fill="red", font=("Arial", 12, "bold"))
        
        # R2 (inferior)
        canvas.create_line(100, 190, 100, 210, fill="white", width=2)
        self.draw_resistor(canvas, 100, 210, 100, 280, vertical=True)
        canvas.create_text(75, 245, text="R2", fill="red", font=("Arial", 12, "bold"))
        
        # RE (resistor de emissor)
        canvas.create_line(225, 240, 225, 260, fill="white", width=2)
        self.draw_resistor(canvas, 225, 260, 225, 330, vertical=True)
        canvas.create_text(255, 295, text="RE", fill="red", font=("Arial", 12, "bold"))
        
        # Capacitor de bypass do emissor
        canvas.create_line(225, 295, 280, 295, fill="white", width=2)
        self.draw_capacitor(canvas, 290, 295, vertical=True)
        canvas.create_text(320, 295, text="CE", fill="white", font=("Arial", 10))
        canvas.create_line(290, 305, 290, 350, fill="white", width=2)
        
        # Terra comum
        canvas.create_line(100, 280, 100, 350, fill="white", width=2)
        canvas.create_line(225, 330, 225, 350, fill="white", width=2)
        canvas.create_line(290, 350, 100, 350, fill="white", width=2)
        canvas.create_line(100, 50, 225, 50, fill="white", width=2)
        self.draw_ground(canvas, 190, 350)
        
        # ========== FRAME ENTRADAS/SAÍDAS (MEIO) ==========
        io_frame = tk.Frame(main_frame, bg="black")
        io_frame.grid(row=0, column=1, padx=15, sticky="n")
        
        tk.Label(
            io_frame, text="PARÂMETROS DE ENTRADA:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=8)
        
        vcc_entry = self.create_input_field(io_frame, "VCC (V):", "12", 1)
        rc_entry = self.create_input_field(io_frame, "RC - Coletor (Ω):", "2200", 2)
        re_entry = self.create_input_field(io_frame, "RE - Emissor (Ω):", "1000", 3)
        r1_entry = self.create_input_field(io_frame, "R1 - Base sup. (Ω):", "47000", 4)
        r2_entry = self.create_input_field(io_frame, "R2 - Base inf. (Ω):", "10000", 5)
        beta_entry = self.create_input_field(io_frame, "β (hFE):", "100", 6)
        vbe_entry = self.create_input_field(io_frame, "VBE (V):", "0.7", 7)
        
        tk.Label(io_frame, text="", bg="black").grid(row=8, column=0)
        
        tk.Label(
            io_frame, text="PONTO DE OPERAÇÃO DC:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=9, column=0, columnspan=2, pady=8)
        
        vb_label = self.create_output_label(io_frame, 10)
        ve_label = self.create_output_label(io_frame, 11)
        vc_label = self.create_output_label(io_frame, 12)
        vce_label = self.create_output_label(io_frame, 13)
        ib_label = self.create_output_label(io_frame, 14)
        ic_label = self.create_output_label(io_frame, 15)
        ie_label = self.create_output_label(io_frame, 16)
        
        tk.Label(io_frame, text="", bg="black").grid(row=17, column=0)
        
        tk.Label(
            io_frame, text="GANHOS AC:",
            fg="white", bg="black", font=("Arial", 12, "bold")
        ).grid(row=18, column=0, columnspan=2, pady=5)
        
        av_label = self.create_output_label(io_frame, 19)
        zi_label = self.create_output_label(io_frame, 20)
        
        # ========== FRAME FÓRMULAS (DIREITA SUPERIOR) ==========
        formula_frame = tk.Frame(main_frame, bg="black", bd=2, relief="groove")
        formula_frame.grid(row=0, column=2, padx=15, sticky="n")
        
        tk.Label(
            formula_frame, text="FÓRMULAS - ANÁLISE DC",
            fg="yellow", bg="black", font=("Arial", 13, "bold")
        ).pack(pady=8)
        
        formulas_text = """
POLARIZAÇÃO (Divisor de Tensão):

         R2
VB = ───────── × VCC
      R1 + R2

VE = VB - VBE

       VE
IE = ──────
       RE

IC ≈ IE

IB = IC / β

VC = VCC - IC×RC

VCE = VC - VE

GANHO DE TENSÃO (AC):

      RC
Av ≈ ────  (com CE)
      re

onde re ≈ 26mV / IE

Zi ≈ R1 || R2 || β×RE
        """
        
        tk.Label(
            formula_frame, text=formulas_text,
            fg="lightgray", bg="black", font=("Courier", 9), justify="left"
        ).pack(padx=8, pady=5)
        
        # ========== GRÁFICO RETA DE CARGA (ABAIXO) ==========
        graph_frame = tk.Frame(self.workspace, bg="black")
        graph_frame.pack(pady=15)
        
        fig = Figure(figsize=(11, 4), facecolor='black')
        ax = fig.add_subplot(111)
        ax.set_facecolor("black")
        ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_title("Reta de Carga DC e Ponto de Operação Q", 
                    color="cyan", fontsize=14, fontweight='bold')
        ax.set_xlabel("VCE (Volts)", color="white", fontsize=12)
        ax.set_ylabel("IC (mA)", color="white", fontsize=12)
        ax.tick_params(colors='white', labelsize=10)
        for spine in ax.spines.values():
            spine.set_color('gray')
        
        canvas_plot = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas_plot.get_tk_widget()
        canvas_widget.pack()
        
        def calculate():
            try:
                VCC = float(vcc_entry.get())
                RC = float(rc_entry.get())
                RE = float(re_entry.get())
                R1 = float(r1_entry.get())
                R2 = float(r2_entry.get())
                beta = float(beta_entry.get())
                VBE = float(vbe_entry.get())
                
                # Análise DC - Polarização por divisor de tensão
                # Tensão na base
                VB = (R2 / (R1 + R2)) * VCC
                
                # Tensão no emissor
                VE = VB - VBE
                
                # Corrente no emissor
                IE = VE / RE
                
                # Corrente no coletor (aproximadamente igual a IE)
                IC = IE
                
                # Corrente na base
                IB = IC / beta
                
                # Tensão no coletor
                VC = VCC - IC * RC
                
                # Tensão coletor-emissor
                VCE = VC - VE
                
                # Ganho de tensão AC (aproximado)
                re = 0.026 / IE  # Resistência intrínseca do emissor (26mV/IE)
                Av = -RC / re  # Negativo indica inversão de fase
                
                # Impedância de entrada
                Zi = (R1 * R2) / (R1 + R2)  # Aproximação simples
                
                # Atualizar labels
                vb_label.config(text=f"Tensão Base VB = {VB:.3f} V")
                ve_label.config(text=f"Tensão Emissor VE = {VE:.3f} V")
                vc_label.config(text=f"Tensão Coletor VC = {VC:.3f} V")
                vce_label.config(text=f"VCE = {VCE:.3f} V")
                ib_label.config(text=f"Corrente Base IB = {IB*1e6:.2f} μA")
                ic_label.config(text=f"Corrente Coletor IC = {IC*1000:.3f} mA")
                ie_label.config(text=f"Corrente Emissor IE = {IE*1000:.3f} mA")
                av_label.config(text=f"Ganho de Tensão Av ≈ {Av:.1f} (com CE)")
                zi_label.config(text=f"Impedância Entrada Zi ≈ {Zi:.0f} Ω = {Zi/1000:.1f} kΩ")
                
                # Plotar reta de carga DC
                # Reta de carga: IC = (VCC - VCE) / (RC + RE)
                # Dois pontos: (VCE=0, IC=VCC/(RC+RE)) e (VCE=VCC, IC=0)
                
                VCE_sat = 0  # Saturação
                IC_sat = VCC / (RC + RE)
                
                VCE_cutoff = VCC
                IC_cutoff = 0
                
                # Criar array para a reta de carga
                VCE_line = np.array([VCE_sat, VCE_cutoff])
                IC_line = np.array([IC_sat, IC_cutoff]) * 1000  # Converter para mA
                
                # Ponto Q (ponto de operação)
                VCE_Q = VCE
                IC_Q = IC * 1000  # mA
                
                # Verificar região de operação
                if VCE < 0.2:
                    region = "SATURAÇÃO"
                    region_color = "red"
                elif IC < 0.001:
                    region = "CORTE"
                    region_color = "blue"
                else:
                    region = "REGIÃO ATIVA"
                    region_color = "green"
                
                # Plotar
                ax.cla()
                ax.set_facecolor("black")
                ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)
                
                # Reta de carga
                ax.plot(VCE_line, IC_line, color="cyan", linewidth=2.5, 
                       label="Reta de Carga DC")
                
                # Ponto Q
                ax.plot(VCE_Q, IC_Q, 'o', color="yellow", markersize=12, 
                       markeredgecolor="white", markeredgewidth=2,
                       label=f"Ponto Q ({VCE_Q:.2f}V, {IC_Q:.2f}mA)")
                
                # Linhas de grade no ponto Q
                ax.axvline(VCE_Q, color="yellow", linestyle=":", linewidth=1, alpha=0.5)
                ax.axhline(IC_Q, color="yellow", linestyle=":", linewidth=1, alpha=0.5)
                
                # Regiões
                ax.axvspan(0, 0.2, alpha=0.1, color="red", label="Saturação")
                ax.axhspan(0, 0.1, alpha=0.1, color="blue", label="Corte")
                
                # Anotações
                ax.annotate(f'Q\n{region}', 
                           xy=(VCE_Q, IC_Q), 
                           xytext=(VCE_Q + 1, IC_Q + 0.5),
                           fontsize=10, color=region_color, fontweight='bold',
                           arrowprops=dict(arrowstyle='->', color=region_color, lw=1.5))
                
                ax.set_title("Reta de Carga DC e Ponto de Operação Q", 
                            color="cyan", fontsize=14, fontweight='bold')
                ax.set_xlabel("VCE (Volts)", color="white", fontsize=12)
                ax.set_ylabel("IC (mA)", color="white", fontsize=12)
                ax.set_xlim(-0.5, VCC + 1)
                ax.set_ylim(-0.5, IC_sat * 1000 + 1)
                ax.tick_params(colors='white', labelsize=10)
                ax.legend(facecolor='black', edgecolor='gray', labelcolor='white', 
                         fontsize=9, loc='upper right')
                
                for spine in ax.spines.values():
                    spine.set_color('gray')
                
                canvas_plot.draw()
                
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")
            except ZeroDivisionError:
                messagebox.showerror("Erro", "Divisão por zero! Verifique os valores.")
        
        tk.Button(
            io_frame, text="CALCULAR E PLOTAR", command=calculate,
            bg="#004400", fg="white", font=("Arial", 13, "bold"),
            padx=25, pady=10
        ).grid(row=21, column=0, columnspan=2, pady=20)
        
        # Informações adicionais
        info_frame = tk.Frame(self.workspace, bg="black", bd=1, relief="solid")
        info_frame.pack(pady=10, padx=20, fill="x")
        
        info_text = """
    AMPLIFICADOR EMISSOR COMUM - Características:
    • Ganho de tensão alto (invertido)  • Impedância de entrada moderada  • Impedância de saída moderada/alta
    • Com capacitor CE bypass, o ganho aumenta significativamente  • Sem CE, ganho = -RC/RE (menor, mais estável)
        """
        
        tk.Label(
            info_frame, text=info_text,
            fg="lightgray", bg="black", font=("Arial", 10), justify="left"
        ).pack(padx=10, pady=8)
    def show_common_collector(self): self.not_implemented()
    def show_opamp_inverting(self): self.not_implemented()
    def show_opamp_noninverting(self): self.not_implemented()
    def show_555_monostable(self): self.not_implemented()
    def show_wien_bridge(self): self.not_implemented()
    def show_half_wave(self): self.not_implemented()
    def show_full_wave(self): self.not_implemented()
    def show_regulator_7805(self): self.not_implemented()
    def show_boost_converter(self): self.not_implemented()
    def show_buck_boost(self): self.not_implemented()
    def show_three_phase_inverter(self): self.not_implemented()
    def show_rc_response(self): self.not_implemented()
    def show_rlc_transient(self): self.not_implemented()
    def show_three_phase(self): self.not_implemented()
    def show_power_factor(self): self.not_implemented()
    def show_transformer(self): self.not_implemented()
    
    def show_standard_resistors(self): self.not_implemented()
    def show_tolerance(self): self.not_implemented()
    
    def tutorial_labels(self):
        messagebox.showinfo(
            "Tutorial: Rótulos Vermelhos e Azuis",
            "Nesta aplicação:\n\n"
            "Rótulos VERMELHOS = Valores de entrada (você insere)\n"
            "Rótulos AZUIS/CIANO = Saídas calculadas\n\n"
            "Esta codificação por cores ajuda a distinguir\n"
            "entre entradas e resultados rapidamente."
        )
    
    def tutorial_quick(self):
        messagebox.showinfo(
            "Tutorial: Análise Rápida",
            "Para explorar rapidamente o comportamento do circuito:\n\n"
            "1. Altere os valores de entrada vermelhos\n"
            "2. Clique em CALCULAR ou CALCULAR E PLOTAR\n"
            "3. Observe como as saídas azuis mudam\n\n"
            "Isso permite realizar análises 'e-se' e\n"
            "estudos de sensibilidade rapidamente."
        )
    
    def show_about(self):
        messagebox.showinfo(
            "Sobre",
            "VISUAL SPREADSHEETS PARA ELETRÔNICA\n"
            "Edição Completa em Português\n\n"
            "Ferramenta educacional completa para análise de circuitos\n"
            "incluindo circuitos AC/DC, amplificadores, osciladores,\n"
            "eletrônica de potência e sistemas elétricos.\n\n"
            "Inspirado no trabalho do Dr. Albert Paul Malvino.\n\n"
            "Recursos:\n"
            "• Múltiplas categorias de circuitos\n"
            "• Cálculos em tempo real\n"
            "• Visualizações gráficas\n"
            "• Desenhos de circuitos\n"
            "• Formas de onda\n"
            "• Fórmulas exibidas\n"
            "• Tutoriais educacionais\n\n"
            "Versão 2.0 PT-BR - 2025"
        )


def main():
    root = tk.Tk()
    app = VisualSpreadsheetsCompleto(root)
    root.mainloop()


if __name__ == "__main__":
    main()