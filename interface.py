import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import webbrowser, os
from main import monitor

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Discord Monitor AI"); self.configure(bg="#e0e0e0"); self.geometry("800x600")
        self.create_tabs(); self.bind("<F8>", lambda e: self.toggle_monitor()); self.update_stats()

    def create_tabs(self):
        style = ttk.Style(self); style.theme_use("clam")
        nb = ttk.Notebook(self); nb.pack(expand=True, fill="both", padx=20, pady=20)
        # aba1
        tab1 = ttk.Frame(nb); nb.add(tab1, text="Canais Monitorados")
        ttk.Label(tab1,text="(Simulação de canais)").pack(pady=50)
        # aba2
        tab2 = ttk.Frame(nb); nb.add(tab2, text="Canal de Denúncia")
        ttk.Label(tab2,text="Canal denúncia (#nome)").pack(pady=10)
        self.denuncia = ttk.Entry(tab2); self.denuncia.pack()
        # aba3
        tab3 = ttk.Frame(nb); nb.add(tab3, text="Histórico de Tickets")
        self.history = scrolledtext.ScrolledText(tab3, state="disabled"); self.history.pack(expand=True,fill="both", padx=10,pady=10)
        ttk.Button(tab3,text="Abrir pasta de tickets",command=self.open_folder).pack(pady=10)
        # aba4
        tab4 = ttk.Frame(nb); nb.add(tab4, text="Estatísticas")
        self.stats_label = ttk.Label(tab4,text="",font=("Arial",14)); self.stats_label.pack(pady=20)
        # teste manual
        frame = ttk.Frame(self); frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(frame,text="Teste manual:").pack(side="left")
        self.test = ttk.Entry(frame, width=60); self.test.pack(side="left", padx=5)
        ttk.Button(frame,text="Analisar",command=self.manual_test).pack(side="left")

    def toggle_monitor(self):
        monitor.running = not monitor.running
        messagebox.showinfo("Monitoramento",f"Monitoramento {'Ativo' if monitor.running else 'Pausado'}")

    def update_stats(self):
        s = monitor.stats
        self.stats_label.config(text=(f"Analisadas:{s['analisadas']}\nIgnoradas:{s['ignoradas']}\nLeves:{s['leves']}\nGraves:{s['graves']}"))
        self.reload_history()
        self.after(1000, self.update_stats)

    def reload_history(self):
        folder = os.path.join(os.path.expanduser("~"),"Desktop","IA-Tickets")
        self.history.config(state="normal"); self.history.delete("1.0", tk.END)
        if os.path.isdir(folder):
            for f in sorted(os.listdir(folder)):
                if f.endswith(".txt"): self.history.insert(tk.END, f + "\n")
        self.history.config(state="disabled")

    def open_folder(self): 
        folder = os.path.join(os.path.expanduser("~"),"Desktop","IA-Tickets")
        os.makedirs(folder, exist_ok=True); webbrowser.open(folder)

    def manual_test(self):
        t = self.test.get(); pred, conf = monitor.clas.classificar(t)
        messagebox.showinfo("Manual",f"Classe: {pred}, Conf: {conf:.2f}")

if __name__=="__main__":
    GUI().mainloop()
