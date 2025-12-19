"""Utilidad para reinicializar la tabla embeddings."""

from sqlalchemy import text
from app.db.database import engine


def drop_embeddings_table() -> None:
	"""Elimina la tabla embeddings y sus dependencias."""
	with engine.connect() as connection:
		connection.execute(text("DROP TABLE IF EXISTS embeddings CASCADE"))
		connection.commit()
	print("Tabla embeddings eliminada.")


if __name__ == "__main__":
	drop_embeddings_table()
