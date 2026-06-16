from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer

# Modelo para vectorizar texto
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Conectar a Milvus Lite
client = MilvusClient("./peliculas.db")

# Crear coleccion
if client.has_collection("peliculas"):
    client.drop_collection("peliculas")

client.create_collection(
    collection_name="peliculas",
    dimension=384
)

# Dataset de peliculas
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

# Vectorizar descripciones
print("Vectorizando datos...")
textos = [p["descripcion"] for p in peliculas]
vectores = modelo.encode(textos).tolist()

# Mostrar cómo se ve un vector
print("\nPrimeros 10 valores del vector de la primera película:")
print(vectores[0][:10])

print("\nDimensión del vector:")
print(len(vectores[0]))

# Preparar datos
datos = [
    {
        "id": peliculas[i]["id"],
        "titulo": peliculas[i]["titulo"],
        "descripcion": peliculas[i]["descripcion"],
        "vector": vectores[i]
    }
    for i in range(len(peliculas))
]

# Insertar en Milvus
client.insert(collection_name="peliculas", data=datos)

print("Coleccion creada y datos cargados correctamente!")
print(f"Total de peliculas insertadas: {len(peliculas)}")