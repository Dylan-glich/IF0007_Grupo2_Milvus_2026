from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer

# Conectar a la base de datos
modelo = SentenceTransformer("all-MiniLM-L6-v2")
client = MilvusClient("./peliculas.db")

# Dataset original para simular SQL
peliculas = [
    {"id": 1, "titulo": "Iron Man",        "descripcion": "Un millonario construye una armadura para convertirse en superheroe"},
    {"id": 2, "titulo": "Batman",          "descripcion": "Un hombre con traje de murcielago lucha contra el crimen en Gotham"},
    {"id": 3, "titulo": "El Rey Lion",     "descripcion": "Un cachorro de leon debe reclamar su reino en la selva africana"},
    {"id": 4, "titulo": "Titanic",         "descripcion": "Una historia de amor en un barco que se hunde en el oceano"},
    {"id": 5, "titulo": "Interstellar",    "descripcion": "Astronautas viajan a traves de un agujero de gusano para salvar la humanidad"},
    {"id": 6, "titulo": "Thor",            "descripcion": "Un dios nordico con un martillo lucha contra villanos en la Tierra"},
    {"id": 7, "titulo": "Frozen",          "descripcion": "Una princesa con poderes de hielo debe salvar a su reino"},
    {"id": 8, "titulo": "Gravity",         "descripcion": "Una astronauta queda atrapada sola en el espacio exterior"},
    {"id": 9, "titulo": "Romeo y Julieta", "descripcion": "Dos jovenes de familias enemigas se enamoran perdidamente"},
    {"id": 10, "titulo": "Avengers",       "descripcion": "Un grupo de superheroes se une para salvar el mundo"},
]

# Consulta del usuario
consulta = input("Escribe lo que quieres buscar: ")

# ------------------------------
# CONSULTA SQL TRADICIONAL
# ------------------------------
print("\n--- Resultado SQL tradicional ---")
print("(Busca si la palabra exacta aparece en el titulo o descripcion)\n")

resultados_sql = []
for pelicula in peliculas:
    if consulta.lower() in pelicula["titulo"].lower() or consulta.lower() in pelicula["descripcion"].lower():
        resultados_sql.append(pelicula)

if len(resultados_sql) == 0:
    print("No se encontraron resultados con esa palabra exacta")
else:
    for r in resultados_sql:
        print("Titulo: " + r["titulo"])
        print("Descripcion: " + r["descripcion"])
        print("")

# ------------------------------
# CONSULTA VECTORIAL CON MILVUS
# ------------------------------
print("\n--- Resultado vectorial con Milvus ---")
print("(Busca por similitud de significado, no por palabra exacta)\n")

vector_consulta = modelo.encode([consulta]).tolist()

resultados_milvus = client.search(
    collection_name="peliculas",
    data=vector_consulta,
    limit=3,
    output_fields=["titulo", "descripcion"]
)

for resultado in resultados_milvus[0]:
    titulo = resultado["entity"]["titulo"]
    descripcion = resultado["entity"]["descripcion"]
    similitud = round(resultado["distance"], 4)
    print("Titulo: " + titulo)
    print("Descripcion: " + descripcion)
    print("Similitud: " + str(similitud))
    print("")