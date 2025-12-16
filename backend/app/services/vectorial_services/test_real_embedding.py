# -*- coding: utf-8 -*-
"""Test de embeddings reales con SentenceTransformer"""

from embeding_creator import string_a_embedding
import numpy as np

print("="*80)
print("TEST DE EMBEDDINGS CON SENTENCETRANSFORMER")
print("="*80)

# Textos de prueba en español
textos = [
    "Python es un lenguaje de programación",
    "Aprendizaje automático es increíble",
    "Python y programación son fundamentales",
    "Inteligencia artificial cambia el mundo",
    "El aprendizaje de máquinas transforma empresas"
]

print("\nGenerando embeddings con SentenceTransformer...\n")

embeddings = []
for i, texto in enumerate(textos, 1):
    try:
        print(f"{i}. Procesando: '{texto}'")
        emb = string_a_embedding(texto)
        embeddings.append(emb)
        print(f"   ✅ Dimensión: {len(emb)}")
        print(f"   Norma: {np.linalg.norm(emb):.4f}")
        print()
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        exit(1)

print("="*80)
print("VALIDACIÓN DE EMBEDDINGS")
print("="*80)
print(f"Total de embeddings generados: {len(embeddings)}")
print(f"Dimensión esperada: 768")
print(f"Dimensión actual: {len(embeddings[0])}")
print(f"Tipo de dato: {embeddings[0].dtype}")
print()

print("="*80)
print("SIMILITUD COSENO ENTRE TEXTOS (normalizados)")
print("="*80)
print()

for i in range(len(embeddings)):
    for j in range(i+1, len(embeddings)):
        sim = np.dot(embeddings[i], embeddings[j])
        print(f"Similitud {i+1} vs {j+1}: {sim:.4f}")
        print(f"  '{textos[i]}'")
        print(f"  '{textos[j]}'")
        print()

print("="*80)
print("✅ TEST COMPLETADO EXITOSAMENTE")
print("="*80)
