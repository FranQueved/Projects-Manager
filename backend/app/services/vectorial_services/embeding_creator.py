import numpy as np
from sentence_transformers import SentenceTransformer

# Modelo global para evitar cargar múltiples veces
_modelo = None

def _cargar_modelo():
    """
    Carga un modelo Sentence Transformers preentrenado.
    
    Usa 'all-MiniLM-L6-v2' que genera embeddings de 384 dimensiones,
    optimizado para búsquedas de similitud entre frases/textos.
    
    Este modelo entiende el contexto semántico mejor que Word2Vec,
    es rápido y eficiente, perfecto para usar con pgvector.
    """
    print("[*] Cargando modelo Sentence Transformers 'all-MiniLM-L6-v2'...")
    modelo = SentenceTransformer('all-MiniLM-L6-v2')
    print("[OK] Modelo cargado exitosamente (384 dimensiones, optimizado para pgvector)")
    return modelo

def string_a_embedding(texto: str) -> np.ndarray:
    """
    Convierte un string a un vector embedding usando Sentence Transformers.
    
    El modelo está optimizado para:
    - Búsquedas de similitud semántica entre perfiles
    - Comparación de skills y experiencias
    - Matching entre empleados y proyectos
    - Uso con pgvector en PostgreSQL
    
    Genera embeddings de 384 dimensiones que capturan similitud semántica profunda.
    Los vectores están normalizados para funcionar óptimamente con pgvector.
    
    Args:
        texto: String a convertir a embedding (perfil, descripción, skills, etc.)
        
    Returns:
        np.ndarray: Vector embedding normalizado de dimensión 384 (float32)
        
    Raises:
        ValueError: Si el texto está vacío o no es válido
    """
    global _modelo
    
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El texto debe ser un string no vacío.")
    
    # Cargar modelo si no existe
    if _modelo is None:
        _modelo = _cargar_modelo()
    
    # Generar embedding usando Sentence Transformers
    # normalize_embeddings=True normaliza el vector para similitud coseno
    embedding = _modelo.encode(texto, convert_to_numpy=True, normalize_embeddings=True)
    
    return embedding.astype(np.float32)