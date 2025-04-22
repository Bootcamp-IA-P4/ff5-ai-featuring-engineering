from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Datos de ejemplo: reseñas de productos
corpus = [
    "Me encanta este producto, es excelente",
    "No me gustó, no lo recomiendo",
    "Calidad aceptable por el precio",
    "Increíble, superó mis expectativas",
    "Defectuoso, no funcionó desde el primer día"
]

# 1. Bolsa de palabras (CountVectorizer)
count_vectorizer = CountVectorizer()
X_count = count_vectorizer.fit_transform(corpus)
df_count = pd.DataFrame(X_count.toarray(), columns=count_vectorizer.get_feature_names_out())

# 2. TF-IDF (TfidfVectorizer)
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Mostrar resultados
print("=== Bolsa de palabras ===")
print(df_count.head())
print("\n=== TF-IDF ===")
print(df_tfidf.head())

# Ejemplo de análisis de sentimiento simple (contar palabras positivas/negativas)
positive_words = ["encanta", "excelente", "increíble", "superó"]
negative_words = ["no", "defectuoso", "gustó"]

def count_sentiment(text, words):
    return sum(1 for word in words if word in text.lower())

df_text = pd.DataFrame(corpus, columns=["Reseña"])
df_text["Palabras_Positivas"] = df_text["Reseña"].apply(lambda x: count_sentiment(x, positive_words))
df_text["Palabras_Negativas"] = df_text["Reseña"].apply(lambda x: count_sentiment(x, negative_words))
df_text["Sentimiento"] = df_text["Palabras_Positivas"] - df_text["Palabras_Negativas"]

print("\n=== Análisis de Sentimiento ===")
print(df_text)