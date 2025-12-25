backend
|-- app
|   |-- db
|   |   |-- __init__.py
|   |   |-- create_tables.py
|   |   `-- database.py
|   |-- models
|   |   |-- __init__.py
|   |   |-- embedding.py
|   |   |-- employee.py
|   |   |-- employee_project.py
|   |   |-- profile.py
|   |   |-- project.py
|   |   |-- required_profile.py
|   |   `-- SCHEMA.md
|   |-- routers
|   |   `-- __init__.py
|   |-- schemas
|   |   |-- employee.py
|   |   |-- profile.py
|   |   `-- project.py
|   |-- services
|   |   |-- creates
|   |   |   |-- __init__.py
|   |   |   |-- create_employee.py
|   |   |   |-- create_profile.py
|   |   |   `-- create_proyect.py
|   |   |-- fixtures
|   |   |   |-- __init__.py
|   |   |   |-- populate_database.py
|   |   |   |-- populate_embeddings.py
|   |   |   |-- seed_data.py
|   |   |   `-- seed_service.py
|   |   |-- service_layer
|   |   |   |-- employee_project_service.py
|   |   |   |-- employee_service.py
|   |   |   |-- profile_service.py
|   |   |   |-- project_service.py
|   |   |   `-- required_profile_service.py
|   |   |-- vectorial_services
|   |   |   |-- embedding_service.py
|   |   |   `-- embeding_creator.py
|   |   `-- __init__.py
|   |-- __init__.py
|   `-- main.py
|-- .env.example
|-- .gitignore
|-- ARCHITECTURE.md
|-- AUTOMATIC_EMBEDDINGS.md
|-- list_backend_structure.py
|-- README.md
`-- requirements.txt

## Detalles por modulo

### app/main.py
- Metodo read_root: responde con el mensaje base de la API.
- Metodo health_check: retorna estado sencillo para monitoreos.

### app/db/create_tables.py
- Clase InitDB.create_tables: inspecciona tablas existentes y crea las faltantes.
- Ejecucion InitDB.create_tables(): dispara la creacion al importar el modulo.

### app/db/database.py
- Funcion enable_pgvector: activa la extension vector al establecer conexion.

### app/models/embedding.py
- Metodo __repr__: devuelve representacion resumida del embedding.

### app/models/employee.py
- Metodo __repr__: expone identificador y oficina del empleado.
- Metodo __str__: retorna el nombre legible del empleado.

### app/models/employee_project.py
- Tabla employee_project: define columnas y columnas calculadas para la relacion muchos a muchos.

### app/models/profile.py
- Metodo __repr__: muestra identificador y un resumen de habilidades.

### app/models/project.py
- Metodo __repr__: resume proyecto con identificador y cliente.

### app/models/required_profile.py
- Metodo __repr__: muestra identificador, proyecto asociado y habilidades.

### app/schemas/employee.py
- Clase EmployeeBase: define campos comunes para empleados.
- Clase EmployeeCreate: agrega datos opcionales de perfil para altas.
- Clase EmployeeRead: expone identificadores al responder.
- Clase EmployeeUpdate: permite actualizaciones parciales.

### app/schemas/profile.py
- Clase ProfileBase: marca campos obligatorios de perfil.
- Clase ProfileCreate: reutiliza base para altas.
- Clase ProfileRead: incorpora identificador para respuestas.
- Clase ProfileUpdate: habilita actualizaciones parciales.

### app/schemas/project.py
- Clase ProjectBase: define campos base de proyectos.
- Clase ProjectCreate: reutiliza base para altas.
- Clase ProjectRead: agrega identificador para respuestas.
- Clase ProjectUpdate: permite modificar campos existentes.

### app/services/creates/create_employee.py
- Metodo EmployeeCreator.__init__: abre sesion de base de datos.
- Metodo create_one: valida perfil y crea empleado unico.
- Metodo create_many: repite validacion y crea lote de empleados.
- Metodo close: cierra la sesion.

### app/services/creates/create_profile.py
- Metodo ProfileCreator.__init__: inicializa sesion de base de datos.
- Metodo create_one: crea un perfil con commit y refresh.
- Metodo create_many: crea varios perfiles y devuelve la lista.
- Metodo close: cierra la sesion (existe duplicado y codigo muerto al final que intenta refrescar created_profiles).

### app/services/creates/create_proyect.py
- Metodo ProjectCreator.__init__: abre sesion de trabajo.
- Metodo create_one: valida datos via esquema y persiste un proyecto.
- Metodo create_many: crea varios proyectos en una transaccion.
- Metodo close: cierra la sesion activa.

### app/services/fixtures/populate_database.py
- Funcion principal seed_all: importa y ejecuta seed_all con opcion de embeddings cuando se corre como script.

### app/services/fixtures/populate_embeddings.py
- Funcion populate_embeddings: genera embeddings de empleados y muestra estadisticas.
- Bloque main: ejecuta populate_embeddings dos veces y finaliza con codigo de salida segun resultado.

### app/services/fixtures/seed_data.py
- Funcion generate_employees: arma 100 empleados con nombres y oficinas aleatorias.
- Funcion generate_random_assignments: crea pares empleado-proyecto unicos.
- Bloque main: imprime resumen de conteos cuando se ejecuta directamente.

### app/services/fixtures/seed_service.py
- Metodo SeedService.__init__: prepara servicios dependientes.
- Metodo seed_database: orquesta la carga de datos y devuelve estadisticas.
- Metodo _create_profiles: crea perfiles base y cuenta exitos.
- Metodo _create_employees_with_profiles: genera empleados usando perfiles embebidos.
- Metodo _create_employees: marcador obsoleto que retorna cero.
- Metodo _create_projects: inserta proyectos y reporta progreso.
- Metodo _create_assignments: vincula empleados con proyectos y contabiliza.
- Metodo _create_embeddings: placeholder sin logica (embeddings se crean durante altas).
- Metodo _create_required_profiles: asigna perfiles requeridos aleatorios a cada proyecto.
- Metodo _create_required_profile_embeddings: placeholder sin logica.
- Metodo validate_data: verifica conteos finales y muestra ejemplos.
- Metodo close: libera servicios internos.
- Funcion seed_all: crea tablas, ejecuta seeding y valida resultados.

### app/services/service_layer/employee_project_service.py
- Metodo __init__: abre sesion SQLAlchemy.
- Metodo assign_employee_to_project: vincula empleado con proyecto evitando duplicados.
- Metodo remove_employee_from_project: elimina una relacion especifica.
- Metodo get_employees_by_project: trae empleados asociados a un proyecto.
- Metodo get_projects_by_employee: trae proyectos asociados a un empleado.
- Metodo assign_multiple_employees_to_project: asigna lote y devuelve cuantas altas exitosas hubo.
- Metodo remove_all_employees_from_project: borra todas las relaciones de un proyecto.
- Metodo remove_employee_from_all_projects: borra todas las relaciones de un empleado.
- Metodo close: cierra la sesion.

### app/services/service_layer/employee_service.py
- Metodo __init__: abre sesion y crea servicio de embeddings.
- Metodo create_one: genera perfil si es necesario, crea empleado y produce embedding.
- Metodo create_many: repite proceso para una lista de empleados.
- Metodo get_by_id: busca empleado por identificador.
- Metodo get_all: retorna todos los empleados.
- Metodo get_by_office: filtra por oficina.
- Metodo get_by_name: hace busqueda parcial por nombre.
- Metodo get_with_profile: entrega empleado con perfil cargado.
- Metodo get_profile_of_employee: devuelve perfil asociado.
- Metodo update_by_id: valida cambios y actualiza empleado.
- Metodo delete_by_id: elimina empleado y confirma exito.
- Metodo close: cierra sesion y servicio de embeddings (definido dos veces, ultima elimina referencia a embedding).

### app/services/service_layer/profile_service.py
- Metodo __init__: inicializa sesion.
- Metodo create_one: crea un perfil nuevo.
- Metodo create_many: registra varios perfiles y refresca resultados.
- Metodo get_by_id: obtiene perfil por identificador.
- Metodo get_all: lista todos los perfiles ordenados.
- Metodo get_by_skill: filtra por habilidad tecnica.
- Metodo get_by_language: filtra por idioma listado.
- Metodo toString: compone cadena limpia para embeddings.
- Metodo update: aplica cambios parciales a un perfil.
- Metodo delete: elimina un perfil existente.
- Metodo close: cierra la sesion.

### app/services/service_layer/project_service.py
- Metodo __init__: abre sesion de base de datos.
- Metodo create_one: valida datos y crea proyecto.
- Metodo create_many: inserta lote de proyectos.
- Metodo get_by_id: busca proyecto por identificador.
- Metodo get_all: devuelve todos los proyectos.
- Metodo get_by_client: filtra por cliente.
- Metodo get_finished: lista proyectos finalizados.
- Metodo get_active: lista proyectos en curso.
- Metodo update_by_id: actualiza campos permitidos.
- Metodo delete_by_id: borra proyecto puntual.
- Metodo delete_many: elimina varios proyectos por lote.
- Metodo close: cierra la sesion.

### app/services/service_layer/required_profile_service.py
- Metodo __init__: abre sesion y prepara servicio de embeddings.
- Metodo add_required_profile: crea perfil requerido y genera embedding.
- Metodo remove_required_profile: borra un perfil requerido.
- Metodo get_required_profiles_for_project: lista perfiles requeridos de un proyecto.
- Metodo get_all: devuelve todos los perfiles requeridos.
- Metodo close: cierra sesion y servicio de embeddings.

### app/services/vectorial_services/embedding_service.py
- Metodo __init__: abre sesion y prepara servicios auxiliares.
- Metodo generate_embedding: envuelve llamada que produce vector en memoria.
- Metodo create_embedding_for_employee: genera y persiste vector de un empleado.
- Metodo create_embeddings_for_all_employees: recorre empleados y acumula exitos.
- Metodo create_embedding_for_required_profile: genera vector para perfil requerido.
- Metodo create_embeddings_for_required_profiles: procesa todos los perfiles requeridos activos.
- Metodo get_employee_embedding: recupera vector almacenado de un empleado.
- Metodo find_similar_employees: busca empleados parecidos usando similitud coseno.
- Metodo find_similar_employees_by_text: busca empleados parecidos contra texto libre.
- Metodo close: cierra sesion y servicios dependientes.

### app/services/vectorial_services/embeding_creator.py
- Metodo _load_model: carga modelo SentenceTransformer all-MiniLM-L6-v2.
- Metodo string_a_embedding: convierte texto en vector normalizado de 384 dimensiones.
