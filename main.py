import threading, time, os
from screen_capture import capture_screen
from ocr_engine import extract_text
from ai_classifier import Classificador
from report_manager import ReportManager

class Monitor:
    def __init__(self, model_path, intervalo=5):
        self.clas = Classificador(model_path); self.rm = ReportManager()
        self.intervalo, self.running = intervalo, True
        self.stats = {"analisadas":0, "ignoradas":0, "leves":0, "graves":0}

    def loop(self):
        while True:
            if self.running:
                os.makedirs("screenshots", exist_ok=True)
                fname = os.path.join("screenshots","tmp.png")
                capture_screen(fname)
                txt = extract_text(fname) or ""
                self.stats["analisadas"] += 1
                pred, conf = self.clas.classificar(txt)
                if pred == 'irrelevante': self.stats["ignoradas"] += 1
                elif pred == 'leve': self.stats["leves"] += 1
                elif pred == 'grave':
                    self.stats["graves"] += 1
                    self.rm.gerar_ticket(fname, txt, pred)
            time.sleep(self.intervalo)

monitor = Monitor("IA/moderador_model.pkl")
threading.Thread(target=monitor.loop, daemon=True).start()
