"""Embedding generation using Sentence Transformers (all-MiniLM-L6-v2)."""

import numpy as np
from sentence_transformers import SentenceTransformer

_model = None


def _load_model():
    """Load Sentence Transformers pre-trained model (384-dimensional)."""
    print("[*] Loading Sentence Transformers model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("[OK] Model loaded (384 dimensions)")
    return model


def string_a_embedding(text: str) -> np.ndarray:
    """Convert text string to 384-dimensional normalized embedding vector.
    
    Args:
        text: Text to convert to embedding
        
    Returns:
        np.ndarray: 384-dimensional normalized float32 vector
        
    Raises:
        ValueError: If text is empty or invalid
    """
    global _model
    
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text must be non-empty string.")
    
    if _model is None:
        _model = _load_model()
    
    embedding = _model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
    return embedding.astype(np.float32)
