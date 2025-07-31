import joblib
class Classificador:
    def __init__(self, pkl_path): self.model = joblib.load(pkl_path)
    def classificar(self, texto):
        prob = self.model.predict_proba([texto])[0]
        classe = self.model.classes_[prob.argmax()]
        return ('incerto', prob.max()) if prob.max() < 0.7 else (classe, prob.max())
