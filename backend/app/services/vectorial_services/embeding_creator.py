
import numpy as np
from sentence_transformers import SentenceTransformer  # type: ignore

def string_a_embedding(texto: str) -> np.ndarray:
    """
    Convierte un string a un vector embedding usando SentenceTransformer.
    
    Args:
        texto: String a convertir a embedding
        
    Returns:
        np.ndarray: Vector embedding de dimensión 768
        
    Raises:
        ValueError: Si el texto está vacío o no es válido
    """
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El texto debe ser un string no vacío.")

    # Cargar el modelo de SentenceTransformer
    modelo = SentenceTransformer("jinaai/jina-embeddings-v2-base-es")
    
    # Generar embedding normalizado
    embedding = modelo.encode(texto, normalize_embeddings=True)
    
    return embedding.astype(np.float32)

if __name__ == "__main__":
    texto = "La inteligencia artificial está transformando el mundo."
    vector = string_a_embedding(texto)

    print("Texto:", texto)
    print("Dimensión del embedding:", len(vector))
    print("Primeros 10 valores:", vector[:10])