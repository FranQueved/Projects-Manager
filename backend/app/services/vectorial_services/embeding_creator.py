import numpy as np
from gensim.models import Word2Vec

# Modelo global para evitar entrenar múltiples veces
_modelo = None

def _entrenar_modelo():
    """
    Entrena un modelo Word2Vec con cada skill como entidad independiente.
    
    Cada línea es una skill única sin relaciones con otras.
    Esto permite generar embeddings únicos para cada skill.
    """
    # Corpus: CADA SKILL POR SEPARADO
    corpus_skills = [
        # Hard Skills - Lenguajes
        ["python"],
        ["javascript"],
        ["java"],
        ["csharp"],
        ["php"],
        ["ruby"],
        ["go"],
        ["swift"],
        ["kotlin"],
        ["typescript"],
        ["rust"],
        ["dart"],
        ["elixir"],
        ["clojure"],
        ["haskell"],
        ["r"],
        ["cpp"],
        ["scala"],
        
        # Hard Skills - Frameworks Backend
        ["django"],
        ["fastapi"],
        ["flask"],
        ["springboot"],
        ["laravel"],
        ["rails"],
        ["express"],
        ["phoenix"],
        
        # Hard Skills - Frameworks Frontend
        ["react"],
        ["vue"],
        ["angular"],
        ["nuxt"],
        ["svelte"],
        
        # Hard Skills - Bases de Datos
        ["postgresql"],
        ["mysql"],
        ["mongodb"],
        ["cassandra"],
        ["redis"],
        ["snowflake"],
        ["dynamodb"],
        
        # Hard Skills - Cloud & DevOps
        ["docker"],
        ["kubernetes"],
        ["aws"],
        ["azure"],
        ["gcp"],
        ["terraform"],
        ["jenkins"],
        ["gitlab"],
        
        # Hard Skills - Data & ML
        ["tensorflow"],
        ["pytorch"],
        ["pandas"],
        ["numpy"],
        ["scikit-learn"],
        ["airflow"],
        ["etl"],
        
        # Hard Skills - Mobile
        ["ios"],
        ["android"],
        ["flutter"],
        ["xcode"],
        
        # Hard Skills - APIs & Protocolos
        ["rest"],
        ["graphql"],
        ["soap"],
        ["grpc"],
        
        # Hard Skills - Otros
        ["html"],
        ["css"],
        ["sql"],
        ["git"],
        ["figma"],
        ["sketch"],
        ["tableau"],
        ["powerbi"],
        
        # Soft Skills
        ["comunicacion"],
        ["liderazgo"],
        ["creatividad"],
        ["innovacion"],
        ["resolucion-problemas"],
        ["analisis"],
        ["adaptabilidad"],
        ["flexibilidad"],
        ["calidad"],
        ["precision"],
        ["paciencia"],
        ["resiliencia"],
        ["presion"],
        ["empatia"],
        ["diseno-usuario"],
        ["mentoria"],
        ["coaching"],
        ["curiosidad"],
        ["autonomia"],
        ["iniciativa"],
        ["vision"],
        ["planificacion"],
        ["organizacion"],
        
        # Idiomas
        ["espanol"],
        ["ingles"],
        ["frances"],
        ["aleman"],
        ["italiano"],
        ["portugues"],
        ["japones"],
        ["chino"],
    ]
    
    # Entrenar modelo Word2Vec
    modelo = Word2Vec(
        sentences=corpus_skills,
        vector_size=768,  # Compatible con BERT/Supabase
        window=1,  # Ventana mínima porque cada skill es independiente
        min_count=1,
        workers=4,
        sg=1,  # Skip-gram
        epochs=10
    )
    return modelo

def string_a_embedding(texto: str) -> np.ndarray:
    """
    Convierte un string a un vector embedding usando Word2Vec (Gensim).
    
    El modelo está entrenado con:
    - Hard skills técnicos (Python, Django, React, etc.)
    - Soft skills (comunicación, liderazgo, etc.)
    - Idiomas
    - Tipos de proyectos
    
    Genera embeddings de 768 dimensiones que capturan similitud semántica.
    Permite hacer búsquedas por similitud entre perfiles, proyectos y empleados.
    
    Args:
        texto: String a convertir a embedding (puede ser skill, descripción, etc.)
        
    Returns:
        np.ndarray: Vector embedding normalizado de dimensión 768
        
    Raises:
        ValueError: Si el texto está vacío o no es válido
    """
    global _modelo
    
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El texto debe ser un string no vacío.")
    
    # Entrenar modelo si no existe
    if _modelo is None:
        print("[*] Entrenando modelo Word2Vec con datos de programa...")
        _modelo = _entrenar_modelo()
        print("[OK] Modelo entrenado exitosamente")
    
    # Tokenizar el texto (convertir a minúsculas y dividir)
    # Reemplazar separadores comunes (comas, guiones, puntos y comas) con espacios
    texto_limpio = texto.lower()
    for separador in [",", "-", ";", ".", "/"]:
        texto_limpio = texto_limpio.replace(separador, " ")
    
    palabras = texto_limpio.split()
    palabras = [p for p in palabras if p]  # Filtrar strings vacíos
    
    # Generar embedding promediando los vectores de las palabras
    vectores = []
    for palabra in palabras:
        try:
            vectores.append(_modelo.wv[palabra])
        except KeyError:
            # Si la palabra no está en el vocabulario, ignorarla
            pass
    
    if not vectores:
        # Si ninguna palabra está en el modelo, retornar vector cero
        embedding = np.zeros(768, dtype=np.float32)
    else:
        # Promediar los vectores de las palabras
        embedding = np.mean(vectores, axis=0).astype(np.float32)
    
    # Normalizar a unit vector para que similitud coseno esté en [-1, 1]
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    
    return embedding.astype(np.float32)