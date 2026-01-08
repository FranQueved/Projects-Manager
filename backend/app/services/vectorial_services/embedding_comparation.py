"""Embedding comparison service - Compare embeddings and find similarities."""

from typing import List
import numpy as np


def compare_embeddings(embedding1: List[float], embedding2: List[float]) -> float:
    """
    Calculate cosine similarity between two embeddings.
    
    Args:
        embedding1: First embedding vector (list of floats)
        embedding2: Second embedding vector (list of floats)
        
    Returns:
        Similarity score between 0.0 and 1.0
    """
    arr1 = np.array(embedding1)
    arr2 = np.array(embedding2)
    
    # Calculate cosine similarity
    dot_product = np.dot(arr1, arr2)
    norm1 = np.linalg.norm(arr1)
    norm2 = np.linalg.norm(arr2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    similarity = dot_product / (norm1 * norm2)
    # Normalize to 0-1 range (cosine similarity is -1 to 1)
    return max(0.0, min(1.0, (similarity + 1) / 2))
