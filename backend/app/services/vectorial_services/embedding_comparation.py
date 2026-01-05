"""Embedding comparison service - Find similar employee profiles based on required profiles."""

from typing import List, Tuple, Optional
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
import numpy as np


class EmbeddingComparationService:
    """Service for comparing embeddings and finding similar profiles."""

    def __init__(self):
        self.db: Session = SessionLocal()

    def find_similar_profiles_for_required_profile(
        self, 
        required_profile_id: int, 
        top_k: int 
    ) -> List[int]:
        """
        Find the most similar employee profiles for a required profile using pgvector similarity.
        
        Args:
            required_profile_id: ID of the required profile to search for similar profiles
            top_k: Number of top similar profiles to return (default: 3)
            
        Returns:
            List of profile IDs that are most similar to the required profile
        """
        try:
            # Get the embedding vector for the required profile
            sql_get_required = text("""
                SELECT vector FROM embeddings 
                WHERE required_profile_id = :required_profile_id
            """)
            
            result = self.db.execute(
                sql_get_required, 
                {"required_profile_id": required_profile_id}
            ).first()
            
            if not result:
                print(f"No embedding found for required_profile_id: {required_profile_id}")
                return []
            
            # Find top K most similar employee profiles using cosine similarity
            sql_find_similar = text(f"""
                SELECT 
                    emb.profile_id,
                    1 - (emb.vector <#> (
                        SELECT vector FROM embeddings 
                        WHERE required_profile_id = :required_profile_id
                    )) as similarity_score
                FROM embeddings emb
                WHERE emb.profile_id IS NOT NULL
                ORDER BY similarity_score DESC
                LIMIT :top_k
            """)
            
            results = self.db.execute(
                sql_find_similar,
                {"required_profile_id": required_profile_id, "top_k": top_k}
            ).fetchall()
            
            # Extract profile IDs from results
            profile_ids = [row[0] for row in results]
            
            if profile_ids:
                print(f"Found {len(profile_ids)} similar profiles for required_profile_id {required_profile_id}")
                for i, (profile_id, score) in enumerate(results, 1):
                    print(f"  {i}. Profile ID: {profile_id}, Similarity: {score:.4f}")
            
            return profile_ids
            
        except Exception as e:
            print(f"Error finding similar profiles for required_profile_id {required_profile_id}: {e}")
            import traceback
            traceback.print_exc()
            return []



    def close(self):
        """Close database session."""
        self.db.close()


