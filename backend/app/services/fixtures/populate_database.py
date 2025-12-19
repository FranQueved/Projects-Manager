"""
Script ejecutable para rellenar completamente la base de datos con datos ficticios.

Este es el punto de entrada recomendado para poblar la BD con:
- 100 empleados
- 100 perfiles (1:1 con empleados)
- 30 proyectos
- 150+ asignaciones empleado-proyecto
- 100+ perfiles requeridos
- Embeddings vectoriales completos (perfiles, empleados, required_profiles)
"""

from app.services.fixtures.seed_service import seed_all


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SCRIPT DE RELLENADO DE BASE DE DATOS - FIXTURES")
    print("=" * 70)
    print("\nEste script ejecutará:")
    print("  [x] Creación de tablas de BD")
    print("  [x] Generación de 100 empleados con perfiles")
    print("  [x] Generación de 30 proyectos")
    print("  [x] Asignaciones aleatorias empleado-proyecto")
    print("  [x] Perfiles requeridos por proyecto (1-4 por proyecto)")
    print("  [x] Embeddings vectoriales de PERFILES")
    print("  [x] Embeddings vectoriales de EMPLEADOS")
    print("  [x] Embeddings vectoriales de PERFILES REQUERIDOS")
    print("\n" + "=" * 70 + "\n")

    # Ejecutar seeding con embeddings habilitados
    success = seed_all(include_embeddings=True)

    if success:
        print("\n[SUCCESS] OPERACIÓN COMPLETADA EXITOSAMENTE")
        print("   La base de datos está lista para usar")
        print("   [OK] Tablas creadas")
        print("   [OK] Datos ficticios poblados")
        print("   [OK] Todos los embeddings generados")
        exit(0)
    else:
        print("\n[ERROR] OPERACIÓN FALLIDA")
        print("   Revisa los errores anteriores")
        exit(1)
