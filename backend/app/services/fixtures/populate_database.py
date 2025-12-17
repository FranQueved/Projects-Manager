"""
Script ejecutable para rellenar completamente la base de datos con datos ficticios.

Este es el punto de entrada recomendado para poblar la BD con:
- 100 empleados
- 100 perfiles (1:1 con empleados)
- 30 proyectos
- 150+ asignaciones empleado-proyecto
- 100 embeddings de perfiles
"""

from app.services.fixtures.seed_service import seed_all


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SCRIPT DE RELLENADO DE BASE DE DATOS - FIXTURES")
    print("=" * 70)
    print("\nEste script ejecutará:")
    print("  ✅ Creación de tablas de BD")
    print("  ✅ Generación de 100 empleados con perfiles")
    print("  ✅ Generación de 30 proyectos")
    print("  ✅ Asignaciones aleatorias empleado-proyecto")
    print("  ✅ Embeddings vectoriales de perfiles")
    print("\n" + "=" * 70 + "\n")

    success = seed_all(include_embeddings=True)

    if success:
        print("\n✅ OPERACIÓN COMPLETADA EXITOSAMENTE")
        print("   La base de datos está lista para usar")
        exit(0)
    else:
        print("\n❌ OPERACIÓN FALLIDA")
        print("   Revisa los errores anteriores")
        exit(1)
