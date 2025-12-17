from gensim.models import Word2Vec
import numpy as np

corpus = [
    "python django postgresql rest apis backend",
    "python fastapi sqlalchemy pydantic api",
    "javascript react nodejs mongodb frontend",
    "comunicacion equipo liderazgo colaboracion",
    "desarrollo software arquitectura microservicios",
]

sentences = [text.split() for text in corpus]
print("Corpus:", corpus)
print("\nFrases tokenizadas:", sentences)

modelo = Word2Vec(
    sentences=sentences,
    vector_size=768,
    window=5,
    min_count=1,
    workers=4,
    sg=1,
    epochs=10
)

print("\nVocabulario:", list(modelo.wv.index_to_key))
print(f"Tamaño del vocabulario: {len(modelo.wv)}")

# Test con palabras que existen
test_palabra = "python"
if test_palabra in modelo.wv:
    vec = modelo.wv[test_palabra]
    print(f"\nVector para '{test_palabra}' (primeros 10): {vec[:10]}")
    print(f"Norma del vector: {np.linalg.norm(vec)}")
else:
    print(f"'{test_palabra}' no está en el vocabulario")

# Test similitud
print("\n--- TEST DE SIMILITUD ---")
palabras1 = "python django postgresql".split()
palabras2 = "python fastapi sqlalchemy".split()

vecs1 = [modelo.wv[p] for p in palabras1 if p in modelo.wv]
vecs2 = [modelo.wv[p] for p in palabras2 if p in modelo.wv]

print(f"Palabras 1 encontradas: {palabras1}")
print(f"Palabras 2 encontradas: {palabras2}")

emb1 = np.mean(vecs1, axis=0) if vecs1 else np.zeros(768)
emb2 = np.mean(vecs2, axis=0) if vecs2 else np.zeros(768)

norm1 = np.linalg.norm(emb1)
norm2 = np.linalg.norm(emb2)

if norm1 > 0:
    emb1 = emb1 / norm1
if norm2 > 0:
    emb2 = emb2 / norm2

sim = np.dot(emb1, emb2)
print(f"Similitud: {sim:.4f}")
