
# IF0007 - Grupo 2 - Milvus
### Bases de Datos I — Universidad de Costa Rica
#### Sede Regional del Caribe | Recinto de Limon
#### Docente: Dr. Carlos Morales Castro

---

## Descripcion del proyecto
Este repositorio contiene el trabajo de investigacion sobre bases de datos vectoriales, especificamente sobre Milvus. Incluye una parte practica donde se demuestra como crear una base de datos vectorial local usando Milvus Lite, cargar datos y realizar busquedas semanticas comparadas con consultas SQL tradicionales.

---

## Integrantes
- Richard Bucardo Cajina
- Zulay Bustos Chacon
- Dylan Angelo Cardona Castillo


---

## Que es Milvus
Milvus es una base de datos vectorial distribuida de codigo abierto desarrollada por Zilliz. Su nombre proviene del ave rapaz del genero Milvus, reconocida por su velocidad, vision aguda y adaptabilidad, cualidades que el equipo busco emular en el diseno del sistema.

Zilliz comenzo a desarrollar Milvus en 2017 y lo dono a la LF AI & Data Foundation bajo la Linux Foundation en enero de 2020. Se distribuye bajo la Licencia Apache 2.0, lo que garantiza acceso libre al codigo fuente sin restricciones de uso.

A diferencia de una base de datos relacional tradicional, Milvus no busca por coincidencia exacta de palabras sino por similitud de significado, lo que lo hace ideal para aplicaciones de inteligencia artificial.

---

## Modos de despliegue
- **Milvus Lite** — biblioteca Python ligera, instalable con pip. Ideal para pruebas y proyectos pequenos. Es el modo que usamos en este proyecto.
- **Milvus Standalone** — nodo unico apto para hasta 100 millones de vectores.
- **Milvus Distributed** — arquitectura distribuida para manejar miles de millones de vectores a gran escala.

---

## Archivos del repositorio
- **Prueba.py** — verifica que Milvus Lite esta instalado correctamente
- **datos.py** — crea la coleccion de peliculas y carga los datos vectorizados
- **busqueda.py** — realiza la consulta semantica y la compara con SQL tradicional
- **.gitignore** — indica a Git que archivos no subir al repositorio

---

## Requisitos
- Windows 10 o superior
- Python 3.11
- Visual Studio Code

---

## Instalacion
**1. Instala Python**
Entra a python.org/downloads y descarga la version mas reciente. Durante la instalacion respondele que si a las dos preguntas que aparecen.

**2. Instala Visual Studio Code**
Entra a code.visualstudio.com y descargalo.

**3. Instala la extension de PowerShell en VS Code**
Abre VS Code, ve al icono de extensiones en la barra izquierda, busca PowerShell e instalala.

**4. Crea la carpeta del proyecto**
Crea una carpeta llamada Milvus en el escritorio. Luego en VS Code ve a File, Open Folder y seleccionala.

**5. Abre la terminal**
En VS Code ve a Terminal, New Terminal.

**6. Permite ejecutar scripts en Windows (solo se hace una vez)**
Cuando te pregunte, escribe S y presiona Enter.
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**7. Instala Python 3.11**
Milvus Lite no es compatible con versiones muy nuevas de Python. Descarga Python 3.11 desde:
```
https://www.python.org/downloads/release/python-3119/
```
Baja hasta abajo y descarga Windows installer (64-bit). Durante la instalacion marca Add Python to PATH.

**8. Crea el entorno virtual**
```
py -3.11 -m venv venv
```

**9. Activa el entorno virtual**
```
venv\Scripts\activate
```
Sabes que funciono cuando aparece (venv) al inicio de la linea.

**10. Instala Milvus Lite**
```
pip install pymilvus milvus-lite
```

**11. Instala la libreria para vectorizar texto**
```
pip install sentence-transformers
```

---

## Como ejecutar el proyecto
Primero carga los datos:
```
python datos.py
```
La primera vez se descarga automaticamente el modelo de vectorizacion, un archivo de aproximadamente 90MB. Esto solo pasa una vez.

Luego ejecuta la busqueda:
```
python busqueda.py
```
El programa te pide que escribas algo, por ejemplo: superheroe, historia de amor, pelicula en el espacio. Luego muestra dos resultados: el de SQL tradicional y el de la busqueda vectorial con Milvus.

---

## Tecnologias usadas
- Python 3.11
- Milvus Lite (Apache 2.0)
- sentence-transformers
- Modelo all-MiniLM-L6-v2

---

*Universidad de Costa Rica — IF0007 Bases de Datos I — 2026*
