# IF0007 - Grupo 2 - Milvus

### Bases de Datos I - Universidad de Costa Rica

#### Sede Regional del Caribe | Recinto de Limón

#### Docente: Dr. Carlos Morales Castro

---

## Descripción del proyecto

Este repositorio contiene el trabajo de investigación sobre bases de datos vectoriales, específicamente sobre Milvus. Incluye una parte práctica donde se demuestra cómo crear una base de datos vectorial local utilizando Milvus Lite, generar embeddings y realizar búsquedas semánticas. Además, se incluye una comparación con consultas SQL tradicionales realizadas en PostgreSQL utilizando el mismo conjunto de datos.

---

## Objetivo General

Implementar una solución basada en Milvus Lite que permita almacenar embeddings vectoriales y realizar búsquedas semánticas, comparando sus resultados con consultas tradicionales basadas en coincidencia textual.

---

## Integrantes

* Richard Bucardo Cajina
* Zulay Bustos Chacón
* Dylan Cardona Castillo

---

## ¿Qué es Milvus?

Milvus es una base de datos vectorial distribuida de código abierto desarrollada por Zilliz. Está diseñada para almacenar, indexar y consultar grandes volúmenes de vectores utilizados en aplicaciones de Inteligencia Artificial.

A diferencia de una base de datos relacional tradicional, Milvus permite realizar búsquedas por similitud semántica, recuperando información relacionada por significado en lugar de depender únicamente de coincidencias exactas de palabras.

---

## Modos de despliegue

* **Milvus Lite**: Biblioteca Python ligera instalable mediante pip. Ideal para pruebas y proyectos académicos. Es la versión utilizada en este proyecto.
* **Milvus Standalone**: Implementación de nodo único apta para manejar grandes volúmenes de vectores.
* **Milvus Distributed**: Arquitectura distribuida diseñada para manejar miles de millones de vectores a gran escala.

---

## Estructura del proyecto

### Archivos de Milvus

* **prueba.py** – Verifica que Milvus Lite esté instalado correctamente.
* **datos.py** – Crea la colección de películas, genera los embeddings e inserta los datos en Milvus.
* **busqueda.py** – Realiza búsquedas semánticas mediante similitud vectorial.

### Archivo de PostgreSQL

* **Peliculas.sql** – Crea la base de datos, la tabla, inserta los registros y ejecuta las consultas SQL utilizadas para comparar PostgreSQL con Milvus.

### Otros archivos

* **README.md** – Documentación del proyecto.
* **.gitignore** – Archivos excluidos del repositorio.

---

## Requisitos

* Windows 10 o superior
* Python 3.11
* Visual Studio Code

---

## Instalación

### 1. Instalar Python 3.11

Descargue Python 3.11 desde:

https://www.python.org/downloads/release/python-3119/

Seleccione:

```text
Windows installer (64-bit)
```

Durante la instalación marque la opción:

```text
Add Python to PATH
```

---

### 2. Instalar Visual Studio Code

Descargue Visual Studio Code desde:

https://code.visualstudio.com/

---

### 3. Instalar la extensión PowerShell

Abra Visual Studio Code, acceda al apartado de extensiones, busque **PowerShell** e instálela.

---

### 4. Crear la carpeta del proyecto

Cree una carpeta llamada:

```text
Milvus
```

Luego selecciónela desde:

```text
File → Open Folder
```

---

### 5. Abrir la terminal

En Visual Studio Code seleccione:

```text
Terminal → New Terminal
```

---

### 6. Permitir la ejecución de scripts en Windows

Ejecutar una única vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando Windows lo solicite, escribir:

```text
S
```

y presionar Enter.

---

### 7. Crear el entorno virtual

```powershell
py -3.11 -m venv venv
```

---

### 8. Activar el entorno virtual

```powershell
venv\Scripts\activate
```

La activación fue exitosa cuando aparece:

```text
(venv)
```

al inicio de la terminal.

---

### 9. Instalar Milvus Lite

```powershell
pip install pymilvus milvus-lite
```

---

### 10. Instalar Sentence Transformers

```powershell
pip install sentence-transformers
```

---

## Ejecución del proyecto

### 1. Verificar la instalación

```powershell
python prueba.py
```

Si aparece el mensaje:

```text
Milvus Lite funciona correctamente!
```

la instalación fue exitosa.

---

### 2. Cargar los datos en Milvus

```powershell
python datos.py
```

Este script:

* Crea la colección `peliculas`.
* Genera embeddings de 384 dimensiones utilizando el modelo `all-MiniLM-L6-v2`.
* Inserta las 10 películas de prueba.
* Muestra información sobre los vectores generados.

La primera ejecución descargará automáticamente el modelo de embeddings (aproximadamente 90 MB).

---

### 3. Ejecutar una búsqueda semántica

```powershell
python busqueda.py
```

El programa solicitará una consulta de texto, por ejemplo:

```text
superheroes
amor
espacio
```

La consulta será convertida en un embedding y comparada con los vectores almacenados en Milvus.

Como resultado se mostrarán las películas más cercanas semánticamente junto con su distancia de similitud.

---

### 4. Ejecutar la comparación en PostgreSQL

Abra PostgreSQL y ejecute:

```sql
Peliculas.sql
```

Este script:

* Crea la base de datos.
* Crea la tabla de películas.
* Inserta los registros.
* Ejecuta consultas mediante `ILIKE`.

Los resultados permiten comparar una búsqueda basada en coincidencia textual con la búsqueda semántica realizada por Milvus.

---

## Tecnologías utilizadas

* Python 3.11
* Milvus Lite
* PostgreSQL
* Sentence Transformers
* Modelo all-MiniLM-L6-v2
* Visual Studio Code

---

## Licencia

Este proyecto fue desarrollado con fines académicos para el curso IF0007 – Bases de Datos I.

---

**Universidad de Costa Rica**
**Sede Regional del Caribe | Recinto de Limón**
**IF0007 – Bases de Datos I**
**2026**
