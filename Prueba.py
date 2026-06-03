from pymilvus import MilvusClient

# Crea una base de datos vectorial local
client = MilvusClient("./mi_base.db")

print("✅ Milvus Lite funciona correctamente!")
