from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib, os

X = [...]
y = [...]
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(X, y)
os.makedirs("IA", exist_ok=True)
joblib.dump(modelo, "IA/moderador_model.pkl")
print("Salvo em IA/moderador_model.pkl")
