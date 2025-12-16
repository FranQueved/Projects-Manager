"""
DATOS DE PRUEBA PARA EL EJEMPLO DE SERVICIOS
=============================================

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
        "hardSkills": "Python, Django, PostgreSQL, REST APIs",
        "softSkills": "Comunicación, Trabajo en equipo, Liderazgo",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "JavaScript, React, Node.js, MongoDB",
        "softSkills": "Creatividad, Resolución de problemas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Java, Spring Boot, MySQL, Microservicios",
        "softSkills": "Análisis, Planificación estratégica",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "C#, .NET, SQL Server, Azure",
        "softSkills": "Adaptabilidad, Aprendizaje continuo",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "PHP, Laravel, MySQL, HTML/CSS",
        "softSkills": "Atención al detalle, Paciencia",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Ruby, Rails, PostgreSQL, AWS",
        "softSkills": "Innovación, Pensamiento crítico",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Go, Docker, Kubernetes, Linux",
        "softSkills": "Resiliencia, Trabajo bajo presión",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Swift, iOS, Xcode, Core Data",
        "softSkills": "Creatividad, Diseño UX/UI",
        "languages": "Español, Inglés, Catalán"
    },
    {
        "hardSkills": "Kotlin, Android, Firebase, MVVM",
        "softSkills": "Empatía, Comunicación efectiva",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "TypeScript, Angular, RxJS, NgRx",
        "softSkills": "Mentoría, Desarrollo de equipos",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Python, FastAPI, SQLAlchemy, Pydantic",
        "softSkills": "Curiosidad, Aprendizaje autónomo",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "JavaScript, Vue.js, Nuxt.js, GraphQL",
        "softSkills": "Flexibilidad, Adaptabilidad",
        "languages": "Español, Inglés, Japonés"
    },
    {
        "hardSkills": "C++, Qt, OpenGL, Linux",
        "softSkills": "Precisión, Análisis técnico",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Scala, Play Framework, Akka, Cassandra",
        "softSkills": "Visión estratégica, Planificación",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Rust, WebAssembly, Tokio, Async",
        "softSkills": "Innovación, Experimentación",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Dart, Flutter, Firebase, Provider",
        "softSkills": "Creatividad, Diseño centrado en usuario",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Elixir, Phoenix, PostgreSQL, OTP",
        "softSkills": "Resiliencia, Pensamiento distribuido",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Clojure, Datomic, Ring, Compojure",
        "softSkills": "Abstracción, Pensamiento funcional",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Haskell, Servant, PostgreSQL, Lens",
        "softSkills": "Rigor matemático, Pureza funcional",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "R, Python, Pandas, TensorFlow",
        "softSkills": "Análisis de datos, Interpretación",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Python, PyTorch, CUDA, Deep Learning",
        "softSkills": "Experimentación, Validación",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "SQL, ETL, Airflow, Snowflake",
        "softSkills": "Organización, Metodología",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Tableau, Power BI, DAX, Storytelling",
        "softSkills": "Comunicación visual, Narrativa",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Figma, Sketch, Adobe XD, Prototyping",
        "softSkills": "Diseño thinking, Empatía usuario",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Jenkins, GitLab CI, Docker, Kubernetes",
        "softSkills": "Automatización, Mejora continua",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Terraform, AWS, Azure, GCP",
        "softSkills": "Arquitectura cloud, Escalabilidad",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Linux, Bash, Python, Monitoring",
        "softSkills": "Troubleshooting, Proactividad",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Scrum, Kanban, Agile, JIRA",
        "softSkills": "Facilitación, Coaching",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "React Native, Expo, Redux, TypeScript",
        "softSkills": "Movilidad, Experiencia móvil",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Unity, C#, AR/VR, Game Physics",
        "softSkills": "Creatividad, Experiencia inmersiva",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Solidity, Web3, Ethereum, Smart Contracts",
        "softSkills": "Descentralización, Seguridad blockchain",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "MATLAB, Simulink, Control Systems",
        "softSkills": "Modelado matemático, Simulación",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "SAP ABAP, Fiori, HANA, BW",
        "softSkills": "Procesos empresariales, ERP",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Salesforce, Apex, Lightning, SOQL",
        "softSkills": "CRM, Automatización ventas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "MuleSoft, Anypoint, Integration, APIs",
        "softSkills": "Conectividad, Arquitectura integración",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "PowerShell, Active Directory, Windows Server",
        "softSkills": "Administración sistemas, Automatización",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Arduino, Raspberry Pi, IoT, Sensors",
        "softSkills": "Prototipado, Hardware/Software",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Qt, QML, C++, Embedded Systems",
        "softSkills": "Interfaces táctiles, UX embedded",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Ansible, Puppet, Chef, Infrastructure as Code",
        "softSkills": "Automatización infraestructura, DevOps",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Prometheus, Grafana, ELK Stack, Monitoring",
        "softSkills": "Observabilidad, Alerting",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Kafka, RabbitMQ, Event Streaming, Microservices",
        "softSkills": "Arquitectura orientada a eventos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "OpenShift, Istio, Service Mesh, Microservices",
        "softSkills": "Orquestación contenedores, Escalabilidad",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "React, Redux, TypeScript, Next.js",
        "softSkills": "Desarrollo frontend moderno",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Vue.js, Nuxt.js, Pinia, Composition API",
        "softSkills": "Reutilización componentes, DX",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Angular, RxJS, NgRx, Material Design",
        "softSkills": "Arquitectura enterprise, Testing",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Svelte, SvelteKit, Stores, Transitions",
        "softSkills": "Performance, Experiencia developer",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Express.js, NestJS, TypeORM, Swagger",
        "softSkills": "APIs RESTful, Documentación",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Django REST, DRF, Celery, Redis",
        "softSkills": "Backend robusto, Tareas asíncronas",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Flask, SQLAlchemy, Marshmallow, JWT",
        "softSkills": "Microframeworks, Flexibilidad",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Spring Boot, JPA, Hibernate, Security",
        "softSkills": "Enterprise Java, Persistencia",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": ".NET Core, Entity Framework, Identity, SignalR",
        "softSkills": "Plataforma Microsoft, Tiempo real",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Laravel, Livewire, Alpine.js, MySQL",
        "softSkills": "Fullstack PHP, SPA sin JS complejo",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Symfony, Doctrine, Twig, API Platform",
        "softSkills": "Arquitectura PHP enterprise",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Ruby on Rails, Hotwire, PostgreSQL, Sidekiq",
        "softSkills": "Conventions over configuration",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Phoenix, Elixir, Ecto, LiveView",
        "softSkills": "Concurrencia, Tiempo real",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Django, Wagtail CMS, PostgreSQL, Elasticsearch",
        "softSkills": "CMS moderno, Búsqueda avanzada",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Strapi, Headless CMS, GraphQL, Admin Panel",
        "softSkills": "Content management, API-first",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "WordPress, WooCommerce, PHP, MySQL",
        "softSkills": "E-commerce, Plugins ecosystem",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Shopify, Liquid, JavaScript, Apps",
        "softSkills": "E-commerce SaaS, Customización",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Magento, PHP, MySQL, Elasticsearch",
        "softSkills": "E-commerce enterprise, Escalabilidad",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "PrestaShop, PHP, Smarty, Modules",
        "softSkills": "E-commerce open source",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Odoo, Python, PostgreSQL, XML",
        "softSkills": "ERP open source, Modularidad",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "SuiteCRM, PHP, MySQL, SugarCRM",
        "softSkills": "CRM open source, Personalización",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Moodle, PHP, MySQL, SCORM",
        "softSkills": "E-learning, LMS",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Canvas LMS, Ruby, PostgreSQL, LTI",
        "softSkills": "E-learning enterprise",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Google Cloud, Firebase, BigQuery, ML Engine",
        "softSkills": "Cloud computing, Machine Learning",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "AWS Lambda, S3, DynamoDB, CloudFormation",
        "softSkills": "Serverless, Infraestructura como código",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Azure Functions, Blob Storage, Cosmos DB, ARM",
        "softSkills": "Cloud Microsoft, Enterprise",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Docker, Kubernetes, Helm, Istio",
        "softSkills": "Contenedorización, Orquestación",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Terraform, Ansible, Packer, Vault",
        "softSkills": "Infrastructure as Code, DevOps",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Jenkins, GitLab CI, GitHub Actions, ArgoCD",
        "softSkills": "CI/CD, Automatización despliegues",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "PostgreSQL, MongoDB, Redis, Elasticsearch",
        "softSkills": "Bases de datos, Búsqueda, Cache",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "MySQL, MariaDB, Percona, Galera",
        "softSkills": "Bases de datos relacionales, Alta disponibilidad",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Oracle, SQL Server, DB2, PL/SQL",
        "softSkills": "Bases de datos enterprise",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "SQLite, LevelDB, RocksDB, Time Series",
        "softSkills": "Bases de datos embebidas, Series temporales",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Prometheus, Grafana, Loki, Tempo",
        "softSkills": "Observabilidad, Métricas, Logs, Trazas",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "ELK Stack, Fluentd, Kafka, ClickHouse",
        "softSkills": "Big Data, Análisis de logs",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Apache Spark, Hadoop, Hive, Presto",
        "softSkills": "Big Data processing, Data lakes",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Airflow, Prefect, Dagster, DBT",
        "softSkills": "Data pipelines, Orchestration",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Pandas, NumPy, Scikit-learn, Jupyter",
        "softSkills": "Data Science, Machine Learning",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "TensorFlow, PyTorch, Keras, OpenCV",
        "softSkills": "Deep Learning, Computer Vision",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "NLP, spaCy, Transformers, BERT",
        "softSkills": "Procesamiento de lenguaje natural",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Tableau, Power BI, Looker, Metabase",
        "softSkills": "Business Intelligence, Visualización",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Figma, Adobe XD, Sketch, InVision",
        "softSkills": "UI/UX Design, Prototipado",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "Photoshop, Illustrator, After Effects, Premiere",
        "softSkills": "Diseño gráfico, Motion graphics",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Blender, Maya, 3ds Max, ZBrush",
        "softSkills": "Modelado 3D, Animación",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Unity, Unreal Engine, Godot, Game Design",
        "softSkills": "Desarrollo de videojuegos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Arduino, Raspberry Pi, ESP32, IoT",
        "softSkills": "Prototipado hardware, Electrónica",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "MATLAB, Simulink, LabVIEW, Control Systems",
        "softSkills": "Sistemas de control, Automatización industrial",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "SolidWorks, AutoCAD, CATIA, Mechanical Design",
        "softSkills": "Diseño mecánico, CAD",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "ANSYS, COMSOL, CFD, FEA",
        "softSkills": "Simulación ingenieril, Análisis numérico",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "PLC Programming, SCADA, Industrial Networks",
        "softSkills": "Automatización industrial, Control de procesos",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Embedded C, RTOS, ARM, Microcontrollers",
        "softSkills": "Sistemas embebidos, Programación de bajo nivel",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "VHDL, Verilog, FPGA, ASIC Design",
        "softSkills": "Diseño digital, Lógica programable",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "ROS, Gazebo, Navigation, Computer Vision",
        "softSkills": "Robótica, Sistemas autónomos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Blockchain, Solidity, Web3.js, DeFi",
        "softSkills": "Tecnología descentralizada, Criptoeconomía",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Quantum Computing, Qiskit, Cirq, Q#",
        "softSkills": "Computación cuántica, Algoritmos cuánticos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Bioinformatics, R, Python, Genomics",
        "softSkills": "Análisis biológico, Secuenciación",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "GIS, ArcGIS, QGIS, GeoServer",
        "softSkills": "Sistemas de información geográfica",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Cybersecurity, Ethical Hacking, SIEM, SOC",
        "softSkills": "Seguridad informática, Análisis de amenazas",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Cryptography, PKI, SSL/TLS, Zero Trust",
        "softSkills": "Criptografía, Seguridad de comunicaciones",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Penetration Testing, OWASP, Burp Suite, Metasploit",
        "softSkills": "Testing de seguridad, Ethical hacking",
        "languages": "Español, Inglés, Portugués"
    },
    {
        "hardSkills": "Compliance, GDPR, ISO 27001, Risk Assessment",
        "softSkills": "Cumplimiento normativo, Gestión de riesgos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Digital Forensics, Memory Analysis, Malware Analysis",
        "softSkills": "Investigación digital, Análisis forense",
        "languages": "Español, Inglés, Francés"
    },
    {
        "hardSkills": "Agile, Scrum, Kanban, XP, Lean",
        "softSkills": "Metodologías ágiles, Gestión de proyectos",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Product Management, Roadmap, User Stories, A/B Testing",
        "softSkills": "Gestión de producto, Validación de hipótesis",
        "languages": "Español, Inglés, Alemán"
    },
    {
        "hardSkills": "UX Research, User Testing, Usability, Accessibility",
        "softSkills": "Investigación de usuario, Diseño centrado en humano",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Growth Hacking, Analytics, SEO, SEM",
        "softSkills": "Crecimiento de producto, Marketing digital",
        "languages": "Español, Inglés, Italiano"
    },
    {
        "hardSkills": "Technical Writing, Documentation, API Docs, MkDocs",
        "softSkills": "Comunicación técnica, Documentación",
        "languages": "Español, Inglés"
    },
    {
        "hardSkills": "Teaching, Mentoring, Curriculum Design, Online Learning",
        "softSkills": "Educación, Desarrollo profesional",
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
    print("📊 DATOS DE PRUEBA GENERADOS:")
    print(f"   • {len(PROFILES_DATA)} perfiles")
    print(f"   • {len(EMPLOYEES_DATA)} empleados")
    print(f"   • {len(PROJECTS_DATA)} proyectos")
    print(f"   • {len(ASSIGNMENTS_DATA)} asignaciones empleado-proyecto")
    print(f"   • Total registros: {len(PROFILES_DATA) + len(EMPLOYEES_DATA) + len(PROJECTS_DATA) + len(ASSIGNMENTS_DATA)}")