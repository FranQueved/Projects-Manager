"""
Datos de prueba (fixtures) para la base de datos

Este archivo contiene datos JSON de prueba para:
- 100 empleados con sus perfiles (relación 1 a 1)
- 30 proyectos
- Asignaciones aleatorias entre empleados y proyectos
"""

from datetime import date, timedelta
import random

# ============================================
# DATOS DE PERFILES (100 perfiles)
# ============================================

PROFILES_DATA = [
    {
        "hard_skills": "Python, Django, PostgreSQL, REST APIs",
        "soft_skills": "Comunicación, Trabajo en equipo, Liderazgo",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "JavaScript, React, Node.js, MongoDB",
        "soft_skills": "Creatividad, Resolución de problemas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Java, Spring Boot, MySQL, Microservicios",
        "soft_skills": "Análisis, Planificación estratégica",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "C#, .NET, SQL Server, Azure",
        "soft_skills": "Adaptabilidad, Aprendizaje continuo",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "PHP, Laravel, MySQL, HTML/CSS",
        "soft_skills": "Atención al detalle, Paciencia",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Ruby, Rails, PostgreSQL, AWS",
        "soft_skills": "Innovación, Pensamiento crítico",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Go, Docker, Kubernetes, Linux",
        "soft_skills": "Resiliencia, Trabajo bajo presión",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Swift, iOS, Xcode, Core Data",
        "soft_skills": "Creatividad, Diseño UX/UI",
        "languages": "Español, Inglés, Catalán"
    },
    {
        "hard_skills": "Kotlin, Android, Firebase, MVVM",
        "soft_skills": "Empatía, Comunicación efectiva",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "TypeScript, Angular, RxJS, NgRx",
        "soft_skills": "Mentoría, Desarrollo de equipos",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Python, FastAPI, SQLAlchemy, Pydantic",
        "soft_skills": "Curiosidad, Aprendizaje autónomo",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "JavaScript, Vue.js, Nuxt.js, GraphQL",
        "soft_skills": "Flexibilidad, Adaptabilidad",
        "languages": "Español, Inglés, Japonés"
    },
    {
        "hard_skills": "C++, Qt, OpenGL, Linux",
        "soft_skills": "Precisión, Análisis técnico",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Scala, Play Framework, Akka, Cassandra",
        "soft_skills": "Visión estratégica, Planificación",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Rust, WebAssembly, Tokio, Async",
        "soft_skills": "Innovación, Experimentación",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Dart, Flutter, Firebase, Provider",
        "soft_skills": "Creatividad, Diseño centrado en usuario",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Elixir, Phoenix, PostgreSQL, OTP",
        "soft_skills": "Resiliencia, Pensamiento distribuido",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Clojure, Datomic, Ring, Compojure",
        "soft_skills": "Abstracción, Pensamiento funcional",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Haskell, Servant, PostgreSQL, Lens",
        "soft_skills": "Rigor matemático, Pureza funcional",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "R, Python, Pandas, TensorFlow",
        "soft_skills": "Análisis de datos, Interpretación",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Python, PyTorch, CUDA, Deep Learning",
        "soft_skills": "Experimentación, Validación",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "SQL, ETL, Airflow, Snowflake",
        "soft_skills": "Organización, Metodología",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Tableau, Power BI, DAX, Storytelling",
        "soft_skills": "Comunicación visual, Narrativa",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Figma, Sketch, Adobe XD, Prototyping",
        "soft_skills": "Diseño thinking, Empatía usuario",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Jenkins, GitLab CI, Docker, Kubernetes",
        "soft_skills": "Automatización, Mejora continua",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Terraform, AWS, Azure, GCP",
        "soft_skills": "Arquitectura cloud, Escalabilidad",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Linux, Bash, Python, Monitoring",
        "soft_skills": "Troubleshooting, Proactividad",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Scrum, Kanban, Agile, JIRA",
        "soft_skills": "Facilitación, Coaching",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "React Native, Expo, Redux, TypeScript",
        "soft_skills": "Movilidad, Experiencia móvil",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Unity, C#, AR/VR, Game Physics",
        "soft_skills": "Creatividad, Experiencia inmersiva",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Solidity, Web3, Ethereum, Smart Contracts",
        "soft_skills": "Descentralización, Seguridad blockchain",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "MATLAB, Simulink, Control Systems",
        "soft_skills": "Modelado matemático, Simulación",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "SAP ABAP, Fiori, HANA, BW",
        "soft_skills": "Procesos empresariales, ERP",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Salesforce, Apex, Lightning, SOQL",
        "soft_skills": "CRM, Automatización ventas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "MuleSoft, Anypoint, Integration, APIs",
        "soft_skills": "Conectividad, Arquitectura integración",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "PowerShell, Active Directory, Windows Server",
        "soft_skills": "Administración sistemas, Automatización",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Arduino, Raspberry Pi, IoT, Sensors",
        "soft_skills": "Prototipado, Hardware/Software",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Qt, QML, C++, Embedded Systems",
        "soft_skills": "Interfaces táctiles, UX embedded",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Ansible, Puppet, Chef, Infrastructure as Code",
        "soft_skills": "Automatización infraestructura, DevOps",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Prometheus, Grafana, ELK Stack, Monitoring",
        "soft_skills": "Observabilidad, Alerting",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Kafka, RabbitMQ, Event Streaming, Microservices",
        "soft_skills": "Arquitectura orientada a eventos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "OpenShift, Istio, Service Mesh, Microservices",
        "soft_skills": "Orquestación contenedores, Escalabilidad",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "React, Redux, TypeScript, Next.js",
        "soft_skills": "Desarrollo frontend moderno",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Vue.js, Nuxt.js, Pinia, Composition API",
        "soft_skills": "Reutilización componentes, DX",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Angular, RxJS, NgRx, Material Design",
        "soft_skills": "Arquitectura enterprise, Testing",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Svelte, SvelteKit, Stores, Transitions",
        "soft_skills": "Performance, Experiencia developer",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Express.js, NestJS, TypeORM, Swagger",
        "soft_skills": "APIs RESTful, Documentación",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Django REST, DRF, Celery, Redis",
        "soft_skills": "Backend robusto, Tareas asíncronas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Flask, SQLAlchemy, Marshmallow, JWT",
        "soft_skills": "Microframeworks, Flexibilidad",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Spring Boot, JPA, Hibernate, Security",
        "soft_skills": "Enterprise Java, Persistencia",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": ".NET Core, Entity Framework, Identity, SignalR",
        "soft_skills": "Plataforma Microsoft, Tiempo real",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Laravel, Livewire, Alpine.js, MySQL",
        "soft_skills": "Fullstack PHP, SPA sin JS complejo",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Symfony, Doctrine, Twig, API Platform",
        "soft_skills": "Arquitectura PHP enterprise",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Ruby on Rails, Hotwire, PostgreSQL, Sidekiq",
        "soft_skills": "Conventions over configuration",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Phoenix, Elixir, Ecto, LiveView",
        "soft_skills": "Concurrencia, Tiempo real",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Django, Wagtail CMS, PostgreSQL, Elasticsearch",
        "soft_skills": "CMS moderno, Búsqueda avanzada",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Strapi, Headless CMS, GraphQL, Admin Panel",
        "soft_skills": "Content management, API-first",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "WordPress, WooCommerce, PHP, MySQL",
        "soft_skills": "E-commerce, Plugins ecosystem",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Shopify, Liquid, JavaScript, Apps",
        "soft_skills": "E-commerce SaaS, Customización",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Magento, PHP, MySQL, Elasticsearch",
        "soft_skills": "E-commerce enterprise, Escalabilidad",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "PrestaShop, PHP, Smarty, Modules",
        "soft_skills": "E-commerce open source",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Odoo, Python, PostgreSQL, XML",
        "soft_skills": "ERP open source, Modularidad",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "SuiteCRM, PHP, MySQL, SugarCRM",
        "soft_skills": "CRM open source, Personalización",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Moodle, PHP, MySQL, SCORM",
        "soft_skills": "E-learning, LMS",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Canvas LMS, Ruby, PostgreSQL, LTI",
        "soft_skills": "E-learning enterprise",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Google Cloud, Firebase, BigQuery, ML Engine",
        "soft_skills": "Cloud computing, Machine Learning",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "AWS Lambda, S3, DynamoDB, CloudFormation",
        "soft_skills": "Serverless, Infraestructura como código",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Azure Functions, Blob Storage, Cosmos DB, ARM",
        "soft_skills": "Cloud Microsoft, Enterprise",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Docker, Kubernetes, Helm, Istio",
        "soft_skills": "Contenedorización, Orquestación",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Terraform, Ansible, Packer, Vault",
        "soft_skills": "Infrastructure as Code, DevOps",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Jenkins, GitLab CI, GitHub Actions, ArgoCD",
        "soft_skills": "CI/CD, Automatización despliegues",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "PostgreSQL, MongoDB, Redis, Elasticsearch",
        "soft_skills": "Bases de datos, Búsqueda, Cache",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "MySQL, MariaDB, Percona, Galera",
        "soft_skills": "Bases de datos relacionales, Alta disponibilidad",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Oracle, SQL Server, DB2, PL/SQL",
        "soft_skills": "Bases de datos enterprise",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "SQLite, LevelDB, RocksDB, Time Series",
        "soft_skills": "Bases de datos embebidas, Series temporales",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Prometheus, Grafana, Loki, Tempo",
        "soft_skills": "Observabilidad, Métricas, Logs, Trazas",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "ELK Stack, Fluentd, Kafka, ClickHouse",
        "soft_skills": "Big Data, Análisis de logs",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Apache Spark, Hadoop, Hive, Presto",
        "soft_skills": "Big Data processing, Data lakes",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Airflow, Prefect, Dagster, DBT",
        "soft_skills": "Data pipelines, Orchestration",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Pandas, NumPy, Scikit-learn, Jupyter",
        "soft_skills": "Data Science, Machine Learning",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "TensorFlow, PyTorch, Keras, OpenCV",
        "soft_skills": "Deep Learning, Computer Vision",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "NLP, spaCy, Transformers, BERT",
        "soft_skills": "Procesamiento de lenguaje natural",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Tableau, Power BI, Looker, Metabase",
        "soft_skills": "Business Intelligence, Visualización",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Figma, Adobe XD, Sketch, InVision",
        "soft_skills": "UI/UX Design, Prototipado",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "Photoshop, Illustrator, After Effects, Premiere",
        "soft_skills": "Diseño gráfico, Motion graphics",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Blender, Maya, 3ds Max, ZBrush",
        "soft_skills": "Modelado 3D, Animación",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Unity, Unreal Engine, Godot, Game Design",
        "soft_skills": "Desarrollo de videojuegos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Arduino, Raspberry Pi, ESP32, IoT",
        "soft_skills": "Prototipado hardware, Electrónica",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "MATLAB, Simulink, LabVIEW, Control Systems",
        "soft_skills": "Sistemas de control, Automatización industrial",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "SolidWorks, AutoCAD, CATIA, Mechanical Design",
        "soft_skills": "Diseño mecánico, CAD",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "ANSYS, COMSOL, CFD, FEA",
        "soft_skills": "Simulación ingenieril, Análisis numérico",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "PLC Programming, SCADA, Industrial Networks",
        "soft_skills": "Automatización industrial, Control de procesos",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Embedded C, RTOS, ARM, Microcontrollers",
        "soft_skills": "Sistemas embebidos, Programación de bajo nivel",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "VHDL, Verilog, FPGA, ASIC Design",
        "soft_skills": "Diseño digital, Lógica programable",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "ROS, Gazebo, Navigation, Computer Vision",
        "soft_skills": "Robótica, Sistemas autónomos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Blockchain, Solidity, Web3.js, DeFi",
        "soft_skills": "Tecnología descentralizada, Criptoeconomía",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Quantum Computing, Qiskit, Cirq, Q#",
        "soft_skills": "Computación cuántica, Algoritmos cuánticos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Bioinformatics, R, Python, Genomics",
        "soft_skills": "Análisis biológico, Secuenciación",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "GIS, ArcGIS, QGIS, GeoServer",
        "soft_skills": "Sistemas de información geográfica",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Cybersecurity, Ethical Hacking, SIEM, SOC",
        "soft_skills": "Seguridad informática, Análisis de amenazas",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Cryptography, PKI, SSL/TLS, Zero Trust",
        "soft_skills": "Criptografía, Seguridad de comunicaciones",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Penetration Testing, OWASP, Burp Suite, Metasploit",
        "soft_skills": "Testing de seguridad, Ethical hacking",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hard_skills": "Compliance, GDPR, ISO 27001, Risk Assessment",
        "soft_skills": "Cumplimiento normativo, Gestión de riesgos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Digital Forensics, Memory Analysis, Malware Analysis",
        "soft_skills": "Investigación digital, Análisis forense",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hard_skills": "Agile, Scrum, Kanban, XP, Lean",
        "soft_skills": "Metodologías ágiles, Gestión de proyectos",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Product Management, Roadmap, User Stories, A/B Testing",
        "soft_skills": "Gestión de producto, Validación de hipótesis",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hard_skills": "UX Research, User Testing, Usability, Accessibility",
        "soft_skills": "Investigación de usuario, Diseño centrado en humano",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Growth Hacking, Analytics, SEO, SEM",
        "soft_skills": "Crecimiento de producto, Marketing digital",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hard_skills": "Technical Writing, Documentation, API Docs, MkDocs",
        "soft_skills": "Comunicación técnica, Documentación",
        "languages": "Español, Inglés"
    },
    {
        "hard_skills": "Teaching, Mentoring, Curriculum Design, Online Learning",
        "soft_skills": "Educación, Desarrollo profesional",
        "languages": "Español, Inglés, Portugués"
    }
]

# ============================================
# NOMBRES Y APELLIDOS PARA EMPLEADOS
# ============================================

FIRST_NAMES = [
    "Ana", "Carlos", "María", "José", "Isabel", "Antonio", "Carmen", "Francisco",
    "Pilar", "Juan", "Teresa", "David", "Cristina", "Alejandro", "Mónica",
    "Miguel", "Ángela", "Rafael", "Dolores", "Javier", "Lucía", "Fernando",
    "Mercedes", "Pablo", "Manuela", "Sergio", "Elena", "Diego", "Patricia",
    "Raúl", "Rosa", "Alberto", "Concepción", "Adrián", "Piedad", "Rubén",
    "Virginia", "Iván", "Carolina", "Óscar", "Silvia", "Hugo", "Lorena",
    "Víctor", "Teresa", "Mario", "Inés", "Roberto", "Eva", "Jaime", "Natalia",
    "Enrique", "Rocío", "Álvaro", "Amparo", "Ramón", "Milagros", "Santiago",
    "Montserrat", "Joaquín", "Nuria", "Vicente", "Lourdes", "Salvador",
    "Consuelo", "Guillermo", "Asunción", "Julio", "Trinidad", "Agustín",
    "Encarnación", "Emilio", "Visitación", "Felipe", "Candelaria", "Sebastián",
    "Milagrosa", "Ernesto", "Apolonia", "Gonzalo", "Remedios", "Félix",
    "Purificación", "Arturo", "Dolores", "Héctor", "Gracia", "Martín",
    "Esperanza", "Rodolfo", "Fe", "Tomás", "Caridad", "Eugenio", "Misericordia",
    "Leopoldo", "Luz", "Baldomero", "Aurora", "César", "Gloria", "Evaristo",
    "Juana", "Fidel", "Inmaculada", "Gerardo", "Soledad", "Horacio", "Clemencia"
]

LAST_NAMES = [
    "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez",
    "Pérez", "Martín", "Ruiz", "Hernández", "Jiménez", "Díaz", "Moreno", "Álvarez",
    "Muñoz", "Romero", "Navarro", "Torres", "Gil", "Ramírez", "Serrano", "Blanco",
    "Suárez", "Molina", "Morales", "Ortega", "Delgado", "Castro", "Rubio", "Ortiz",
    "Marín", "Sanz", "Núñez", "Iglesias", "Cortés", "Garrido", "Santos", "Guerrero",
    "Cano", "Prieto", "Méndez", "Calvo", "Domínguez", "Herrera", "Vega", "Flores",
    "Cabrera", "Campos", "Vargas", "Reyes", "Arias", "Medina", "Fuentes", "Carmona",
    "Benítez", "Rojas", "Aguilar", "Santiago", "Nieto", "Herrero", "Lorenzo",
    "Montero", "Hidalgo", "Giménez", "Ibáñez", "Ferrer", "Duran", "Santiago",
    "Vicente", "Benito", "Moreno", "Albert", "Riera", "Domingo", "Esteban",
    "Parra", "Bravo", "Gallardo", "Rivas", "Mateo", "Pascual", "Soler", "Velasco",
    "Moya", "Soto", "Silva", "Mora", "Guillen", "Pardo", "Vidal", "León", "Márquez"
]

OFFICES = [
    "Desarrollador Frontend", "Desarrollador Backend", "Full Stack Developer",
    "DevOps Engineer", "Data Scientist", "UX/UI Designer", "Product Manager",
    "QA Engineer", "Scrum Master", "Tech Lead", "Arquitecto de Software",
    "Analista de Sistemas", "Ingeniero de Datos", "Especialista en Ciberseguridad",
    "Administrador de Sistemas", "Consultor Técnico", "Desarrollador Móvil",
    "Ingeniero de Machine Learning", "Diseñador Gráfico", "Marketing Digital",
    "Analista de Negocio", "Project Manager", "Soporte Técnico", "DBA",
    "Cloud Architect", "DevSecOps", "Technical Writer", "Agile Coach",
    "Research Engineer", "Solutions Architect", "Platform Engineer",
    "Site Reliability Engineer", "Data Engineer", "Business Analyst",
    "System Analyst", "Software Engineer", "Web Developer", "Mobile Developer",
    "Game Developer", "Embedded Systems Engineer", "IoT Developer",
    "Blockchain Developer", "AI/ML Engineer", "Computer Vision Engineer",
    "NLP Engineer", "Robotics Engineer", "Quantum Computing Researcher",
    "Bioinformatics Specialist", "Geospatial Analyst", "Cybersecurity Analyst",
    "Penetration Tester", "Compliance Officer", "Digital Forensics Expert",
    "Product Owner", "UX Researcher", "Growth Hacker", "Technical Trainer"
]

# ============================================
# GENERACIÓN DE EMPLEADOS (100 empleados)
# ============================================

def generate_employees():
    """Genera 100 empleados con nombres aleatorios y perfiles asignados"""
    employees = []

    for i in range(100):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        full_name = f"{first_name} {last_name}"

        employee = {
            "name": full_name,
            "office": random.choice(OFFICES)
        }
        employees.append(employee)

    return employees

EMPLOYEES_DATA = generate_employees()

# ============================================
# DATOS DE PROYECTOS (30 proyectos)
# ============================================

PROJECTS_DATA = [
    {
        "name": "Sistema de Gestión de Inventarios",
        "description": "Plataforma web para gestión de inventarios en tiempo real con integración IoT",
        "client": "LogisticsCorp",
        "start_date": date.today() - timedelta(days=30),
        "budget": 75000,
        "presential": False
    },
    {
        "name": "App Móvil de Delivery",
        "description": "Aplicación móvil para pedidos y entregas a domicilio con geolocalización",
        "client": "FoodExpress",
        "start_date": date.today() - timedelta(days=15),
        "budget": 95000,
        "presential": True
    },
    {
        "name": "Plataforma E-learning",
        "description": "Sistema de aprendizaje en línea con cursos interactivos y certificación",
        "client": "EduTech Solutions",
        "start_date": date.today() - timedelta(days=45),
        "budget": 120000,
        "presential": False
    },
    {
        "name": "Dashboard Analytics Empresarial",
        "description": "Panel de control con métricas en tiempo real y reportes automatizados",
        "client": "BusinessMetrics Inc",
        "start_date": date.today() - timedelta(days=20),
        "budget": 65000,
        "presential": False
    },
    {
        "name": "Sistema de Reserva de Hoteles",
        "description": "Plataforma de reservas hoteleras con integración de pagos y APIs externas",
        "client": "HotelChain Group",
        "start_date": date.today() - timedelta(days=60),
        "budget": 85000,
        "presential": True
    },
    {
        "name": "App de Fitness y Salud",
        "description": "Aplicación móvil para seguimiento de actividad física y nutrición",
        "client": "HealthTech Labs",
        "start_date": date.today() - timedelta(days=25),
        "budget": 55000,
        "presential": False
    },
    {
        "name": "Plataforma de Comercio Electrónico",
        "description": "Tienda online completa con carrito de compras y pasarela de pagos",
        "client": "ShopOnline Ltd",
        "start_date": date.today() - timedelta(days=35),
        "budget": 110000,
        "presential": False
    },
    {
        "name": "Sistema de Gestión Hospitalaria",
        "description": "Software médico para gestión de pacientes y citas médicas",
        "client": "MediCare Systems",
        "start_date": date.today() - timedelta(days=50),
        "budget": 150000,
        "presential": True
    },
    {
        "name": "Red Social Profesional",
        "description": "Plataforma de networking profesional con perfiles y conexiones",
        "client": "ConnectPro Network",
        "start_date": date.today() - timedelta(days=40),
        "budget": 90000,
        "presential": False
    },
    {
        "name": "App de Transporte Compartido",
        "description": "Aplicación para compartir viajes con sistema de calificaciones",
        "client": "RideShare Co",
        "start_date": date.today() - timedelta(days=18),
        "budget": 70000,
        "presential": True
    },
    {
        "name": "Sistema de Control de Calidad",
        "description": "Plataforma para control de calidad en procesos manufactureros",
        "client": "QualityControl Inc",
        "start_date": date.today() - timedelta(days=55),
        "budget": 80000,
        "presential": True
    },
    {
        "name": "Portal de Noticias Interactivo",
        "description": "Sitio web de noticias con comentarios y personalización de contenido",
        "client": "NewsPortal Media",
        "start_date": date.today() - timedelta(days=28),
        "budget": 60000,
        "presential": False
    },
    {
        "name": "Sistema de Gestión Bancaria",
        "description": "Aplicación bancaria con transferencias y gestión de cuentas",
        "client": "SecureBank Corp",
        "start_date": date.today() - timedelta(days=70),
        "budget": 180000,
        "presential": True
    },
    {
        "name": "Plataforma de Streaming Musical",
        "description": "Servicio de streaming de música con playlists personalizadas",
        "client": "MusicStream Ltd",
        "start_date": date.today() - timedelta(days=22),
        "budget": 95000,
        "presential": False
    },
    {
        "name": "App de Gestión de Tareas",
        "description": "Aplicación para organización personal y equipos de trabajo",
        "client": "TaskMaster Pro",
        "start_date": date.today() - timedelta(days=12),
        "budget": 45000,
        "presential": False
    },
    {
        "name": "Sistema de Videoconferencias",
        "description": "Plataforma de reuniones virtuales con grabación y compartición",
        "client": "MeetOnline Inc",
        "start_date": date.today() - timedelta(days=38),
        "budget": 125000,
        "presential": False
    },
    {
        "name": "Marketplace de Servicios",
        "description": "Plataforma para conectar freelancers con empresas",
        "client": "ServiceMarket Hub",
        "start_date": date.today() - timedelta(days=32),
        "budget": 78000,
        "presential": False
    },
    {
        "name": "Sistema de Monitoreo IoT",
        "description": "Dashboard para monitoreo de dispositivos IoT industriales",
        "client": "IoT Solutions Corp",
        "start_date": date.today() - timedelta(days=48),
        "budget": 105000,
        "presential": True
    },
    {
        "name": "App de Realidad Aumentada",
        "description": "Aplicación móvil con experiencias de realidad aumentada",
        "client": "AR Experiences Ltd",
        "start_date": date.today() - timedelta(days=16),
        "budget": 85000,
        "presential": False
    },
    {
        "name": "Plataforma de Crowdfunding",
        "description": "Sistema para recaudación de fondos con campañas y donaciones",
        "client": "FundRaise Platform",
        "start_date": date.today() - timedelta(days=42),
        "budget": 92000,
        "presential": False
    },
    {
        "name": "Sistema de Gestión Documental",
        "description": "Repositorio digital con búsqueda y versionado de documentos",
        "client": "DocuManage Systems",
        "start_date": date.today() - timedelta(days=58),
        "budget": 68000,
        "presential": True
    },
    {
        "name": "App de Seguimiento Deportivo",
        "description": "Aplicación para seguimiento de rendimiento deportivo",
        "client": "SportTrack Pro",
        "start_date": date.today() - timedelta(days=8),
        "budget": 52000,
        "presential": False
    },
    {
        "name": "Plataforma de Encuestas Online",
        "description": "Herramienta para crear y analizar encuestas interactivas",
        "client": "SurveyMaster Inc",
        "start_date": date.today() - timedelta(days=26),
        "budget": 58000,
        "presential": False
    },
    {
        "name": "Sistema de Control de Acceso",
        "description": "Sistema de seguridad con control de acceso biométrico",
        "client": "SecureAccess Corp",
        "start_date": date.today() - timedelta(days=65),
        "budget": 135000,
        "presential": True
    },
    {
        "name": "Red Social para Mascotas",
        "description": "Plataforma para dueños de mascotas con comunidad y servicios",
        "client": "PetSocial Network",
        "start_date": date.today() - timedelta(days=19),
        "budget": 62000,
        "presential": False
    },
    {
        "name": "App de Recetas Inteligente",
        "description": "Aplicación de cocina con recomendaciones basadas en IA",
        "client": "SmartChef AI",
        "start_date": date.today() - timedelta(days=14),
        "budget": 48000,
        "presential": False
    },
    {
        "name": "Plataforma de Telemedicina",
        "description": "Sistema de consultas médicas remotas con videollamadas",
        "client": "TeleHealth Solutions",
        "start_date": date.today() - timedelta(days=52),
        "budget": 140000,
        "presential": True
    },
    {
        "name": "Sistema de Gestión Escolar",
        "description": "Plataforma para administración de instituciones educativas",
        "client": "EduManage Systems",
        "start_date": date.today() - timedelta(days=44),
        "budget": 98000,
        "presential": True
    },
    {
        "name": "App de Viajes y Turismo",
        "description": "Guía turística interactiva con reservas y recomendaciones",
        "client": "TravelGuide Pro",
        "start_date": date.today() - timedelta(days=21),
        "budget": 72000,
        "presential": False
    },
    {
        "name": "Plataforma de Subastas Online",
        "description": "Sistema de subastas en tiempo real con pujas automáticas",
        "client": "BidMaster Auctions",
        "start_date": date.today() - timedelta(days=36),
        "budget": 88000,
        "presential": False
    }
]

# ============================================
# ASIGNACIONES ALEATORIAS EMPLEADO-PROYECTO
# ============================================

def generate_random_assignments(num_assignments=200):
    """
    Genera asignaciones aleatorias entre empleados y proyectos.

    Args:
        num_assignments: Número de asignaciones a generar

    Returns:
        Lista de diccionarios con employee_id y project_id
    """
    assignments = []
    employee_ids = list(range(1, 101))  # IDs de empleados (1-100)
    project_ids = list(range(1, 31))    # IDs de proyectos (1-30)

    for _ in range(num_assignments):
        employee_id = random.choice(employee_ids)
        project_id = random.choice(project_ids)

        # Evitar duplicados
        assignment = {"employee_id": employee_id, "project_id": project_id}
        if assignment not in assignments:
            assignments.append(assignment)

    # Limitar a asignaciones únicas
    return assignments[:min(num_assignments, len(employee_ids) * len(project_ids))]

ASSIGNMENTS_DATA = generate_random_assignments(150)  # 150 asignaciones aleatorias

# ============================================
# EXPORTACIÓN DE DATOS
# ============================================

if __name__ == "__main__":
    print("[DATA] DATOS DE PRUEBA GENERADOS:")
    print(f"   • {len(PROFILES_DATA)} perfiles")
    print(f"   • {len(EMPLOYEES_DATA)} empleados")
    print(f"   • {len(PROJECTS_DATA)} proyectos")
    print(f"   • {len(ASSIGNMENTS_DATA)} asignaciones empleado-proyecto")
    print(f"   • Total registros: {len(PROFILES_DATA) + len(EMPLOYEES_DATA) + len(PROJECTS_DATA) + len(ASSIGNMENTS_DATA)}")
