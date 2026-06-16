from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer

# Conectar a la base de datos
modelo = SentenceTransformer("all-MiniLM-L6-v2")
client = MilvusClient("./peliculas.db")

# Consulta del usuario
consulta = input("Escribe lo que quieres buscar: ")

# Cargar la coleccion en memoria
client.load_collection("peliculas")

# Convertir la consulta en vector
vector_consulta = modelo.encode([consulta]).tolist()

resultados_milvus = client.search(
    collection_name="peliculas",
    data=vector_consulta,
    limit=3,
    output_fields=["titulo", "descripcion"]
)

# Mostrar resultados
print("\n--- Resultado vectorial con Milvus ---")
print("(Busca por cercanía semántica, no por palabra exacta)\n")

for resultado in resultados_milvus[0]:
    titulo = resultado["entity"]["titulo"]
    descripcion = resultado["entity"]["descripcion"]
    distancia = round(resultado["distance"], 4)
    print("Titulo: " + titulo)
    print("Descripcion: " + descripcion)
    print("Distancia: " + str(distancia))
    print("")