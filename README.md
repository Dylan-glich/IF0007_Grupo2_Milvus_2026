IF0007 - Grupo 2 - Milvus
Bases de Datos I — Universidad de Costa Rica
Sede Regional del Caribe | Recinto de Limón
Docente: Dr. Carlos Morales Castro
Descripción del proyecto
Este repositorio contiene el trabajo de investigación sobre bases de datos vectoriales, específicamente sobre Milvus. Incluye una parte práctica donde se demuestra cómo crear una base de datos vectorial local usando Milvus Lite, cargar datos y realizar búsquedas semánticas comparadas con consultas SQL tradicionales.

Objetivo General
Implementar una solución basada en Milvus Lite que permite almacenar incrustaciones vectoriales y realizar búsquedas semánticas, comparando sus resultados con consultas tradicionales basadas en coincidencia exacta de palabras.

Integrantes
Richard Bucardo Cajina
Zulay Bustos Chacón
Dylan Cardona Castillo
¿Qué es Milvus?
Milvus es una base de datos vectoriales distribuida de código abierto desarrollado por Zilliz. Su nombre proviene del ave rapaz del genero Milvus, reconocido por su velocidad, visión aguda y adaptabilidad, cualidades que el equipo busco emular en el diseño del sistema.

Zilliz comenzó a desarrollar Milvus en 2017 y lo donó a la LF AI & Data Foundation bajo la Linux Foundation en enero de 2020. Se distribuye bajo la Licencia Apache 2.0, lo que garantiza acceso libre al código fuente sin restricciones de uso.

A diferencia de una base de datos relacional tradicional, Milvus no busca por coincidencia exacta de palabras sino por similitud de significado, lo que lo hace ideal para aplicaciones de inteligencia artificial.

Modos de despliegue
Milvus Lite : biblioteca Python ligera, instalable con pip. Ideal para pruebas y proyectos pequeños. Es el modo que usamos en este proyecto.
Milvus Standalone : ​​nodo único apto para hasta 100 millones de vectores.
Milvus Distributed : arquitectura distribuida para manejar millas de millones de vectores a gran escala.

## Estructura del proyecto
- **Milvus-Peliculas/Prueba.py** — verifica que Milvus Lite este instalado correctamente
- **Milvus-Peliculas/datos.py** — crea la coleccion de peliculas y carga los datos vectorizados
- **Milvus-Peliculas/busqueda.py** — realiza la consulta semantica con Milvus
- **Postgrest-Peliculas/script-tabla.sql** — crea la tabla en PostgreSQL con el estandar de nomenclatura
- **Postgrest-Peliculas/script-insert.sql** — inserta los mismos datos en PostgreSQL
- **Postgrest-Peliculas/script-consultas.sql** — consultas con ILIKE para comparar con Milvus
- **.gitignore** — indica a Git que archivos no subir al repositorio

Requisitos
Windows 10 o superior
Python 3.11
Código de Visual Studio
Instalación
1. Instale Python. Ingrese a python.org/downloads y descargue la versión más reciente. Durante la instalación responda que si a las dos preguntas que aparecen.

2. Instala Visual Studio Code Ingresa a code.visualstudio.com y descárgalo.

3. Instale la extensión de PowerShell en VS Code Abra VS Code, y al icono de extensiones en la barra izquierda, busque PowerShell e instale.

4. Crea la carpeta del proyecto Crea una carpeta llamada Milvus en el escritorio. Luego en VS Code ve a Archivo, Abrir carpeta y seleccionala.

5. Abre la terminal En VS Code ve a Terminal, New Terminal.

6. Permite ejecutar scripts en Windows (solo se hace una vez) Cuando te pregunte, escribe S y presiona Enter.

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
7. Instale Python 3.11 Milvus Lite no es compatible con versiones muy nuevas de Python. Descarga Python 3.11 desde:

https://www.python.org/downloads/release/python-3119/
Baja hasta abajo y descarga el instalador de Windows (64 bits). Durante la instalación marca Add Python to PATH.

8. Crea el entorno virtual

py -3.11 -m venv venv
9. Activa el entorno virtual

venv\Scripts\activate
Sabes que funciona cuando aparece (venv) al inicio de la linea.

10. Instala Milvus Lite

pip install pymilvus milvus-lite
11. Instale la librería para vectorizar texto

pip install sentence-transformers
Como ejecutar el proyecto
Primero carga los datos:

python datos.py
La primera vez se descarga automáticamente el modelo de vectorización, un archivo de aproximadamente 90MB. Esto solo pasó una vez.

Luego ejecuta la búsqueda:

python busqueda.py
El programa te pide que escribas algo, por ejemplo: superheroe, historia de amor, pelicula en el espacio. Luego muestra dos resultados: el de SQL tradicional y el de la busqueda vectorial con Milvus.

Tecnologías usadas
Python 3.11
Milvus Lite (Apache 2.0)
transformadores de oraciones
Modelo all-MiniLM-L6-v2
Universidad de Costa Rica — IF0007 Bases de Datos I — 2026
