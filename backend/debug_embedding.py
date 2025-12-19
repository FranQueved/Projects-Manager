import sys
import os
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Agregar el directorio actual al path para poder importar app
sys.path.append(os.getcwd())

from app.db.database import DATABASE_URL

def test_embedding_insertion():
    print("="*60)
    print("DIAGNÓSTICO DE EMBEDDINGS Y PGVECTOR")
    print("="*60)
    
    try:
        # 1. Conectar a la base de datos
        print(f"[*] Conectando a: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else '...'}")
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()
        print("[OK] Conexión exitosa")
        
        # 2. Verificar extensión vector
        print("\n[*] Verificando extensión 'vector'...")
        try:
            result = db.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector'")).fetchone()
            if result:
                print(f"[OK] Extensión 'vector' encontrada (versión {result[2]})")
            else:
                print("[WARN] Extensión 'vector' NO encontrada. Intentando crearla...")
                db.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
                db.commit()
                print("[OK] Extensión creada")
        except Exception as e:
            print(f"[ERROR] Fallo al verificar/crear extensión vector: {e}")
            return

        # 3. Verificar tabla embeddings
        print("\n[*] Verificando tabla 'embeddings'...")
        try:
            # Insertar un vector de prueba (384 dimensiones)
            # Usamos un vector de ceros con un 1 al principio
            dummy_vector = [0.0] * 384
            dummy_vector[0] = 1.0
            
            vector_str = "[" + ",".join(str(x) for x in dummy_vector) + "]"
            
            print("[*] Intentando insertar vector de prueba...")
            sql = text("""
                INSERT INTO embeddings (vector) 
                VALUES (CAST(:vector_str AS vector))
                RETURNING id
            """)
            
            result = db.execute(sql, {"vector_str": vector_str})
            new_id = result.fetchone()[0]
            db.commit()
            
            print(f"[OK] Vector insertado correctamente con ID: {new_id}")
            
            # 4. Leer de vuelta
            print("[*] Leyendo vector de vuelta...")
            sql_read = text("SELECT vector FROM embeddings WHERE id = :id")
            row = db.execute(sql_read, {"id": new_id}).fetchone()
            
            if row:
                vec = row[0]
                print(f"[OK] Vector leído correctamente. Tipo: {type(vec)}")
                # print(f"     Primeros valores: {vec[:5] if hasattr(vec, '__getitem__') else vec}")
                
                # Limpiar
                print("[*] Limpiando datos de prueba...")
                db.execute(text("DELETE FROM embeddings WHERE id = :id"), {"id": new_id})
                db.commit()
                print("[OK] Limpieza completada")
            else:
                print("[ERROR] No se pudo leer el vector insertado")
                
        except Exception as e:
            print(f"[ERROR] Fallo en operación de tabla embeddings: {e}")
            import traceback
            traceback.print_exc()
            db.rollback()
            
    except Exception as e:
        print(f"[FATAL] Error general: {e}")
    finally:
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    test_embedding_insertion()
